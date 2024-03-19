from django.shortcuts import render
from .forms import *
from django.views import View
from .models import *
from .mail import *


class LetterCreateView(View):
    def get(self,request):
        form = LetterCreateForm()
        return render(request, 'tesr/index.html', {'form':form})
    def post(self, request):
        form = LetterCreateForm(request.POST,request.FILES)

        if form.is_valid():
            letter = form.save(commit=False)
            letter.creater = request.user
            letter.save()
        return render(request, 'tesr/index.html', {'form':form})

class LetterSend(View):
    def get(self, request, pk):
        model = letter.objects.get(pk=pk)
        form = LetterSendForm()
        return render(request, 'letter/mail.html', {'model':model, 'form':form})
    def post(self, request, pk):
        model = letter.objects.get(pk=pk)
        text = model.path.read().decode('utf-8')
        text = text.replace('/text/', request.POST['description'])
        form = LetterSendForm()
        req = request.POST
        send_ya_mail([req['mail']], text ,req['title'])
        return render(request, 'letter/mail.html', {'model': model, 'form': form})