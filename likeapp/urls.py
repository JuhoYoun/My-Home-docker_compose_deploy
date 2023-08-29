from django.urls import path, include

from likeapp.views import LikeArticleView

app_name = "likeapp"

urlpatterns = [
    path('article/like/<int:pk>', LikeArticleView.as_view(), name='article_like')
]