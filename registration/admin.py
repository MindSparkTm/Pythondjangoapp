from django.contrib import admin
from .models import Registration


# Register your models here.




class Gyminfo(admin.ModelAdmin):
    list_display = ["id", "created", "last_updated", "gymname","country","state","zipcode", "email", "phonenumber", "location",
                    "zipcode", "contactperson", "blog", "website", "facebook", "instagram", "paybill",
                    "paymentcontactnumber"]


admin.site.register(Registration, Gyminfo)


