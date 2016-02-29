from django.db import models
from datetime import datetime

class Domain(models.Model):
    domain = models.CharField(max_length=100)
    quantity = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.domain


class Proxies(models.Model):
    proxy = models.CharField(max_length=30)
    add_date = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=100, default='no website')
    related_domain = models.ForeignKey(Domain, null=True)
    # is_used = models.BooleanField(default=False)      # todo

    def __unicode__(self):
        return self.proxy

    class Meta:
        ordering = ['-add_date']


