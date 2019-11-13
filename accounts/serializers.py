from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):

    phone_number = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.phone_number = self.validated_data.get('phone_number', '')
        user.save(update_fields=['phone_number', ])
