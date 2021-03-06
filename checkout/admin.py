# pylint: disable=missing-module-docstring
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Show Line Item in admin view"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Show Order in Admin view"""
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total','original_bag',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total','original_bag',
              'stripe_pid', 'order_status', 'delivery_date',
              'order_comments')

    list_display = ('order_number', 'order_status', 'date', 'full_name',
                    'order_total', 'delivery_date',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
