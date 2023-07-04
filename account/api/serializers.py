from rest_framework import serializers

from account.models import User

class AccountSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=False)

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        User.objects.get_or_create(username=username , password=password)
        user = User.objects.get(username=username)
        return user
    
    def validate_username(self , value):
        for user in User.objects.all():
            if value == user.username:
                raise serializers.ValidationError('your username already existed')
        return value