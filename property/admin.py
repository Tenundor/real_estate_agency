from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.StackedInline):
    model = Owner.owned_flats.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]


class CompliantAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owned_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, CompliantAdmin)
admin.site.register(Owner, OwnerAdmin)
