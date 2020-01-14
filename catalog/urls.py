from django.urls import path

from .views import index, show_category, SearchView

urlpatterns = [
    path('', index, name='index'),
    path('catalog/<str:category_name>/',show_category,name='catalog'),
    path('search/', SearchView.as_view(), name='search_view'),
]
