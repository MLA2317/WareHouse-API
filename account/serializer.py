from rest_framework import serializers
from .models import Account, MyProduct
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from product.serializer import ProductPOSTSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=25, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=25, write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'bio', 'avatar', 'gender', 'role', 'password', 'password2', 'created_date', 'modified_date')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password does not same, Try again!')
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=25, required=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        username = obj.get('username')
        tokens = Account.objects.get(username=username).tokens
        return tokens

    class Meta:
        model = Account
        fields = ('username', 'password', 'tokens')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({
                "message": "Username or password not correct"
            })
        if not user.is_active:
            raise AuthenticationFailed({
                "message": "Account disabled"
            })
        return attrs


class MyProfileCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'bio', 'avatar')


class MyProfileSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'bio', 'avatar')


class MyProductSellerSerializer(serializers.ModelSerializer):
    products = ProductPOSTSerializer(required=True)

    class Meta:
        model = MyProduct
        fields = ['id', 'author', 'products', 'created_date']
        extra_kwargs = {
            'author': {'read_only': True}
        }

    def validate(self, attrs):
        author = attrs.get('author')
        if author.role == 2:
            raise AuthenticationFailed({
                "message": "You don't post Product" })
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        instance = super().create(**validated_data)
        instance.author_id = user_id
        instance.save()
        return instance


class MyProductCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProduct
        fields = ['id', 'author', 'products', 'created_date']
        extra_kwargs = {
            'author': {'read_only': True}
        }

    def validate(self, attrs):
        author = attrs.get('author')
        if author.role == 1:
            raise AuthenticationFailed({
                "message": "You don't get Product" })
        return attrs





