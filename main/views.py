from django.shortcuts import render

from main.forms import MailingForm
from main.models import Mailing
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class MailingListView(ListView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailing_list')
    extra_context = {
        "title": "Создание новой рассылки"
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form, *args, **kwargs):
        if form.is_valid():
            new_mailing = form.save(commit=False)
            new_mailing.user = self.request.user
            new_mailing.save()
        return super().form_valid(form)


class MailListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Список рассылок'
    }
