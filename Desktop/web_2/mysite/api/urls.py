from django.urls import include, path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
urlpatterns = [
    #이전에는 함수 - 현재는 class 로 작동하도록 urls연결 
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('posts/', views.PostList.as_view(), name="post-list"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post-detail"),
    path('questions/', views.QuestionList.as_view(), name="question-list"),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name="question-detail"),
    path('profile/', views.profile, name="profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
