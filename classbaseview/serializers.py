from abc import ABC

from rest_framework.exceptions import ValidationError

from classbaseview import models
from rest_framework import serializers
from classbaseview.models import UserInfo


class MyFiled(serializers.CharField):

    def to_representation(self, value):
        """
        :param value:数据库对应字段的的数据
        :return:
        """
        return value
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
#
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

# 定制自己的字段类 实现数据的定制化操作 但是不常用

# class UserSerializer(serializers.ModelSerializer):
#     type = serializers.CharField(source="get_user_type_display")
#     roles = serializers.SerializerMethodField()
#     # view_name 反向生成 url中的name
#     group_ = serializers.HyperlinkedIdentityField(view_name="gp")
#     user_name = MyFiled(source="username")
#     # 完成一些基本的操作
#     class Meta:
#         model = models.UserInfo
#         # fields = "__all__"
#         fields = ["id","user_name","password","type","roles","group_"]
#         # group 的显示信息 group_id 为当前表的字段 没有group.id方法
#         # extra_kwargs = {"group":{"source":"group_id"},}
#
#     def get_roles(self, row):
#         role_object_list = row.roles.all()
#         ret = []
#         for x in role_object_list:
#             print(x)
#             ret.append({'id': x.id, "title": x.title})
#         return ret

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = ["id","username","password","user_type","roles","group"]
        depth = 1


class UserGroupSerlizer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGroup
        fields ="__all__"

class xxxvalidator(object):
    def __init__(self,base):
        self.base=base
    def __call__(self, value):
        if not value.startswith(self.base):
            message = "This field must be  start with %s"% self.base
            raise ValidationError(message)

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass
class GroupSerlizers(serializers.Serializer):
    title = serializers.CharField(error_messages={"required":"标题不能为空"},validators=[xxxvalidator("h"),])