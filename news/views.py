from django.shortcuts import render, redirect
from news.models import New


def new(request):
    news = New.objects.all()
    return render(request, 'news/new.html', {'news': news})



# def about(request):
#     return render(request, 'about.html')



def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        file = request.FILES.get('file')
        return redirect('index')
    return render(request, 'news/create.html')





def detail(request,id):
    news = New.objects.get(id=id)
    news.news_view=news.news_view+1
    news.save()
    return render(request, 'news/detail.html', {"news":news})



