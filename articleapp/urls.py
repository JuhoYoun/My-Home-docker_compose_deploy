from django.urls import path, include
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = "articleapp"

urlpatterns = [
    #path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'), # Django에서 기본적으로 제공해준다. 우리가 Template만 지정해주면 나머지는 다 만들어준다
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]