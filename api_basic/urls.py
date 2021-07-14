from django.urls import path
from .views import ArticleAPIView, ArticleDetailsAPIView, GenericAPIView

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetailsAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view())

]
