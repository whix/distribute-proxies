# -*- coding: utf-8 -*-
from distribute_proxies.wsgi import *
import requests
import re
import thread
from datetime import datetime
from proxies.models import Proxies, Domain
import httplib
import sys
from configureUrl import ConfigureUrl

# sys.stdout = open('error_log.txt', 'a')


class ManageProxies(ConfigureUrl):
    def __init__(self):
        super(ManageProxies, self).__init__()
        self.test_url = 'http://wcf.beyebe.com/Common/ProxyTest.ashx'
        # the web pages display the format of proxy like 0.0.0.0:0000
        # self.urls1 = ["http://code.76lt.com/daili/?dd=gaosu",
        #               "http://code.76lt.com/daili/?dd=feiniming",
        #               "http://code.76lt.com/daili/?dd=niming"]
        self.reg1 = re.compile(r'(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}')
        # the web pages display the format of proxy like 0.0.0.0+(some str)+0000
        # self.urls2 = ['http://www.kuaidaili.com/free/%s/' % i for i in ['inha', 'intr', 'outha', 'outtr']] + \
        #     ['http://www.66ip.cn/areaindex_%d/1.html' % i for i in xrange(1, 35)] + \
        #     ['http://www.kxdaili.com/dailiip/%d/%d.html#ip' % (i, j) for i in xrange(1, 5) for j in xrange(1, 11)] + \
        #     ['http://www.swei360.com/free/?stype=%d&page=%d' % (i, j) for i in xrange(1, 5) for j in xrange(1, 3)] + \
        #     ['http://ip84.com/gn/%d' % j for j in xrange(1, 4)] + \
        #     ['http://ip84.com/pn/%d' % j for j in xrange(1, 7)] + \
        #     ['http://ip84.com/tm/%d' % j for j in xrange(1, 13)] + \
        #     ['http://www.nianshao.me/?stype=5&page=%d' % i for i in xrange(1,51)] + \
        #     ['http://www.xicidaili.com/%s/%d' % (i, j) for i in ['nn', 'nt', 'wt'] for j in xrange(1, 3)] + \
        #     ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218']
        self.reg2 = re.compile(r'((?:\d{1,3}\.){3}\d{1,3})\D*?(\d{1,5})')
        self.http_reg = re.compile(r'http://(.*?)/')
        # store the proxies fetched in urls
        self.proxies_fetched = []
        # the split the proxies_fetched list
        self.proxies_split = []
        # the dict each proxy is mapping the source of url
        self.proxy_url = {}

    def get_domain_name(self, url):
        domain_name = re.findall(self.http_reg, url)[0]
        return domain_name

    def split_proxies_fetched(self):
        for i in xrange(0, len(self.proxies_fetched), 1000):
            self.proxies_split.append(self.proxies_fetched[i:i+1000])

    def set_related_domain(self, proxy_object):
        if proxy_object.related_domain is None:
            domain_field = self.get_domain_name(proxy_object.website)
            d = Domain.objects.get_or_create(domain=domain_field, defaults={'quantity': 0})
            proxy_object.related_domain = d[0]
            proxy_object.save()
            d[0].quantity += 1
            d[0].save()

    def update_domain_quantity(self):
        domain_queryset = Domain.objects.all()
        for domain in domain_queryset:
            domain.quantity = Proxies.objects.filter(related_domain=domain).count()
            domain.save()

    # update the proxies in database to make sure it still works
    def update_db(self):
        print 'updating the proxies in database...'
        sys.stdout.flush()
        proxies_list = Proxies.objects.all()
        for proxies_object in proxies_list:
            try:
                res = requests.post(url=self.test_url, data={'key': 'ok'}, auth=requests.auth.HTTPBasicAuth('user',
                                    'pass'), proxies={"http": "http://" + proxies_object.proxy}, timeout=5)
                if res.status_code != 200 or res.content != 'ok':
                    if proxies_object.related_domain is not None and proxies_object.related_domain.quantity > 0:
                        proxies_object.related_domain.quantity -= 1
                        proxies_object.related_domain.save()
                    proxies_object.delete()
                else:
                    proxies_object.add_date = datetime.now()
                    proxies_object.save()
                    if proxies_object.related_domain is None:
                        self.set_related_domain(proxies_object)
            except (IOError, httplib.IncompleteRead):
                if proxies_object.related_domain is not None and proxies_object.related_domain.quantity > 0:
                    proxies_object.related_domain.quantity -= 1
                    proxies_object.related_domain.save()
                proxies_object.delete()
        print 'finished updating...'
        sys.stdout.flush()

    # get the proxies from the website of providing proxy
    def get_page_proxies(self):
        self.proxies_fetched = []       # clean the old data
        self.proxies_split = []
        self.proxy_url = {}
        for url1 in self.urls1:
            try:
                headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
                html1 = requests.get(url=url1, headers=headers, auth=requests.auth.HTTPBasicAuth('user', 'pass'), timeout=15).content # add auth and timeout
                items1 = re.findall(self.reg1, html1)
                for i in items1:
                    self.proxy_url[i] = url1
                    self.proxies_fetched.append(i)
            except (IOError, httplib.IncompleteRead),e:
                print 'Exception Error:', e
                continue
        for url2 in self.urls2:
            try:
                headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
                html2 = requests.get(url=url2, headers=headers, auth=requests.auth.HTTPBasicAuth('user', 'pass'), timeout=15).content
                items = re.findall(self.reg2, html2)
                for item in items:
                    item_temp = item[0] + ':' + item[1]
                    self.proxy_url[item_temp] = url2
                    self.proxies_fetched.append(item_temp)
            except (IOError, httplib.IncompleteRead),e:
                print 'Exception Error:', e
                continue

    # choose the proxies is useful and save
    def filter_proxies(self, proxy_lis):
        for proxy in proxy_lis:
            try:
                res = requests.post(url=self.test_url, data={'key': 'ok'}, proxies={"http": "http://" + proxy},
                                    auth=requests.auth.HTTPBasicAuth('user', 'pass'), timeout=5)
                if res.status_code == 200 and res.content == 'ok':
                    # only show the domain if the url is too long
                    if len(self.proxy_url[proxy]) > 100:
                        self.proxy_url[proxy] = 'http://' + self.get_domain_name(self.proxy_url[proxy])
                    # get_or_create 返回一个元组，包含一个对象(get/create)和一个布尔值，get为False，create为True
                    p = Proxies.objects.get_or_create(proxy=proxy, defaults={'website': self.proxy_url[proxy]})
                    p[0].add_date = datetime.now()
                    p[0].save()
                    self.set_related_domain(p[0])
            except (IOError, httplib.IncompleteRead):
                continue

    # setting the frequency for each function
    def start_working_helper(self):
        while True:
            try:
                print '[time:%s]loop begin' % datetime.now()
                sys.stdout.flush()
                self.get_page_proxies()
                print '[time:%s] len:%s' % (datetime.now(), len(self.proxies_fetched))
                sys.stdout.flush()
                self.split_proxies_fetched()
                print '[time:%s] len:%s' % (datetime.now(), len(self.proxies_split))
                sys.stdout.flush()
                for lis in self.proxies_split:
                    beg = datetime.now()
                    self.filter_proxies(lis)
                    print "[time:%s] filter_proxies function cost %s." % (datetime.now(), datetime.now() - beg)
                    sys.stdout.flush()
                    beg = datetime.now()
                    self.update_db()
                    print "[time:%s] update_db function cost %s." % (datetime.now(),datetime.now() - beg)
                    sys.stdout.flush()
                print '[time:%s] ready to execute update_domain_quantity function' % datetime.now()
                sys.stdout.flush()
                self.update_domain_quantity()
            except Exception, e:
                print "[time:%s] Exception:%s" % (datetime.now(), e)
                sys.stdout.flush()
                continue

    # start a new tread
    def start_working(self):
        thread.start_new_thread(self.start_working_helper, ())


manage_proxies = ManageProxies()
manage_proxies.start_working_helper()

