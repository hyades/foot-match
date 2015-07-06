from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse

from models import User, Game, Score, Match

import json
import datetime
# Create your views here.


def index(request):
    return render_to_response('index.html', {})


def users(request):
    users = [
        {
            "user_id": i.id,
            "user_name": i.user_name,
            "user_email": i.user_email
        } for i in User.objects.all()
    ]
    return JsonResponse({'users': users})


def users_details(request, user_id):
    user = User.objects.get(id=user_id)
    matches = [
        {
            "match_id": i.id,
            "match_time": i.match_time
        }
        for i in Match.objects.filter(users__id=user_id)
    ]
    return JsonResponse(
        {
            "user_id": user.id,
            "user_name": user.user_name,
            "user_email": user.user_email,
            "matches": matches
        }
    )


def games(request):
    games = [
        {
            "game_id": i.id,
            "game_name": i.game_name,
            "game_desc": i.game_desc
        }
        for i in Game.objects.all()
    ]
    return JsonResponse({'games': games})


def users_new(request):
    content = json.loads(request.body)
    name = content['user_name']
    email = content['user_email']
    user = User(user_name=name, user_email=email)
    user.save()
    return JsonResponse({"success": "ok"})


def matches(request):
    matches = []
    for match in Match.objects.all().order_by('-match_time'):
        matches.append(
            {
                "match_id": match.id,
                "match_time": match.match_time,
            })
    return JsonResponse({"matches": matches})


def match_new(request):
    # print request.body
    content = json.loads(request.body)
    time = content['match_time']
    users = content['users']
    game_id = content['game']
    match = Match(match_time=time)
    match.save()
    match.game = Game(id=game_id)
    match.users = [user['user_id'] for user in users]
    match.save()
    return JsonResponse({"success": "ok"})


def match_detail(request, match_id):
    match = Match.objects.get(id=match_id)
    score_desc = match.score.score_desc if match.score else None
    game = match.game.game_name if match.game else None
    users = [
        {
            "user_name": i.user_name,
            "user_id": i.id
        }
        for i in match.users.all()
    ]
    resp = {
        "match_time": match.match_time,
        "users": users,
        "score": score_desc,
        "game": game,
    }
    return JsonResponse(resp)


def match_edit(request, match_id):
    content = json.loads(request.body)
    time = content['match_time']
    users = content['users']
    score_desc = content['score']

    match = Match.objects.get(id=match_id)
    match.match_time = time
    match.users = [user['user_id'] for user in users]
    score = None
    if match.score:
        score = match.score
        score.score_desc = score_desc
        score.save()
    else:
        if score_desc:
            score = Score(score_desc=score_desc)
            score.save()
    if score:
        match.score = score
    match.save()
    return JsonResponse({"success": "ok"})


def match_register(request, match_id, user_id):
    user = User.objects.get(id=user_id)
    match = Match.objects.get(id=match_id)
    match.users.add(user)
    return JsonResponse({"success": "ok"})
