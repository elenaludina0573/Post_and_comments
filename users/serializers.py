from rest_framework import serializers

from users.models import User
from users.validators import EmailValidator, PasswordValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        validators = [PasswordValidator(field='password'), EmailValidator(field='email',)]
