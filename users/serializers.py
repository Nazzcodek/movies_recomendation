from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer class for the User model.

    Attributes:
        profile_picture_url (serializers.SerializerMethodField): A serializer method field for the profile picture URL.
    
    Methods:
        create(validated_data): Creates a user object with the provided validated data.
        get_profile_picture_url(obj): Returns the URL of the profile picture for the given object.
    """
    profile_picture_url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'profile_picture', 'profile_picture_url']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'is_active', 'is_staff', 'is_superuser']

    def create(self, validated_data):
        """
        Creates a user object with the provided validated data.

        Parameters:
            validated_data (dict): A dictionary containing the validated data for creating a user.
        
        Returns:
            User: The newly created user object.
        """
        # Ensure the password is hashed before saving
        user = User.objects.create_user(**validated_data)
        return user
 
    def get_profile_picture_url(self, obj):
        """
        Return the URL of the profile picture for the given object.

        Parameters:
            obj (object): The object for which to retrieve the profile picture URL.

        Returns:
            str or None: The URL of the profile picture if it exists, else None.
        """
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None
