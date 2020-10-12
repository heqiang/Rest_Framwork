from rest_framework import  serializers
from classbaseview import  models


class PagerRoleSerizers(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"


class PagerUserSerizers(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = "__all__"