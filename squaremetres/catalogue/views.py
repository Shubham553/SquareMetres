from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import ModelFormMixin
from .forms import *
from .models import *
from django.views.generic import CreateView, UpdateView


# def index(request):
#     catalogue = Catalogue.objects.order_by('-catalogue_date').filter(is_published=True)
#     paginator = Paginator(catalogue, 6)
#     page = request.GET.get('page')
#     paged_catalogues = paginator.get_page(page)
#     context = {
#         'catalogues': paged_catalogues
#     }
#     return render(request, 'catalogues/catalogues.html', context)
#
#
# def catalogue(request, catalogue_id):
#     catalogue = get_object_or_404(Catalogue, pk=catalogue_id)
#     context = {
#         'listing': catalogue
#     }
#     return render(request, 'catalogues/catalogues.html', context)
#
#
# def search(request):
#     queryset_catalogue = Catalogue.objects.order_by('-catalogue_date')
#
#     # Keywords
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_catalogue = queryset_catalogue.filter(description__icontains=keywords)
#
#     # City
#     if 'city' in request.GET:
#         city = request.GET['city']
#         if city:
#             queryset_catalogue = queryset_catalogue.filter(city__iexact=city)
#
#     # State
#     if 'state' in request.GET:
#         state = request.GET['state']
#         if state:
#             queryset_catalogue = queryset_catalogue.filter(state__iexact=state)
#
#     # Bedrooms
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             queryset_catalogue = queryset_catalogue.filter(bedrooms__lte=bedrooms)
#
#     # Price
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_catalogue = queryset_catalogue.filter(price__lte=price)
#
#     context = {
#         'state_choices': state_choices,
#         'bedroom_choices': bedroom_choices,
#         'price_choices': price_choices,
#         'catalogues': queryset_catalogue,
#         'values': request.GET
#     }
#     return render(request, 'catalogues/search.html', context)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def property(request, id):
    property_view = Catalogue.objects.get(id=id)
    # images = property.images.all()

    context = {
        'property': property_view,
        # 'images':images

    }
    return render(request, 'property.html', context)


def properties(request):
    properties_view = Catalogue.objects.all()
    # count = 1
    # images = []
    # for i in properties:
    # if count == 1:
    # images = i.images.all()
    # count = count + 1
    # print(images[0].image)
    return render(request, 'properties.html', {'properties': properties_view, })


def contactus(request):
    return render(request, 'contact.html')


class AddProperty(CreateView):
    # model = Catalogue
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.profile = self.request.user
        self.object.save()
        return super(AddProperty, self).form_valid(form)

