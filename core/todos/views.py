from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import TodoSerializer


class TodoCreateView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        todos = request.user.todos.all()

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
        
    
    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

