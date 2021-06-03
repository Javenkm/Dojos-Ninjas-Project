from django.shortcuts import render, redirect

from .models import *

def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }
    return render(request, 'index.html', context)


def createDojo(request):
    name = request.POST['dojo_name']
    city = request.POST['dojo_city']
    state = request.POST['dojo_state']
    desc = request.POST['dojo_desc']
    Dojo.objects.create(
        name = name,
        city = city,
        state = state,
        desc = desc,
    )
    return redirect("/")


def createNinja(request):
    dojo = Dojo.objects.get(id = request.POST['dojo_id'])
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    Ninja.objects.create(
        dojo = dojo,
        first_name = first_name,
        last_name = last_name,
    )
    return redirect('/')


def delete_dojo(request):
    dojo = Dojo.objects.get(id = request.POST['dojo_delete'])
    dojo.delete()

    return redirect('/')