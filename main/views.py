from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Alexander Audric Johansyah',
        'class': 'PBP C',
        'npm': '2206815466',
        'app': 'SoundW♫ve',
        'description': "Discover and enjoy a vast music library with our extensive collection",
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
        }
    }

    return render(request, "main.html", context)