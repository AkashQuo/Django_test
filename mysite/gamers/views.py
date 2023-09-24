from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse

from .models import GAMER_USER
from .serializers import GamerUserSerializer


@api_view()
def get_user(request):
    gamer_obj = GAMER_USER.objects.all()
    gamer_json = GamerUserSerializer(gamer_obj, many=True)
    return Response({
        'status': 200,
        'message': gamer_json
    })


@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
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


class MyView(APIView):
    def get(self, request):
        # Logic for handling GET request
        return HttpResponse('This is a GET request')

    def post(self, request):
        # Logic for handling POST request
        return HttpResponse('This is a POST request')

    def put(self, request):
        # Logic for handling PUT request
        return HttpResponse('This is a PUT request')

    def delete(self, request):
        # Logic for handling DELETE request
        return HttpResponse('This is a DELETE request')

# def my_function_based_view(request):
#     context = {'name': 'John Doe'}
#     return render(request, 'my_template.html', context)
