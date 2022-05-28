from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer, CreateUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        ''' @override
        '''
        return CreateUserSerializer if self.action == 'create' else UserSerializer
