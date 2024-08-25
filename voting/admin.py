from django.contrib import admin
from.models import Question,Choice,Registration

# Register your models here.

@admin.register(Question)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['question_text','pub_date']

@admin.register(Choice)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['question','choice_text','votes']

@admin.register(Registration)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['Full_Name','Email_address','Phone_number','Gender','Street_address','state','City','Age','state','dob']