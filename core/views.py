from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Episodes
from .episodes import *


@login_required
def index(request):
    if request.method == 'POST':
        e = int(request.POST.get('NUM'))
        if request.user.episodes.filter(episode=e).exists():
            request.user.episodes.get(episode=e).delete()
        else:
            Episodes(user=request.user, episode=e).save()
        return HttpResponse()

    episode_set = set([e.episode for e in request.user.episodes.all()])
    trailer_set = set(TRAILERS)

    for e in E:
        e['CHK'] = 1 if int(e['NUM']) in episode_set else 0
        e['TRA'] = f"/static/core/audio/{e['NUM']}.mp3" if int(e['NUM']) in trailer_set else ''
        e['LIN'] = LINKS[e['NUM']] if request.user.is_superuser and e['NUM'] in LINKS else ''

    return render(request, 'core/index.html', {'E': E})



