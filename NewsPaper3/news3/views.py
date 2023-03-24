
from django.views.generic import ListView

from .models import News
from .forms import DummyForm
from .filters import NewsFilter


class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 1
    form_class = DummyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DummyForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)
        # header = request.POST.get['header']
        # description = request.POST.get['description']
        # email = request.POST.get['email']
        # news = News(header=header, description=description, email=email)  # создаём новый товар и сохраняем
        # news.save()
        # return super().get(request, *args, **kwargs)


class Search(ListView):
    model = News
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context
