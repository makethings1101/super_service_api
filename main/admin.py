# coding:utf-8

from django.contrib import admin

from main.models import CustomerProfile, Maintainer, Order


admin.site.register(CustomerProfile)
admin.site.register(Maintainer)
admin.site.register(Order)
