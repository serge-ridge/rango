from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/',
         views.category, name='category'),
    path('category/<slug:category_name_slug>/add_page/',
         views.add_page, name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('search/', views.search, name='search'),
    path('goto/', views.track_url, name='goto'),
    path('like_category/', views.like_category, name='like_category'),
    path('suggest_category/', views.suggest_category, name='suggest_category'),
    path('auto_add_page/', views.auto_add_page, name='auto_add_page'),
]
