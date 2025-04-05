from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'branch', 'year', 'email', 'contact_number') 
    list_filter = ('branch', 'year')  
    search_fields = ('name', 'roll_number', 'email', 'contact_number') 

admin.site.register(Student,StudentAdmin)