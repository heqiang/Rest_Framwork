from django.urls import path, re_path,include
from classbaseview import views
from django.conf.urls  import url
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r"MyUserModelViewSet",views.MyUserModelViewSet)


urlpatterns = [
        # url(r'^(?P<versions>[v1|v2]+)/users/$', views.UserView.as_view(),name="User"),
        # url(r'^(?P<versions>[v1|v2]+)/userinfo/$', views.UserInfoView.as_view(),name="userinfo"),
        # url(r'^(?P<versions>[v1|v2]+)/group/(?P<pk>\d+)$', views.GroupView.as_view(),name='ttt'),
        # url(r'group/$',views.Group.as_view()),
        # url(r'pager1/$',views.PagerView.as_view()),
        # url(r'MyGenericView/$',views.MyGenericView.as_view({"get":"get"})),
        # url(r'MyModelViewSet/$',views.MyModelViewSet.as_view({'get': 'list',
        #                                                       "post":"create",
        #                                                       "put":"update",
        #                                                       "patch":"perform_update",
        #                                                       "delete":"destroy"})),
        url(r'^(?P<versions>[v1|v2]+)/',include(router.urls))
]


