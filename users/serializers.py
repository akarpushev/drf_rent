from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


    def create(self, validated_data):  # нужен для хэширования пароля
        user = User.objects.create_user(**validated_data)  # create_user хэширует
        # user = User.objects.create(
        #     email=validated_data['email'],
        #     username=validated_data['username'],
        # )
        # user.set_password(validated_data['password'])
        # user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    #email = serializers.EmailField()



