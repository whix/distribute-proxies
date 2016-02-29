from django.contrib import admin
from proxies.models import Proxies, Domain


# Register your models here.
class ProxiesAdmin(admin.ModelAdmin):
    list_display = ('proxy', 'website', 'add_date', 'related_domain')
    ordering = ('-add_date',)
    list_filter = ('add_date',)
    search_fields = ('proxy', 'website')


class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'quantity', 'add_date')
    ordering = ('-quantity',)

admin.site.register(Domain, DomainAdmin)
admin.site.register(Proxies, ProxiesAdmin)
