from django.http import HttpResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin    # 1.10.x

class ForbiddenIpMiddleware(MiddlewareMixin):
    def process_view(self,request,view_func,*view_args,**view_kwargs):
        DISALLOWED_IPS = settings.DISALLOWED_IPS
        ALLOWED_IPS = settings.ALLOWED_IPS

        if 'HTTP_X_FORWARDED_FOR' in  request.META:
            ip =  request.META['HTTP_X_FORWARDED_FOR']
            print("HTTP_X_FORWARDED_FOR:", ip)
        else:
            ip = request.META['REMOTE_ADDR']
            print("REMOTE_ADDR:", ip)
        if ip in DISALLOWED_IPS or \
                '.'.join(ip.split('.')[:3])+'.0' in DISALLOWED_IPS or \
                '.'.join(ip.split('.')[:2])+'.0.0' in DISALLOWED_IPS:
            print("black list！")
            return HttpResponse('您的ip在黑名单中')
        elif "*" not in ALLOWED_IPS and \
                ip not in ALLOWED_IPS and \
                '.'.join(ip.split('.')[:3])+'.0' not in ALLOWED_IPS and \
                '.'.join(ip.split('.')[:2])+'.0.0' not in ALLOWED_IPS:
            print("white list!")
            return HttpResponse('您的ip不在白名单中！')