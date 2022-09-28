from django.contrib import admin

# Register your models here.
from .models import UserData 
from .models import incharge , club

admin.site.register(UserData)
admin.site.register(incharge)
admin.site.register(club)
