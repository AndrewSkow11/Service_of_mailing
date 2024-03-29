from django.shortcuts import render
from main.models import Mailing
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView


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
    fields = ['title', 'mail_to', 'periodicity', 'message', 'status']
