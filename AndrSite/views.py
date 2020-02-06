import smtplib

from django.http import HttpResponse
from .models import MailSender
from django.shortcuts import render


def pivo(request):
    return render(request, 'mainpage.html')

def basis(request):
    return HttpResponse(MailSender.objects.all())

def goodJob(request):
    if request.method == "POST":
        mailsender = MailSender(request.POST)
        mailsender.MailTo = request.POST.get("MailTo")
        mailsender.MailText = request.POST.get("MailText")
        if IsMailCorrect(mailsender.MailTo):
            SendMessage(mailsender.MailTo, mailsender.MailText)
            return HttpResponse(mailsender.MailTo + "  Mail is correct")
        else:
            return HttpResponse(mailsender.MailTo + " Your mail nihya not correct")
    else:
        return HttpResponse("Polnoe govno bratan")

def IsMailCorrect(str00):
    if str00.find('@') > 2:
        return True
    else:
        return False

def SendMessage(toMail, textmsg):
    fromm = "hwoarang322@mail.ru"
    passwo = "pivo44Dj"

    msgDone = "\r\n".join((
        "From: %s" % fromm,
        "To: %s" % toMail,
        "Subject: %s" % "",
        "",
        textmsg))

    smtpObj = smtplib.SMTP("smtp.mail.ru", 587)
    smtpObj.starttls()
    smtpObj.login(fromm, passwo)
    smtpObj.set_debuglevel(False)
    smtpObj.sendmail(fromm, toMail, msgDone)
    smtpObj.quit()