from django.urls import path, re_path
from classbaseview import views
from django.conf.urls  import url

urlpatterns = [
        #
        url(r'^(?P<versions>[v1|v2]+)/users/$',views.UserView.as_view(),name="User"),
        url(r'^(?P<versions>[v1|v2]+)/userinfo/$',views.UserinfoView.as_view(),name="userinfo")
]


