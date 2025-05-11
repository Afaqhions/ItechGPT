from django.contrib import admin

# importing db from meassage-->app
from message.models import message

# creating a class to display table to admin pannel
class message_usr(admin.ModelAdmin):
    # displaying columns/attributes of table 
    # name should be sameto table column
    list_display = ('usr_name','usr_message') 

# Registering message model here.
admin.site.register(message,message_usr)