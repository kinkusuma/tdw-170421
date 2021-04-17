from django.shortcuts import render, redirect
from apps.models import Users_tb, Skill_tb
from apps.forms import FormUser, FormSkill

# Create your views here.
def main(request):
    users = Users_tb.objects.all()
    skills = Skill_tb.objects.all()

    context = {
        'users' : users,
        'skills' : skills
    }

    return render(request, 'index.html', context)

def tambah(request):
    if request.POST:
        form = FormUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormUser()
            return redirect('main')
    else:
        form = FormUser()

        context = {
            'form' : form,
        }

    return render(request, 'add.html', context)

def ubah(request, id_user):
    user = Users_tb.objects.get(id=id_user)
    if request.POST:
        form = FormUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            form = FormUser()
            return redirect('main')
    else:
        form = FormUser(instance=user)
        context = {
            'user' : user,
            'form' : form
        }

    return render(request, 'ubah.html', context)

def hapus(request, id_user):
    user = Users_tb.objects.get(id=id_user)
    user.delete()
    return redirect('main')