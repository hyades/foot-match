from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',

    url(r'users/?$', views.users, name='users'),
    url(r'users/(?P<user_id>[0-9]+)/?$', views.users_details, name='users_details'),
    url(r'games/?$', views.games, name='games'),
    url(r'users/new/?$', views.users_new, name='users_new'),
    url(r'matches/?$', views.matches, name='matches'),
    url(r'matches/(?P<match_id>[0-9]+)/?$', views.match_detail, name='match_detail'),
    url(r'matches/new/?$', views.match_new, name='match_new'),
    url(r'matches/edit/(?P<match_id>[0-9]+)/?$', views.match_edit, name='match_edit'),
    url(r'matches/(?P<match_id>[0-9]+)/register/(?P<user_id>[0-9]+)/?$', views.match_register, name='match_register'),
    url(r'/?$', views.index, name='index'),
)
