from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    """
    View to create a new user.

    Methods:
    --------
    create(self, request, *args, **kwargs):
        Create a new user.

        Args:
            request: The request object containing user data.
            args: Additional positional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object with the status and headers.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'User created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
    

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    """
    API endpoint for user login. Returns a token upon successful authentication.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # User is authenticated, generate and return a token
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        # Authentication failed
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ModifyUserView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update and delete a user instance.

    Attributes:
        serializer_class (Serializer): The serializer class used for serializing and deserializing user data.
        permission_classes (list): The list of permission classes that the user must have to access this view.
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieve the user instance associated with the current request.

        Returns:
            object: The user instance associated with the current request.
        """
        return self.request.user

    def perform_update(self, serializer):
        """
        Perform an update operation on the user.

        Args:
            serializer (Serializer): The serializer object used to validate and update the user data.

        Returns:
            Response: A Response object with a status message indicating the success of the update operation.
        """
        password = serializer.validated_data.get('password', None)
        if password:
            serializer.instance.password = make_password(password)
        else:
            serializer.validated_data['password'] = self.request.user.password

        serializer.save()
        return Response({'status': 'User updated successfully'}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        """
        Deletes the given instance and returns a response with the status of the deletion.

        Parameters:
            instance (object): The instance to be deleted.

        Returns:
            Response: A response object with the status of the deletion.
        """
        instance.delete()
        return Response({'status': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.all()
