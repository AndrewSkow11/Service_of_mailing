from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class Client(models.Model):
    email = models.EmailField(verbose_name='контактный email')
    name = models.CharField(max='255', verbose_name='Ф. И. О.')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')


class Mailing(models.Model):
    first_time = models.DateTimeField(auto_now_add=True,
                                      verbose_name='дата и время первой'
                                                   ' отправки рассылки')
    # periodicity = models.Choices  (verbose_name='периодичность')
