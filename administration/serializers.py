from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Role

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract the role data from validated data if passed in the request
        role_data = validated_data.pop('role', None)
        
        if role_data:
            # If a role is passed, use it
            role = Role.objects.get(name=role_data['name'])
        else:
            # If no role is passed, assign the "admin" role by default
            role = Role.objects.get_or_create(name='admin')  # Or whatever your default role is
        
        # Create the user with the validated data (excluding the role)
        user = User.objects.create_user(**validated_data)
        
        # Assign the role to the newly created user
        user.role = role
        user.save()
        
        return user