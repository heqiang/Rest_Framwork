# Create your views here.
import  hashlib
import time
import json
from collections  import OrderedDict
from django.http import JsonResponse,HttpResponse
from classbaseview.models import UserInfo,UserToken,UserGroup,Role
from classbaseview.serializers import UserSerializer,UserGroupSerlizer,GroupSerlizers
from classbaseview.util.Authication import Authication
from classbaseview.util.MyPermission import MyPermission
from classbaseview.util.Mythrottles import  MyBaseThrottle,VisitThrottle,UserThrottle
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.versioning import  URLPathVersioning
from classbaseview.models import UserInfo
from  rest_framework.serializers import  ValidationError
from classbaseview.util.pager import PagerRoleSerizers,PagerUserSerizers
from classbaseview.util.ViewSet import MyModelViewSetSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination,BasePagination,CursorPagination

""""
 增删改查：ModelViewSet
 增删：CreateModelMixin，DestroyModelMixin
 复杂逻辑 ：GenericViewSet,APIView
 
 PS:
"""
order_dict = {
    1:{
        "name":"洗发水",
        "age":11,
        "content":"ssss"
    },
    2: {
        "name": "老王",
        "age": 13,
        "content": "dsadas"
    },
    3: {
        "name": "老李",
        "age": 12,
        "content": "fdfff"
    }
}

def  md5(username):
    ctime = str(time.time())
    m = hashlib.md5(bytes(username,encoding="utf-8"))
    m.update(bytes(ctime,encoding="utf-8"))
    return m.hexdigest()

class UserViewset(APIView):
    """
    用户登录认证
    """
    authentication_classes = []
    def get(self, request, *args, **kwargs):

        return JsonResponse({"msg":"get"})

    def post(self, request, *args, **kwargs):
        res = {
            "code":200,
            "msg":""
        }

        user_type = request._request.POST.get("user_type")
        username = request._request.POST.get("username")
        password = request._request.POST.get("password")

        obj = UserInfo.objects.filter(username = username)
        if not obj:
            res["msg"] = "注册成功"
            UserInfo.objects.create(user_type=user_type, username=username, password=password)
            userid = obj.values().values().first()["id"]
            tokon = md5(username)
            UserToken.objects.update_or_create(user_id=userid, defaults={"token": tokon})
        else:
            if password ==obj.values().values().first()["password"]:
                userid = obj.values().values().first()["id"]
                res["msg"] = "登录成功"
                tokon = md5(username)
                UserToken.objects.update_or_create(user_id=userid ,defaults={"token":tokon})
            else:
                res["code"] = 300
                res["msg"] = "密码错误"
        return  JsonResponse(res)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass

class OrderViewset(APIView):
    """
    订单
    """
    message = "必须是vip及以上才有权访问"
    authentication_classes = [Authication]
    permission_classes = [MyPermission]
    throttle_classes = [UserThrottle,]

    def get(self,request,*args,**kwargs):

        ret = {

            "code":1000,
            "msg":None,
            "data":None,
        }
        try:
            ret["data"] = order_dict
        except Exception as e:
            pass
        return  JsonResponse(ret)

class UserView(APIView):

    versioning_class = URLPathVersioning

    def get(self,request,*args,**kwargs):
        VERSION = request.version
        return HttpResponse(VERSION)


class UserInfoView(APIView):
    # versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        users = UserInfo.objects.all()
        ser = UserSerializer(instance=users,many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)
class GroupView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = UserGroup.objects.filter(pk=pk).first()
        ser = UserGroupSerlizer(instance=obj, many=False)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)

###########################
"""
数据校验
  钩子函数
"""

class Group(APIView):

    def post(self,request,*args,**kwargs):
        ser = GroupSerlizers(data=request.data)
        ser.data
        msg = ""
        if ser.is_valid():
            title = ser.validated_data["title"]
            msg = "ok"
        else:
            msg = ser.errors["title"][0]
        return HttpResponse(msg)


"""
渲染-》rest的Response 翻页配置 
"""

class MyPageNumberPaginations(PageNumberPagination):
    """
    自定义 翻页参数及数量
    """
    page_size = 3
    # 路由每页参数
    page_size_query_param = "size"
    # 每页最大数量
    max_page_size = 6
    page_query_param = 'page'


class PagerView(APIView):

    def get(self,request,*args,**kwargs):
        roles = Role.objects.all()
        # rest自带的分页
        pg = CursorPagination()
        # 要么在setting中配置全局每页数量 要么如下指定
        # pg.cursor_query_param="s"
        pg.page_size=2
        #默认的排序规则
        pg.ordering = "id"
        pager_roles = pg.paginate_queryset(queryset=roles,request=request,view=self)

        #使用继承后的分页类
        # pg= MyPageNumberPaginations()
        # pager_roles = pg.paginate_queryset(queryset=roles,request=request,view=self)
        # 对分页数据进行序列化
        ser = PagerRoleSerizers(instance=pager_roles, many=True)
        # return Response(ser.data)
        # 直接返回下面的response 返回的数据中有上下页的链接及 数据的总数
        response = pg.get_paginated_response(ser.data)
        del response.data["next"]
        del  response.data["previous"]
        return  response


"""
GenericViewSet 和一般的不同的是
重新了as_view() GenericAPIView用处不大
"""

class MyGenericView(GenericViewSet):
    queryset = Role.objects.all()
    #序列化
    serializer_class = PagerRoleSerizers
    pagination_class = MyPageNumberPaginations
    def get(self,requests,*args,**kwargs):
        #数据获取
        user = self.get_queryset()
        pager_user = self.paginate_queryset(user)
        #序列化
        ser = self.get_serializer(instance=pager_user,many=True)
        response = self.get_paginated_response(ser.data)
        return response

"""
    ModelViewSet 使用
"""
class MyUserModelViewSet(ModelViewSet):
    queryset =  UserInfo.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = MyModelViewSetSerializer

