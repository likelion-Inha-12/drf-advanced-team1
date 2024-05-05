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
