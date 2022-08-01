from django.urls import include, path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
