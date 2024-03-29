from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class Client(models.Model):
    """Клиент - тот, кто получает рассылки"""
    email = models.EmailField(verbose_name='контактный email')
    name = models.CharField(max_length=255, verbose_name='Ф. И. О.')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    # user = models.ForeignKey(User, on_delete=models.CASCADE,
    #                          verbose_name='пользователь', null=True)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


def __str__(self):
    return f'{self.username} {self.email}'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема')
    body = models.TextField(verbose_name='тело')

    def __str__(self):
        return f"{self.subject} {self.body}"


class Meta:
    verbose_name = 'сообщение'
    verbose_name_plural = 'сообщение'


class Mailing(models.Model):
    CHOICES_INTERVAL = [
        ('first_time', 'разово'),
        ('day', 'раз в день'),
        ('week', 'раз в неделю'),
        ('month', 'раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена')
    ]

    title = models.CharField(max_length=255, verbose_name='заголовок рассылки')
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name='дата и время первой'
                                                    ' отправки рассылки')
    # user = models.ForeignKey(User)

    mail_to = models.ManyToManyField(Client, verbose_name='клиенты')
    periodicity = models.CharField(max_length=128, choices=CHOICES_INTERVAL,
                                   default='', verbose_name='периодичность')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True,
                                verbose_name='сообщение')
    status = models.CharField(max_length=128, choices=STATUS_CHOICES, verbose_name='статус рассылки')
