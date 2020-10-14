from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('todosposts/', PostListView.as_view(), name="todos"),
    path('detalhes/<int:pk>/', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view()),
]