from django.contrib import admin
from .models import files,Recommend,Results,History,Contact
# Register your models here.

admin.site.register(files)
admin.site.register(Recommend)
admin.site.register(Results)
admin.site.register(History)
admin.site.register(Contact)