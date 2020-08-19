from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import*
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from student.models import*


#multipul student create
class MulStudentDetail(APIView):
    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success'}, status=status.HTTP_201_CREATED)
        return Response({'status':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#single student create
class CreateStudentDetail(APIView):
    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success'}, status=status.HTTP_201_CREATED)
        return Response({'status':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#student view
class StudentView(APIView):
    #token authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student = StudentInfo.objects.all()
        student_data = StudentInfoSerializer(student, many=True)
        return Response({'status':student_data.data}, status=status.HTTP_201_CREATED)


#single student view
class ViewStudent(APIView):
    def get(self, request, pk):
        student = StudentInfo.objects.get(id=pk)
        student_data = StudentInfoSerializer(student)
        return Response({'status':student_data.data}, status=status.HTTP_201_CREATED)


#student attendance api function base
@api_view(['Get'])
def std_attendance(request, std_class, std_roll):
    try:
        std_obj = StudentDetailInfo.objects.get(
            roll=int(std_roll),
            class_id__classname=std_class
        )
        att_obj = StudentAttendance.objects.create(
            student_id=std_obj,
            status=1
        )
        return Response({'status':'success'}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({'status':'failed'}, status=status.HTTP_400_BAD_REQUEST)


#student attendance api class base
class std_att_class(APIView):
    def get(self, request, std_class, std_roll):
        try:
            std_obj = StudentDetailInfo.objects.get(
                roll=int(std_roll),
                class_id__classname=std_class
            )
            att_obj = StudentAttendance.objects.create(
                student_id=std_obj,
                status=1
            )
            return Response({'status':'success'}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({'status':'failed'}, status=status.HTTP_400_BAD_REQUEST)


#student result apt
#@api_view(['POST'])
class result_student(APIView):
    #basic authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = ResultSerializer(data=request.data)
            if serializer.is_valid():
                board = serializer.validated_data["board"]
                roll = serializer.validated_data["roll"]
                result = StudentResult.objects.get(roll=roll, board=board)
                return Response({'Result':result.gpa}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err)

