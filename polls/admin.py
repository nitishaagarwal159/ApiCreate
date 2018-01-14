from django.contrib import admin
from . models import employees,uploadem,uploadphone,receiverequest,Posts,Likes,Shares

# Register your models here.
admin.site.register(employees)
admin.site.register(uploadem)
admin.site.register(uploadphone)
admin.site.register(receiverequest)
admin.site.register(Posts)
admin.site.register(Likes)
admin.site.register(Shares)