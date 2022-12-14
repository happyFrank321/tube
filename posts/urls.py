from django.urls import path
from . import views

urlpatterns = [
    # Просмотр группы
    path("group/<slug:slug>/", views.group_posts),
    # Создание поста
    path("new/", views.new_post, name="new_post"),
    # Главная страница
    path('', views.index, name='index'),
    # Профайл пользователя
    path('<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),
    path(
        '<str:username>/<int:post_id>/edit/', 
        views.post_edit, 
        name='post_edit'
        ),
]