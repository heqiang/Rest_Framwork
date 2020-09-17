# Create your views here.
import  hashlib
import time
import json
from django.http import JsonResponse,HttpResponse
from classbaseview.models import UserInfo,UserToken,UserGroup
from classbaseview.serializers import UserSerializer,UserGroupSerlizer
from classbaseview.util.Authication import Authication
from classbaseview.util.MyPermission import MyPermission
from classbaseview.util.Mythrottles import  MyBaseThrottle,VisitThrottle,UserThrottle
from rest_framework.views import APIView
from rest_framework.versioning import  URLPathVersioning
from classbaseview.models import UserInfo

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
    def get(self, request, *args, **kwargs):
        users = UserInfo.objects.all()
        ser = UserSerializer(instance=users,many=True,context={'request': request})
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)
class GroupView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = UserGroup.objects.filter(pk=pk).first()
        ser = UserGroupSerlizer(instance=obj, many=False)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)