from django.db import models


#student information table
class StudentInfo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    father = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


#student shift table
class StudentShiftInfo(models.Model):
    shiftname = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return self.shiftname


#student class information table
class StudentClassInfo(models.Model):
    classname = models.CharField(max_length=10, blank=True, null=True)
    classshortname = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.classname


#student detail information
class StudentDetailInfo(models.Model):
    roll = models.IntegerField()
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    shiftid = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    class_id = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    section = models.CharField(max_length=5, blank=True, null=True)
    class Meta:
        unique_together = ['roll', 'class_id']


    def __str__(self):
        return str(self.roll)


# student attendance table
class StudentAttendance(models.Model):
    student_id = models.ForeignKey(
        StudentDetailInfo,
        on_delete=models.CASCADE,  
    )
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)
    class Meta:
        unique_together = ['student_id', 'date']


    def __str__(self):
        return str(self.student_id.roll)


#student result
class StudentResult(models.Model):
    roll = models.IntegerField()
    board = models.CharField(max_length=15, blank=True, null=True)
    gpa = models.IntegerField()


    def __str__(self):
        return str(self.roll)










    








