from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from classbaseview.models import UserToken


#认证类


class  Authication(BaseAuthentication):
    def authenticate(self,request):
        token = request._request.GET.get("token")
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("用户认证失败")
        #在rest framwork 内部会将返回两个字段赋值给request，以供后续操作
        return  token_obj.user_id,token_obj
    def authenticate_header(self,request):
        """
        认证失败返回给浏览器的相应头
        :param request:
        :return:
        """
        pass


class  Authication1(BaseAuthentication):
    def authenticate(self,request):
        pass
    def authenticate_header(self,request):
        pass
