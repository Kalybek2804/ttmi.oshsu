from django.shortcuts import render

def about(request):
    return render(request, 'about/about.html')



def maps(request):
    return render(request, 'about/maps.html')