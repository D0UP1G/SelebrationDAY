from django.shortcuts import render
from .forms import *
from django.views import View
from .models import *
from .mail import *
from django.shortcuts import redirect

def SendMail(request):
    return render(request, 'letter/mail-sended.html')

class LetterCreateView(View):
    def get(self,request):
        if request.user.is_authenticated:
            form = LetterCreateForm()
            return render(request, 'letter/mailsend.html', {'form':form})
        else:
            return redirect('user:registration')
    def post(self, request):
        if request.user.is_authenticated:
            form = LetterCreateForm(request.POST,request.FILES)


            if form.is_valid():
                letter = form.save(commit=False)
                letter.creater = request.user
                letter.save()
            return render(request, 'letter/mailsend.html', {'form':form, 'succeful':'Succes'})
        else:
            return redirect('user:registration')

class LetterView(View):

    def get(self, request):
        post = letter.objects.all()
        posts = post[::-1]

        return render(request, 'letter/vid-mail.html', {'post_l': posts} )

    

class LetterSend(View):
    def get(self, request, pk):
        model = letter.objects.get(pk=pk)
        form = LetterSendForm()
        return render(request, 'letter/mail.html', {'model':model, 'form':form})
    

    def post(self, request, pk):
        model = letter.objects.get(pk=pk)
        text = model.path.read().decode('utf-8')
        html = text.replace('/text/', request.POST['description'])
        form = LetterSendForm()
        req = request.POST
        send_ya_mail([req['mail']], html ,req['title'])
        return redirect('letter:sended')