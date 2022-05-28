from rest_framework import routers
from posts import views as post_vs

# Register api routes here
routers = routers.DefaultRouter()
routers.register(r'', post_vs.PostViewSet, 'posts')
