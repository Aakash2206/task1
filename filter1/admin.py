from django.contrib import admin
from .models import Data, Subcat, Subsubcat

# Register your models here.
admin.site.register(Data)
admin.site.register(Subcat)
admin.site.register(Subsubcat)

