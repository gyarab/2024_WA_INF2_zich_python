from django.shortcuts import render, get_object_or_404
from .models import EngineSpecifications, Category, Manufacturer

def index(request):
    engines = EngineSpecifications.objects.all()
    categories = Category.objects.all()
    manufacturers = Manufacturer.objects.all()
    return render(request, 'AplikaceUkol/index.html', {
        'engines': engines,
        'categories': categories,
        'manufacturers': manufacturers
    })

def engine_detail(request, pk):
    engine = get_object_or_404(EngineSpecifications, pk=pk)
    categories = engine.categories.all()
    manufacturer = engine.manufacturer
    return render(request, 'AplikaceUkol/engine_detail.html', {
        'engine': engine,
        'categories': categories,
        'manufacturer': manufacturer
    })

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    engines = EngineSpecifications.objects.filter(categories=category)
    return render(request, 'AplikaceUkol/category_detail.html', {
        'category': category,
        'engines': engines
    })

def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    engines = EngineSpecifications.objects.filter(manufacturer=manufacturer)
    return render(request, 'AplikaceUkol/manufacturer_detail.html', {
        'manufacturer': manufacturer,
        'engines': engines
    })