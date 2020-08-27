from rest_framework.permissions import BasePermission
from classbaseview.models import UserInfo


#权限类
class MyPermission(BasePermission):
      def has_permission(self,request,view):
          user = UserInfo.objects.filter(id=request.user).first()
          if user.user_type >= 2:
              return  True
          return  False