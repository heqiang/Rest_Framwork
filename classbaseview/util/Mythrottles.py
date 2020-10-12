from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
import time
from classbaseview.models import UserInfo

VISIT_RECOED = {}

class MyBaseThrottle(object):

        def  __init__(self):
            self.history = None
        def allow_request(self, request, view):
            remote_addr = request.META.get('REMOTE_ADDR')
            ctime = time.time()
            if remote_addr not in VISIT_RECOED:
                VISIT_RECOED[remote_addr] = [ctime,]
                print(VISIT_RECOED)
                return True

            history = VISIT_RECOED.get(remote_addr)
            self.history = history

            while history and history[-1]< ctime-12:
                history.pop()
                return True

        def wait(self):
            """
            还需要等待多时秒
            :return:
            """
            # 返回提示
            ctime = time.time()
            return 12 - (ctime-self.history[-1])


#继承SimpleRateThrottle 只需要重写 get_ident 方法
class  VisitThrottle(SimpleRateThrottle):
        scope =  "hq"
        def get_cache_key(self, request, view):
            # 返回一个唯一标识  HTTP_X_FORWARDED_FOR or REMOTE_ADDR
            return  self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
        scope =  "user"

        def get_cache_key(self, request, view):
            username = UserInfo.objects.filter(id = request.user)
            return username

