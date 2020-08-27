from rest_framework import serializers
from classbaseview.models import Movie,UserInfo


class MovieSerializer(serializers.ModelSerializer):
    """
    创建一个序列器
    """
    Name = serializers.CharField()
    Url = serializers.CharField()
    Quote = serializers.CharField()
    Star = serializers.CharField()


class  UserSerializer(serializers.ModelSerializer):
    """
    创建一个用户的序列器
    """
    username = serializers.CharField()
    user_type = serializers.CharField()

    class Meta:
        model = UserInfo
        fields = ("username","user_type","password")