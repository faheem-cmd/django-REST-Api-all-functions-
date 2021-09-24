from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import news
from .models import workers
from .models import CartItem
from .models import Cars

admin.site.register(news)
admin.site.register(workers)
admin.site.register(CartItem)
admin.site.register(Cars)