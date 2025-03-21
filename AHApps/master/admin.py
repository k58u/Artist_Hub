from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = 'ARTIST HUB'                    
admin.site.index_title = 'Artist dashboard'                 
admin.site.site_title = 'ARTIST HUB ADMIN PANEL' 