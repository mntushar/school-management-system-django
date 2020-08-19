from django.contrib import admin
from student.models import*


#student information display
class StudentInfoShow(admin.ModelAdmin):
    list_display = ['name', 'father']


#student detail information display
class StudentDetailInfoShow(admin.ModelAdmin):
    list_display = ['roll', 'class_id', 'shiftid', 'section']


#student shift information display
class StudentShiftInfoShow(admin.ModelAdmin):
    list_display = ['shiftname']


#student class information display
class StudentClassInfoShow(admin.ModelAdmin):
    list_display = ['classname', 'classshortname']


#student attendance display
class StudentAttendanceShow(admin.ModelAdmin):
    list_display = ['student_id', 'status']


admin.site.register(StudentInfo, StudentInfoShow) #student information register
admin.site.register(StudentDetailInfo, StudentDetailInfoShow) #student detail information register
admin.site.register(StudentClassInfo, StudentClassInfoShow) #student class information register 
admin.site.register(StudentShiftInfo, StudentShiftInfoShow) #student shift information register
admin.site.register(StudentAttendance, StudentAttendanceShow) #student attendance register


