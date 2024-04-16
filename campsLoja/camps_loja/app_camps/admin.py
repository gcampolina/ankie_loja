from django.contrib import admin
from .models import Produto
from django.conf import settings
from django.contrib.admin.models import LogEntry
from .models import CustomUser
from django.contrib.admin import AdminSite


admin.site.register(Produto)

admin.site.register(CustomUser)