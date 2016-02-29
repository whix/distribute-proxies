# -*- coding: utf-8 -*-


class ConfigureUrl(object):
    def __init__(self):
        # the web pages display the format of proxy like 0.0.0.0:0000
        self.urls1 = ["http://code.76lt.com/daili/?dd=gaosu",
                      "http://code.76lt.com/daili/?dd=feiniming",
                      "http://code.76lt.com/daili/?dd=niming"]
        # the web pages display the format of proxy like 0.0.0.0+(some str)+0000
        self.urls2 = ['http://www.kuaidaili.com/free/%s/' % i for i in ['inha', 'intr', 'outha', 'outtr']] + \
            ['http://www.66ip.cn/areaindex_%d/1.html' % i for i in xrange(1, 35)] + \
            ['http://www.kxdaili.com/dailiip/%d/%d.html#ip' % (i, j) for i in xrange(1, 5) for j in xrange(1, 11)] + \
            ['http://www.swei360.com/free/?stype=%d&page=%d' % (i, j) for i in xrange(1, 5) for j in xrange(1, 3)] + \
            ['http://ip84.com/gn/%d' % j for j in xrange(1, 4)] + \
            ['http://ip84.com/pn/%d' % j for j in xrange(1, 7)] + \
            ['http://ip84.com/tm/%d' % j for j in xrange(1, 13)] + \
            ['http://www.nianshao.me/?stype=5&page=%d' % i for i in xrange(1,51)] + \
            ['http://www.xicidaili.com/%s/%d' % (i, j) for i in ['nn', 'nt', 'wt'] for j in xrange(1, 3)] + \
            ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218']