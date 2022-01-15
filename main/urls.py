from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.shorturl, name='index'),
    path('profile/', views.user_detail_urls, name='user-page'),
    path('<str:slugs>/', views.redirect_on_prime_url, name='redirect')
]
