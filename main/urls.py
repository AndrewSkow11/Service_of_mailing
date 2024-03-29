from django.urls import path

from main.apps import MainConfig
from main.views import index, MailingListView, MailingDeleteView, MailingDetailView, MailingUpdateView, MailingCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>/', MailingDetailView.as_view(), name='mailing_delete'),
]