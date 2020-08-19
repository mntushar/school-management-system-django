from django.contrib import admin
from teacher.models import TeacherInfo


#teacher information display
class TeacherInfoShow(admin.ModelAdmin):
    list_display = ('name', 'designation')


admin.site.register(TeacherInfo, TeacherInfoShow) #teacher information register



