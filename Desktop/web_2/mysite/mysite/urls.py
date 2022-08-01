
# """mysite URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path , include

# urlpatterns = [
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('admin/', admin.site.urls),
#     path('blog/', include('blog.urls'), name="blog"),
#     path('toy/', include('toy.urls'), name="toy"),
#     path('polls/', include('polls.urls'), name="polls"),
#     path('api-auth/', include('rest_framework.urls')),
# ]

from django.urls import path, include, re_path
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), name="blog"),
    path('toy/', include('toy.urls'), name="toy"),
    path('polls/', include('polls.urls'), name="polls"),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

