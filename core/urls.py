from django.urls import path

from .views import IndexView, TermsView, ArticleView, LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('article/', ArticleView.as_view(), name='article'),
    path('login/', LoginView.as_view(), name='login'),

]
