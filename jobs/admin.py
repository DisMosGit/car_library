from django.contrib import admin

# Register your models here.
from .models import JobList, JobOnCar

class JobListAdmin(admin.ModelAdmin):
    pass
admin.site.register(JobList, JobListAdmin)


class JobOnCarAdmin(admin.ModelAdmin):
    pass
admin.site.register(JobOnCar, JobOnCarAdmin)