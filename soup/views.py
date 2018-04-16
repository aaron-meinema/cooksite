from django.shortcuts import get_object_or_404, render
from .models import Site, Page, Content


def index(request):
    page_list = Page.objects.all()
    context = {
        'page_list': page_list,
    }
    title = "super awesome"
    return render(request, 'soup/index.html', context, title)


def add(request):
    return render(request, 'soup/index.html')


def page(request, page_id):
    rendered_page = get_object_or_404(Page, id=page_id)
    return render(request, 'soup/index.html', {'rendered_page': rendered_page})
