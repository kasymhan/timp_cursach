from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .forms import *
import json
from django.contrib.auth import login, authenticate
import os


# Create your views here.
def Site(request):
    file = Announcement.objects.all()
    try:
        if request.session['user']['login']:
            a = 1
        else:
            a = 0
        return render(request, 'index.html', context={'product': file, 'b': a})
    except:
        return render(request, 'index.html', context={'product': file})


class Registration(View):
    def get(self, request):
        form_registr = registration()
        return render(request, 'blog/регистрация.html', context={'form': form_registr})

    def post(self, request):
        form_registr = registration(data=request.POST, files=request.FILES)
        if form_registr.is_valid():
            abament = form_registr.sign_up()
            return redirect(abament)
        return render(request, 'blog/регистрация.html', context={'form': form_registr})


class Auth(View):
    def get(self, request):
        form = auth()
        return render(request, 'index.html', context={'auth': form})

    def post(self, request):
        auth_registr = auth(request.POST)
        autht = authenticate(request.POST)
        if auth_registr.is_valid():
            user = auth_registr.sign_in()
            if user == 'profile':
                request.session['user'] = {'login': request.POST.get('login')}
            return redirect(user)
        return render(request, 'index.html', context={'form': auth_registr})


class logout(View):
    def get(self, request):
        if 'user' in request.session:
            del request.session['user']
            return redirect('site')
        return render(request, 'index.html')


class Announcemen(View):
    def get(self, request):
        return render(request, 'blog/Аnnouncement.html', context={'form': ''})

    def post(self, reguest):
        notions = anouncement(reguest.POST)
        if notions.is_valid():
            notions2 = notions.notion(reguest.session['user']['login'])
            return redirect('profile')
        return render(reguest, 'blog/Аnnouncement.html', context={'form': notions})


class Profile(View):
    def get(self, request):
        try:
            if 'user' in request.session:
                user = Acconts.objects.filter(login=request.session['user']['login']).values()
                file = os.path.abspath(user.values()[0]['file_l'])
                if user:
                    nots = Announcement.objects.filter(
                        accounts=Acconts.objects.filter(login=request.session['user']['login']).get()).all()
                    account = User.objects.filter(
                        account=Acconts.objects.filter(login=request.session['user']['login']).get()).all()
                    return render(request, 'blog/profile.html',
                                  context={'notes': nots, 'name': account.values()[0], 'file': user.values()[0]})
            return render(request, 'index.html', context={'user': request.session['user']})
        except:
            pass

    def post(self, request):
        pass


class Delete_Announcement(View):
    def post(self, request):
        if 'id12' in request.POST:
            id = request.POST.get('id12')
            Announcement.objects.filter(id=id).delete()
            return redirect('profile')
        elif 'redirect' in request.POST:
            id = request.POST.get('redirect')
            file = Announcement.objects.filter(id=id).values()
            return render(request, 'blog/rqdirect_Аnnouncement.html', context={'file': file})


class Search(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        if 'search' in request.POST and request.POST.get('search'):
            name = request.POST.get('search')
            notes = Announcement.objects.filter(Name=name).all()
            return render(request, 'index.html', context={'product': notes})

        return render(request, 'index.html', context={'product': Announcement.objects.all()})


class An(View):
    def post(self, request):
        anc = Announcement.objects.filter(id=request.POST.get('id'))
        anc.update(Name=request.POST.get('Name'), inform=request.POST.get('Text'), price=request.POST.get('price'))
        return redirect('profile')


class Ac(View):
    def get(self, request):
        ac = Acconts.objects.filter(login=request.session['user']['login'])
        return render(request, 'blog/redirect_profile.html', context={'user': ac})


class Anouc(View):
    def get(self, request, pk):
        anc = Announcement.objects.filter(id=pk).values()
        print(anc)
        return render(request, 'blog/anouc.html', context={'an': anc[0]})
