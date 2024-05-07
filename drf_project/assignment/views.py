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
    
    #api 6 특정 과제 삭제
    def delete(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        assignment.delete()
        return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)

#api 5 특정 과제 수정
@api_view(['PUT', 'PATCH']) 
#전체와 부분 업데이트 사용자가 선택
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'PUT':
        serializer = AssignmentSerializer(assignment, data=request.data) #전체 업데이트
    elif request.method == 'PATCH':
        serializer = AssignmentSerializer(assignment, data=request.data, partial=True) #일부 업데이트

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "success"})
    return JsonResponse(serializer.errors, status=400)

#api 7 파트별 조회
@api_view(['GET'])
def get_part(request, part):
    part_set = ['ALL', 'BE', 'FE']
    if part not in part_set:
        data = {'message':'존재하지 않는 파트입니다. [ALL|BE|FE] 중에 입력해주세요.'}
        return Response(data,status=404)
    
    assignments = Assignment.objects.filter(part=part)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

#api 8 태그별 조회
@api_view(['GET'])
def get_tag(request,tag):
    try:
        category = Category.objects.get(name=tag)
    
    except Category.DoesNotExist:
        # 카테고리가 존재하지 않을 경우 현재 모든 카테고리 제시
        tags = Category.objects.all()
        tag_list = [{'name': tag.name} for tag in tags] 
        data = {'message': '존재하지 않는 카테고리 입니다.', 'tag_list': tag_list}
        return Response(data, status=404)
    
    assignments = Assignment.objects.filter(tag=category)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)
    