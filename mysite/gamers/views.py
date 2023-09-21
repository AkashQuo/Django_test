from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.views.generic import ListView

from .models import GAMER_USER


@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'message': 'Yes! Django rest framework is working!!',
            'method_called': 'You called GET method'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'Yes! Django rest framework is working!!',
            'method_called': 'You called POST method'
        })
    else:
        return Response({
            'status': 400,
            'message': 'Yes! Django rest framework is working!!',
            'method_called': 'You called INVALID method'
        })