from django.contrib import admin
from myapp.models import Resume
# Register your models here.


@admin.register(Resume)
class Resumeadmin(admin.ModelAdmin):
    list_display=['id','name','dob','gender','locality','city','job_city','pin','email','mobile','state','profile_image','file']