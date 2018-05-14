from django.shortcuts import get_object_or_404, render
from .models import Site, Page, Content
from .scrape import smulweb_ingredients, smulweb_instructions, title

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
        selected_site = request.POST['site']
        #smulweb
        if selected_site == "1":
            site = selected_page
            ingredients = smulweb_ingredients(site, "div.ingredienten")
            instructions = smulweb_instructions(site, "div.itemprop_instructions")
            the_title = title(site)
            page = Page(name=the_title)
            duplicate = 0
            for previous in Page.objects.all():
                if previous.name == the_title:
                    duplicate = 1
            if duplicate == 0:
                page.save()
                last_page = Page.objects.last()
                this_site = Site.objects.get(id=1)
                ingredients_content = Content(type="ingredients", content=ingredients, site_id=this_site, page_id=last_page)
                instructions_content = Content(type="instructions", content=instructions, site_id=this_site, page_id=last_page)

                ingredients_content.save()
                instructions_content.save()
                context['selected_page'] = instructions
            else:
                context['selected_page'] = "duplicate page"
            return render(request, 'soup/add.html', context)


def page(request, page_id):
    rendered_page = get_object_or_404(Page, id=page_id)
    display_content = Content.objects.filter(page_id_id=page_id)
    context['display_content'] = display_content
    context['rendered_page'] = rendered_page
    context['active'] = page_id
    context['title'] = Page.objects.get(id=page_id).name.__str__()
    return render(request, 'soup/pages.html', context,)
