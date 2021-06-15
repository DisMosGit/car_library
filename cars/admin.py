from django.contrib import admin

# Register your models here.
from .models import CarBrand, CarModel, CarModification, CarSpecifications, PersonalCar


class CarBrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarBrand, CarBrandAdmin)


class CarModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarModel, CarModelAdmin)


class CarModificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarModification, CarModificationAdmin)


class CarSpecificationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarSpecifications, CarSpecificationsAdmin)


class PersonalCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(PersonalCar, PersonalCarAdmin)