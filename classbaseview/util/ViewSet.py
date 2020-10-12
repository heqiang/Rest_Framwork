from rest_framework import  serializers
from classbaseview.models import UserInfo

class  MyModelViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
        depth = 0