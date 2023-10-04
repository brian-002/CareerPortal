from django.contrib import admin

from .models import UserProfile, JobApplication, PortalPhotos

admin.site.register(UserProfile)
admin.site.register(JobApplication)
admin.site.register(PortalPhotos)