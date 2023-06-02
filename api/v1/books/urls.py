from django.urls import path
from api.v1.books import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:pk>/', views.bookssingle, name='bookssingle'),
    path('<int:pk>/add-to-favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
