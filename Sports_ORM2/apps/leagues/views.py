from django.db.models import Q
from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"atlantic_soccer": Team.objects.filter(league__name__iexact='atlantic soccer conference'),
		"boston_penguins": Player.objects.filter(Q(curr_team__team_name__iexact='penguins') & Q(curr_team__location__iexact='boston')),
		"intl_coll_baseball": Player.objects.filter(curr_team__league__name__iexact='international collegiate baseball conference'),
		"players_lopez": Player.objects.filter(last_name__iexact='lopez').filter(curr_team__league__name__iexact='American Conference of Amateur Football'),
		"football_players": Player.objects.filter(all_teams__league__sport__iexact='football').distinct(),
		"sophia_teams": Team.objects.filter(curr_players__first_name__iexact="sophia"),
		"sophia_leagues": League.objects.filter(teams__curr_players__first_name__iexact="sophia"),
		"flores_noroughriders": Player.objects.filter(last_name__iexact='flores').exclude(curr_team__team_name__iexact='washington roughriders'),
		"samevans_teams": Team.objects.filter(all_players__first_name__iexact="samuel", all_players__last_name__iexact='evans'),
		"manitoba_players": Player.objects.filter(Q(all_teams__team_name__istartswith='manitoba') | Q(curr_team__team_name__istartswith='manitoba')),
		"wichita_players": Player.objects.filter(all_teams__team_name__istartswith='wichita'),
		# Not working quite right. Not excluding Oregon Colts
		"jacobgray_teams": Team.objects.filter(all_players__first_name__iexact='jacob', all_players__last_name__iexact='gray').exclude(team_name__iexact='oregon colts'),
		"joshua_players": Player.objects.filter(first_name__iexact='joshua').filter(all_teams__league__name__iexact='Atlantic Federation of Amateur Baseball Players'),
		# Unable to figure out
		# "twelve_players": Team.objects.all_players.annotate
		# (player_count=Count('first_name')).filter(player_count__gt=12),

		# count_players_teams

		# "jacobgray_teams": Team.objects.filter(Q(all_players__first_name__iexact='jacob') & Q(all_players__last_name__iexact='gray')).exclude(team_name__iexact='oregon colts'),


		# "baseball_leagues": League.objects.filter(sport__icontains='baseball'),
		# "womens_leagues": League.objects.filter(name__icontains='women'),
		# "hockey_leagues": League.objects.filter(sport__icontains='hockey'),
		# "nofootball_leagues": League.objects.exclude(sport__icontains='football'),
		# "conference_leagues": League.objects.filter(name__icontains='conference'),
		# "atlantic_region_leagues": League.objects.filter(name__icontains='atlantic'),
		# "dallas_teams": Team.objects.filter(location__icontains='dallas'),
		# "raptors_teams": Team.objects.filter(team_name__icontains='raptors'),
		# "city_teams": Team.objects.filter(location__icontains='city'),
		# "t_teams": Team.objects.filter(team_name__istartswith='t'),
		# "bylocation_teams": Team.objects.all().order_by('location'),
		# "reverse_teams": Team.objects.all().order_by('-team_name'),
		# "cooper_players": Player.objects.filter(last_name__iexact='cooper'),
		# "joshua_players": Player.objects.filter(first_name__iexact='joshua'),
		# "cooper_nojoshua_players": Player.objects.filter(last_name__iexact='cooper').exclude(first_name__iexact='joshua'),
		# "alexander_wyatt_players": Player.objects.filter(Q(first_name__iexact='alexander') | Q(first_name__iexact='wyatt')),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")