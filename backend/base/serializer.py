from rest_framework import serializers

# from django.contrib.auth.models import User  # AbstractUser Olabilir
from django.contrib.auth import get_user_model  # 1
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product

#dfdfgfhgfdjgfhj rhydghjhfk
# PLEASE_NOTE_THIS PART !!!!!!!!!
# in order to create UserSerializer i used model = get_user_model() by importing 1 from the imports
# when i used model = User i got an error in the server
#'NoneType' object has no attribute '_meta' error to be exact
class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isFarmer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "_id", "username", "email", "name", "isAdmin", "isFarmer"]

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_isFarmer(self, obj):
        return obj.isFarmer

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "_id",
            "username",
            "email",
            "name",
            "isAdmin",
            "isFarmer",
            "token",
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
