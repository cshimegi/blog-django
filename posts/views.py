from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer, CreatePostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        ''' @override
        '''
        return CreatePostSerializer if self.action == 'create' else PostSerializer
