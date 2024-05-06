#from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *

#api1 과제 생성
@api_view(['POST'])
def create_assignment(request):
    serializer = AssignmentPostSerializer(data=request.data)
    if serializer.is_valid(): # Serializer의 Meta 필드에 맞게 입력 받았는지 확인하는 조건문
        tag_name = serializer.validated_data.get('tag')
        if tag_name:
            tag, _ = Category.objects.get_or_create(name=tag_name)
            serializer.validated_data['tag'] = tag
        serializer.save()
        return JsonResponse({"message":"success"})
    
    return JsonResponse({"message":"fail"}, status=400)

#api 2 과제 제출물 생성
@api_view(['POST'])
def create_submission(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    # 해당 과제가 없으면 에러 404 처리

    submission = Submission(
        content = request.data.get('content'),
        link = request.data.get('link')
    )
    submission.save()
    return JsonResponse({'message':'success'})


#api 3 과제 목록 조회
class AssignmentListAPIView(APIView):
    def get(self, request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True) #퀘리셋이 많은 인자를 가짐
        return Response(serializer.data)

#api 4 특정 과제 조회
class AssignmentAPIView(APIView): 
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

#api 5 특정 과제 수정
@api_view(['PUT', 'PATCH']) 
#전체와 부분 업데이트 사용자가 선택
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'PUT':
        serializer = AssignmentPostSerializer(assignment, data=request.data) #전체 업데이트
    elif request.method == 'PATCH':
        serializer = AssignmentPostSerializer(assignment, data=request.data, patrial=True) #일부 업데이트
    
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "success"})
    return JsonResponse(serializer.errors, status=400)

#api 6 특정 과제 삭제
@api_view(['DELETE'])
def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.delete()
    return JsonResponse({"message": "deleted"})


