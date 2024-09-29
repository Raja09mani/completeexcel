from django.contrib import admin
from .models import StudentDetail, StudentMark

class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ('sid', 'sno', 'sname', 'sclass', 'saddress')
    search_fields = ('sname', 'sclass')

class StudentMarkAdmin(admin.ModelAdmin):
    list_display = ('roll', 'tamil', 'english', 'maths', 'science', 'socialscience')
    
from .models import StudDetail

class StudDetailAdmin(admin.ModelAdmin):
    list_display = ('sid', 'roll', 'sname', 'sclass', 'saddress','tamil', 'english', 'maths', 'science', 'socialscience')
    search_fields = ('sname', 'sclass')


admin.site.register(StudDetail, StudDetailAdmin)
admin.site.register(StudentDetail, StudentDetailAdmin)
admin.site.register(StudentMark, StudentMarkAdmin)
