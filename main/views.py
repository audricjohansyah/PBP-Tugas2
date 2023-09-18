from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    items = Item.objects.all()
    context = {
        'name': 'Alexander Audric Johansyah',
        'class': 'PBP C',
        'npm': '2206815466',
        'app': 'SoundW♫ve',
        'description': "Discover and enjoy a vast music library with our extensive collection",
        'items': items,
        'item_count' : Item.objects.count(),
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
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

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

# def count_items(request):
#     # Lakukan kueri ke model Anda dan hitung jumlah item
#     item_count = Item.objects.count()

#     context = {'item_count': item_count}
#     return render(request, "main", context)