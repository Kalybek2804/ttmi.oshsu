from django.shortcuts import render


def spec_programmer(request):
    return render(request, 'spec/spec_programmer.html')
