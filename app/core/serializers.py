from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ["groups", "user_permissions"]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5},}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
    

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            msg = _('No existe el usuario con el correo y/o clave ingresada!')
            raise serializers.ValidationError(msg, code='authorization')


        attrs['user'] = user
        return attrs


