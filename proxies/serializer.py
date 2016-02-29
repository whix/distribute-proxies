from rest_framework import serializers
from proxies.models import Proxies


class ProxiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proxies
        fields = ('proxy',)