from django.contrib.auth import authenticate, get_user_model
from rest_framework.serializers import (CharField, ModelSerializer,
                                        HyperlinkedRelatedField,
                                        Serializer, ValidationError)


User = get_user_model()


class UserRegistrationSerializer(ModelSerializer):
    password = CharField(max_length=128, write_only=True)
    token = CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(Serializer):
    username = CharField(max_length=50)
    password = CharField(max_length=128, style={'input_type': 'password'}, write_only=True)
    token = CharField(max_length=100, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise ValidationError('Provided credentials don\'t match any existing user')

        else:
            raise ValidationError('Both username and password are required for authentication')

        data['user'] = user
        return data


class UserSerializer(ModelSerializer):
    followers = HyperlinkedRelatedField(many=True, read_only=True, view_name='user-detail')
    playlists = HyperlinkedRelatedField(many=True, read_only=True, view_name='playlist-detail')
    liked_songs = HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    password = CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'username', 'password', 'photo', 'followers',
                  'followers_amount', 'playlists', 'liked_songs', 'is_staff')


class UserShortInfoSerializer(ModelSerializer):

    class Meta(UserSerializer.Meta):
        fields = ('url', 'username', 'photo', 'followers',
                  'followers_amount', 'playlists')