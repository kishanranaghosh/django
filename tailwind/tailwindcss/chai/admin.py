from django.contrib import admin
from .models import *

# Register your models here.
class ChaiRewviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'date_added')
    inlines = [ChaiRewviewInline]

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'user', 'quantity', 'date_added')

admin.site.register(ChaiVarity, )
admin.site.register(ChaiReview, )
admin.site.register(ChaiOrder)
admin.site.register(ChaiCart, )