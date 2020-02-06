from django.db import models
import datetime
from django.utils import timezone

class MailSender(models.Model):
    MailTo = models.CharField('Почта получателя', max_length = 50)
    MailFrom = models.CharField('Почта отправителя',max_length = 50)
    MailText = models.TextField('Текст сообщения')
    def __str__(self):
        return self.MailTo

    def whenMail(self):
        return timezone.now()