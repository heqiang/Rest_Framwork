from rest_framework import  serializers
from classbaseview import  models


class PagerSerizers(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"