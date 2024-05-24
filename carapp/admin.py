from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'number_of_cylinders', 'number_of_passengers', 'car_color', 'cylinder_volume', 'owner_name')
    list_filter = ('car_color', 'owner_name')
    search_fields = ('car_name', 'owner_name')

    fieldsets = (
        (None, {
            'fields': ('car_name', 'number_of_cylinders', 'number_of_passengers', 'car_color', 'cylinder_volume', 'owner_name')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            owner_name = form.cleaned_data.get('owner_name')
            obj.owner_name = owner_name
        super().save_model(request, obj, form, change)
