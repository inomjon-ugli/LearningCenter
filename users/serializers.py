from rest_framework import serializers
from .models import CustomUser,Profil



class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'phone',
            'password',
            'password2',
        )
    
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwordlar ikki xil kiririlgan")
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            phone = validated_data['phone'],
            password = validated_data['password'],
        )
        return user

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = (
            'id',
            'user',
            'bio',
            'avatar',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=(
            'id',
            'username',
            'first_name',
            'last_name',
            'full_name',
            'email',
            'phone',
            'role',
            'student_group',
            'is_active',

        )
    