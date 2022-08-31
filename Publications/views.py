from django.shortcuts import render
from SiteView.models import MyTitles, ContactMethod
from Publications.models import Publication
from preferences import preferences
import markdown

# Create your views here.

def IndexView(original_request) :

    context = {}

    # Dealing with titles
    all_title = ""
    my_titels = MyTitles.objects.all()

    for i, title in enumerate(my_titels) :

        if i != len(my_titels)-1 :
            all_title += title.name + " | "
        else :
            all_title += title.name
    
    context["Title"]        = all_title


    # Dealing with contact methods
    all_contact = []
    my_contacts = ContactMethod.objects.all()

    for contact in my_contacts :

        all_contact.append((contact.link, contact.icon))
    
    context["Contact"]      = all_contact

    # Dealing with site preferences
    context["Name"]         = preferences.SitePreference.my_name
    context["Photo"]        = preferences.SitePreference.my_photo
    context["Introduction"] = markdown.markdown(preferences.SitePreference.my_brief_intro, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',  # 语法高亮拓展
        'markdown.extensions.toc'  # 自动生成目录
    ])
    
    # Dealing with publications
    context["Publications"] = Publication.objects.all()

    return render(original_request, 'index.html', context)