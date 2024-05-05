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
def create_tag(request):
    tag = Category(request.data.get('tag'))
    tag.save()
    return JsonResponse(status=204)

@api_view(['POST'])
def create_assignment(request):

    assignment = Assignment(
        title = request.data.get('title'),
        deadline = request.data.get('deadline'),
        part = request.data.get('part'),
        # tag_id = request.data.get('Category'),
        link = request.data.get('link'),
        content = request.data.get('content')
    )
    assignment.save()
    return JsonResponse({'message':'success'})


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
