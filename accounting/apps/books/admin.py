from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


class PaymentInline(GenericTabularInline):
    model = models.Payment
    extra = 1


class InvoiceLineInline(admin.TabularInline):
    model = models.InvoiceLine
    extra = 1


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = (
        InvoiceLineInline,
        PaymentInline,
    )
    readonly = (
        'total_incl_tax', 'total_excl_tax',
    )


class BillLineInline(admin.TabularInline):
    model = models.BillLine
    extra = 1


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    inlines = (
        BillLineInline,
        PaymentInline,
    )
    readonly = (
        'total_incl_tax', 'total_excl_tax',
    )


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
