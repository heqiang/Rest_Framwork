from abc import ABC
from classbaseview import models
from rest_framework import serializers
from classbaseview.models import UserInfo


class MovieSerializer(serializers.ModelSerializer):
    """
    创建一个序列器
    """
    Name = serializers.CharField()
    Url = serializers.CharField()
    Quote = serializers.CharField()
    Star = serializers.CharField()


# class UserSerializer(serializers.Serializer):
#     """
#     创建一个用户的序列器
#     """
#     username = serializers.CharField()
#     password = serializers.CharField()
#     # xxxxx = serializers.CharField(source="user_type")  # row.user_type  source将xxxx对应为user_type
#     # user_type_choince中的数字必须是int类型
#     type = serializers.CharField(source="get_user_type_display")  # row.get_user_type_display()
#     #
#     gp = serializers.CharField(source="group.title")
#     # 自定义显示 获取当前用户的所有role 信息
#     # 多对多情况
#     roles = serializers.SerializerMethodField()
#     # 默认get_字段名
#     def get_roles(self,row):
#          role_object_list = row.roles.all()
#          ret = []
#          for x in role_object_list:
#              ret.append({'id':x.id,"title":x.title})
#          return ret
class UserSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_user_type_display")
    roles = serializers.SerializerMethodField()
    group = serializers.CharField(source="group.title")
    # 完成一些基本的操作
    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ["id","username","password","type","roles","group"]
        # group 的显示信息 group_id 为当前表的字段 没有group.id方法
        # extra_kwargs = {"group":{"source":"group_id"},}

    def get_roles(self, row):
        role_object_list = row.roles.all()
        ret = []
        for x in role_object_list:
            ret.append({'id': x.id, "title": x.title})
        return ret