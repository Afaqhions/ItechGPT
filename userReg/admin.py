from django.contrib import admin
# Importing use reg model
from userReg.models import usrReg
# Register your models here.
class user_reg(admin.ModelAdmin):
    list_display = ('first_name','last_name','user_name','email','password')

# Making admin access-->(Model_name,model_reg_name)
admin.site.register(usrReg,user_reg)