from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'form.html')
