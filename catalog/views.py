from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from .models import Category, Product

def index(request):
    list_of_categories = Category.objects.all()
    list_of_products = Product.objects.all().order_by('-price')
    
    return render(request, 'index.html', {'list_of_categories':
        list_of_categories, 'list_of_products': list_of_products[:4]})

def show_category(request, category_name):
    list_of_categories = Category.objects.all()
    category = list_of_categories.get(name=category_name)
    list_of_products = category.product_set.all()
    content = {
            'list_of_categories': list_of_categories,
            'category_name': category_name,
            'list_of_products': list_of_products,
            }

    return render(request, 'catalog.html', content)

class SearchView(ListView):
    model = Product 
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
                Q(name__icontains=query) | Q(article__icontains=query) )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_categories'] = Category.objects.all()
        context['search'] = self.request.GET.get('q')
        return context


