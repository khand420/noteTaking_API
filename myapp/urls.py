from django.urls import include, path
from .views import TodoCreate, TodoList, TodoDetail, TodoUpdate, TodoDelete


urlpatterns = [
	path('create/', TodoCreate.as_view(), name='create-Todo'),
    path('', TodoList.as_view()),
    path('<int:pk>/', TodoDetail.as_view(), name='retrieve-Todo'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update-Todo'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete-Todo')
]