from rest_framework import routers
from users import views as user_vs

# Register api routes here
routers = routers.DefaultRouter()
routers.register(r'', user_vs.UserViewSet, 'users')
