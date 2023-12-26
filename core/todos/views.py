from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework import status

from .models import Todo

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


class TodoDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk: int) -> Todo:
        try:
            todo = Todo.objects.get(pk=pk)
            self.check_object_permissions(self.request, todo)
            return todo
        except Todo.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request: Request, pk: int) -> Response:
        task = self.get_object(pk)
        serializer = TodoSerializer(task)

        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        task = self.get_object(pk)
        
        data = request.data
        data['user'] = request.user.id

        serializer = TodoSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request: Request, pk: int) -> Response:
        task = self.get_object(pk)
        serializer = TodoSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        task = self.get_object(pk)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
