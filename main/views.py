import datetime
import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    user_id = request.user.id
    random_number = random.randint(10**8, 10**9 - 1)
    formatted_random_number = f"{random_number:09d}"
    random_alphabet_char = random.choice(string.ascii_letters)
    context = {
        'name': request.user.username,
        'class': f'PBP {random_alphabet_char.upper()}',
        'npm': '2206815466',
        'app': 'SoundW♫ve',
        'description': "Discover and enjoy a vast music library with our extensive collection",
        'items': items,
        'random_user_id': f'{user_id} - {formatted_random_number}',
        'item_count' : items.count(),
        'last_login': request.COOKIES['last_login'],
        'albums': {
            '1': "What's Going On",
            '2': 'H2O',
            '3': 'Never Too Much',
            '4': 'La La Means I Love You',
            '5': 'My Cherie Amour'
        },
        'duration': {
            '1': '35 min 32 sec',
            '2': '46 min 31 sec',
            '3': '36 min 57 sec',
            '4': '31 min 18 sec',
            '5': '35 min 53 sec'
        },
        'year':{
            '1': '1971',
            '2': '1982',
            '3': '1981',
            '4': '1968',
            '5': '1969'
        },
        'artists':{
            '1': 'Marvin Gaye',
            '2': 'Daryl Hall & John Oates',
            '3': 'Luther Vandross',
            '4': 'The Delfonics',
            '5': 'Stevie Wonder'
        },
        'stock':{
            '1': '2',
            '2': '5',
            '3': '4',
            '4': '1',
            '5': '6'
        },
        'artwork':{
            '1': 'https://resources.tidal.com/images/454e707d/13c8/4cb3/84e9/494d69f66f97/640x640.jpg',
            '2': "https://resources.tidal.com/images/2c9417ec/11ca/411e/8729/0acbda2f76ce/640x640.jpg",
            '3': "https://resources.tidal.com/images/819ba4c9/88f2/4336/b1f1/02b08727cfb5/640x640.jpg",
            '4': "https://i.scdn.co/image/ab67616d0000b273afd192f82c3e9904b13714aa",
            '5': "https://resources.tidal.com/images/79c2be89/3a61/47d5/abd5/31a86a958c79/640x640.jpg"
        }
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)

def delete_product(request, id):
    itemdelete = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        itemdelete.delete()
        return redirect('main:show_main')
    
    return render(request, 'delete_product.html', {'item': itemdelete})

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increment_amount(request, id):
    product = get_object_or_404(Item, pk=id)
    product.amount += 1
    product.save()
    return redirect('main:show_main')

def decrement_amount(request, id):
    product = get_object_or_404(Item, pk=id)
    if product.amount > 0:
        product.amount -= 1
        product.save()
    if product.amount <= 0:
        product.delete()
    return redirect ('main:show_main')