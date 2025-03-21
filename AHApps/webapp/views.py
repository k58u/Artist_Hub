import requests
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from AHApps.artist.models import Artist, ArtistProfile,ArtistCatalogue,ArtistCatalogueCategory
from django.db.models import Q

def base(request):
    query = request.GET.get('query', '')  # Get the query from the GET request
    category_filter = request.GET.get('category', '')  # Get the category filter from the GET request
    
    # Fetch all categories to populate the dropdown
    categories = ArtistCatalogueCategory.objects.all()

    catalogues = ArtistCatalogue.objects.all()  # Default to all catalogues if no query is provided

    if query:
        # If there's a query, filter catalogues by title, content, or category name
        query_terms = query.split()
        filters = Q()  # Initialize an empty filter
        
        for term in query_terms:
            # Apply query terms to title, content, or category name
            filters |= Q(title__icontains=term) | Q(content__icontains=term) | Q(categories__name__icontains=term)

        catalogues = catalogues.filter(filters).distinct()  # Use distinct to avoid duplicate catalogues
    
    if category_filter:
        # If there's a category filter, filter catalogues by the selected category
        catalogues = catalogues.filter(categories__name__icontains=category_filter).distinct()

    return render(request, 'web/base.html', {'catalogues': catalogues, 'query': query, 'category_filter': category_filter, 'categories': categories})

def catalogue_detail(request, catalogue_id):
    artist_catalog = ArtistCatalogue.objects.filter(artist_catalogue_id=catalogue_id).prefetch_related('categories').first()

    context = {
        'catalog': artist_catalog,
        'categories': artist_catalog.categories.all() if artist_catalog else []
    }
    print(context) 
    return render(request, "web/catalogue_detail.html", context)

def home(request):
    catalogues = ArtistCatalogue.objects.all()[12:]  # Fetch all catalogues
    return render(request, 'web/home.html', {'catalogues': catalogues})

