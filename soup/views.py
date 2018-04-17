from django.shortcuts import get_object_or_404, render
from .models import Site, Page, Content

page_list = Page.objects.all()
context ={
    'page_list': page_list
}


def index(request):
    context['title'] = 'this is the index page'
    return render(request, 'soup/index.html', context)


def add(request):
    site_list = Site.objects.all()
    context['title'] ='add page here'
    context['site_list'] = site_list

    try:
        selected_page = request.POST['page']
    except KeyError:
        return render(request, 'soup/add.html', context)
    else:
        context['selected_page'] = selected_page
        return render(request, 'soup/add.html', context)


def page(request, page_id):
    rendered_page = get_object_or_404(Page, id=page_id)
    context['rendered_page'] = rendered_page
    return render(request, 'soup/index.html', context,)
