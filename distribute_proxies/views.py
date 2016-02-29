from django.http import HttpResponse
from proxies.models import Proxies
import datetime
from django.shortcuts import render_to_response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from hawkrest import HawkAuthentication
from rest_framework.generics import ListAPIView
from proxies.serializer import ProxiesSerializer

print 'views.py'
def homepage(request):
    return HttpResponse('Welcome to this site!!!')


def get_proxy(request):
    p = Proxies.objects.all()[0]    #using class Meta order by "-add_date"
    p.add_date = datetime.datetime.now() - datetime.timedelta(days=1)
    p.save()
    return HttpResponse(p)


def proxy_info(request):
    time_point = datetime.datetime.now() - datetime.timedelta(minutes=10)
    ten_min = Proxies.objects.filter(add_date__gt=time_point).count()
    time_point = datetime.datetime.now() - datetime.timedelta(hours=1)
    one_hour = Proxies.objects.filter(add_date__gt=time_point).count()
    time_point = datetime.datetime.now() - datetime.timedelta(hours=2)
    two_hour = Proxies.objects.filter(add_date__gt=time_point).count()
    time_point = datetime.datetime.now() - datetime.timedelta(hours=12)
    twe_hour = Proxies.objects.filter(add_date__gt=time_point).count()
    all_objects = Proxies.objects.all().count()
    return render_to_response('proxy_info.html', locals())


# class GetProxy(APIView):
#     authentication_classes = (HawkAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, format=None):
#         p = Proxies.objects.all()[0]    #using class Meta order by "-add_date"
#         p.add_date = datetime.datetime.now() - datetime.timedelta(days=1)
#         p.save()
#         return HttpResponse(p)

class HawkTest(APIView):
    authentication_classes = (HawkAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        if request.body == 'ok':
            return HttpResponse('ok')
        else:
            return HttpResponse('the content is wrong!')
