from django.shortcuts import render_to_response
from artists.models import Guitarrist

def guitarrists(request):
    
    context = {
        'guitarrists': Guitarrist.objects.all()
    }
    return render_to_response('artists/guitarrists.html', context)