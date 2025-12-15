# REST framework
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend



@api_view(['GET'])
def test(request):
    return Response({'0-0': 'yurp'}, status=status.HTTP_200_OK)
