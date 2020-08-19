from rest_framework import serializers
from student.models import*


#student info serializer
class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'


#student result serializer
class ResultSerializer(serializers.Serializer):
    board = serializers.CharField(max_length=15)
    roll = serializers.IntegerField()
