from django.urls import path
from api import views
from knox import views as knox_views

urlpatterns = [
    path("users/",views.UserView.as_view()),
    path("users/<int:pk>",views.RetrieveUserView.as_view()),
    path("blog/",views.BlogListView.as_view()),
    path('blog/<int:pk>',views.RetrieveBlogView.as_view()),
    path('author',views.AuthorListView.as_view()),
    path('author/<int:pk>',views.RetrieveAuthorView.as_view()),
    path('comment',views.CommentListView.as_view()),
    path('comment/<int:pk>',views.RetrieveComment.as_view()),
    #path('register/', views.RegisterAPI.as_view()),
    #path('login/', views.LoginAPI.as_view()),
    #path('logout/', knox_views.LogoutView.as_view()),
]
