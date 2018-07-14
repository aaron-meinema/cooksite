from django.shortcuts import get_object_or_404, render
from .models import Site, Page, Content, ContentLine
from .scrape import SmulWeb
from rest_framework import viewsets
from .serializers import ContentSerializer, ContentLineSerializer

page_list = Page.objects.all()
context ={
    'page_list': page_list,
    'active': 'none'
}


def index(request):
    context['active'] = 'home'
    context['title'] = 'this is the index page'
    return render(request, 'soup/index.html', context)


def add(request):
    site_list = Site.objects.all()
    context['title'] = 'add page here'
    context['site_list'] = site_list
    context['active'] = 'add'

    try:
        selected_page = request.POST['page']
    except KeyError:
        return render(request, 'soup/add.html', context)
    else:
        selected_site = int(request.POST['site'])
        # modular problem below 1 line
        site = SmulWeb(selected_page)
        the_title = str(site)
        page = Page(name=the_title)
        duplicate = 0
        for title in Page.objects.all():
            if title == the_title:
                duplicate = 1
        if duplicate == 0:
            page.save()
            last_page = Page.objects.last()
            this_site = Site.objects.get(id=selected_site)
            # possible modularity problem below 4 lines
            ingredients_content = Content(type="ingredients", site_id=this_site, page_id=last_page)
            instructions_content = Content(type="instructions", site_id=this_site, page_id=last_page)
            ingredients_content.save()
            instructions_content.save()
            content_instructions = Content.objects.latest('id')

            line_number = 1
            for line, keyword in site.split_lines(site.smulweb_instructions()).items():
                print(line)
                instruction_line = ContentLine(content_line=line, content_type=keyword,
                                               content=content_instructions, line_number=line_number)
                instruction_line.save()
                line_number += 1
            line_number = 1
            for line, keyword in site.split_lines(site.smulweb_ingredients()).items():
                print(line)
                ingredients_line = ContentLine(content_line=line, content_type=keyword,
                                               content_id=content_instructions.id-1, line_number=line_number)
                ingredients_line.save()
                line_number += 1
            context['selected_page'] = site.smulweb_instructions()
        else:
            context['selected_page'] = "duplicate page"
        return render(request, 'soup/add.html', context)


def page(request, page_id):
    rendered_page = get_object_or_404(Page, id=page_id)
    display_content = Content.objects.filter(page_id_id=page_id)
    content_lines = ContentLine.objects.filter(content__in=display_content)
    context['content_lines'] = content_lines
    context['display_content'] = display_content
    context['rendered_page'] = rendered_page
    context['active'] = page_id
    context['title'] = str(Page.objects.get(id=page_id).name)
    return render(request, 'soup/pages.html', context,)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentLineViewSet(viewsets.ModelViewSet):
    queryset = ContentLine.objects.all()
    serializer_class = ContentLineSerializer
