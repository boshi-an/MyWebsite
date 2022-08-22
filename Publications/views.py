from django.shortcuts import render

# Create your views here.

def IndexView(OriginalRequest) :

    context = {}

    return render(OriginalRequest, 'index.html', context)