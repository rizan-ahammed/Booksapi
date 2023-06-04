from django.urls import path
from api.v1.books.views import books,bookssingle,add_to_favorites,create,update,delete,view_favorites

urlpatterns = [
    path("",books ),
    path('<int:pk>/',bookssingle),
    path('create/',create),
    path('<int:pk>/update/',update ),
    path('<int:pk>/delete/',delete ),
    path('<int:pk>/add-to-favorites/',add_to_favorites),
    path('view-favorites/',view_favorites),

]
