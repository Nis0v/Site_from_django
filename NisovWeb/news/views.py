from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView



def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'artiles'

def create(request):
    error = ''
    if request.method == "post":
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return request('news')
        else:
           error = 'Форма была неверно заполнена'
    form = ArtilesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)