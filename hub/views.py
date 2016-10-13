from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Art, Category


class ArtListView(ListView):
    model = Art

    def get_queryset(self):
        qs = super(ArtListView, self).get_queryset()
        category_slug = self.kwargs.get('category')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArtListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.kwargs.get('category')
        return context


class ArtDetailView(DetailView):
    model = Art
