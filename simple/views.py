from __future__ import print_function
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from GChartWrapper import *
# from django.template import loader

import twitter
#Twitanalyser1
CONSUMER_KEY = ('i5kSIFav5k85d8nhORtaSZYhW')
CONSUMER_SECRET = ('cH12dv61ujPZFuxKUA4L0NztjVoI7clslE6kueHZvy42C02B5A')
ACCESS_TOKEN = ('1362707197-6Eu0rmnlPHaj6cZMtbxUaW9SOIYOx571a4KdMg0')
ACCESS_TOKEN_SECRET = ('fwClOx7brVjSyJYW4EBDWXM5i9t9ON6BPnU1CKL187J7f')

#TwitAnalyser2
# CONSUMER_KEY = ('OHuaRYejmnfKLj7FCQEqpL94x')
# CONSUMER_SECRET = ('Ldvek8fW5OqtbgkVWSGDZ8VM5a2V7FnIR58aH3Vyk7bWTD8FDI')
# ACCESS_TOKEN = ('1362707197-uVEfSe9TevJnHaC2ez28CkycGWOCach95kRtPC5')
# ACCESS_TOKEN_SECRET = ('6Zq5rXfZKZsZaiOfLmVPo4YSAlJbxepWsvzqCFpbbLrTJ')

def home(request):
	return render(request, 'simple/take_handle.html')

def search(request):
	api = twitter.Api(consumer_key=CONSUMER_KEY,
						consumer_secret=CONSUMER_SECRET,
						access_token_key=ACCESS_TOKEN,
						access_token_secret=ACCESS_TOKEN_SECRET)
	final_graphs = []
	response = HttpResponse()
	
	if 'handle' in request.GET and request.GET['handle']:
		t_handle = str(request.GET['handle'])
		response.write(format(request.GET['handle']))

		me = api.GetUser(screen_name = t_handle)
		# response.write(me)
		friends = api.GetFriends(screen_name = t_handle)
		followers = api.GetFollowers(screen_name = t_handle)
		
		final_graphs.append(ratio_chart(me))
		final_graphs.append(create_profile(followers))
		final_graphs.append(ff_count(friends, followers))
		final_graphs.append(friends_count(friends, followers))
	else:
		response.write('You submitted an empty form.')

	return render_to_response('simple/show_chart.html', {'chart_urls': final_graphs, 'response': response})

def ff_count(friends, followers):
	friends_count = []
	followers_count = []
	friend_name = []

	for f in friends:
		friends_count.append(f.friends_count)
		followers_count.append(f.followers_count)
		name = f.name
		name = name.split( )
		friend_name.append(name[0])

	G = VerticalBarStack([ friends_count[:20],followers_count[:20] ], encoding='text')
	G.color('4F6900', 'BAF408')
	G.label(*friend_name[0:20])
	G.axes('y')
	G.axes.range(0,0,2000,200)
	G.scale(0,2000)
	G.bar(25, 25)
	G.marker('N*c*','black',0,-1,15)
	G.size(1000 , 275)
	G.title("My Friend's Friends : Follower Ratio")

	return str(G)

def ratio_chart(me):
	G = VerticalBarStack( [me.favourites_count, me.followers_count, me.friends_count, me.statuses_count])
	G.label('Favourites', 'Followers', 'Following', 'Statuses')
	G.color('44D1CC') 
	G.size(1000, 150)
	G.axes('y')
	G.axes.range(0,0,150,25)
	G.scale(0,150)
	G.bar(30,35)
	G.marker('N*c*','black',0,-1,20)
	G.title("My Life on Twitter")

	return str(G)


def create_profile(followers):
	year_count = {}
	count = 0

	for f in followers:
		year = f.created_at
		year = year.split()
		year = str(year[5])
		if(year in year_count):
			count = year_count[year]
		year_count.update({year : count+1})

	# year_count.sort()
	keys = year_count.keys()
	values = year_count.values()
	G = Line([values[:15]])
	G.label(*keys[0:15])
	G.color('76A4FB')
	G.line(2)
	G.marker('o', '0077CC',0,-1,5)
	G.marker('N*c*','black',0,-1,10)
	G.axes('y')
	G.axes.range(0,0,50,5)
	G.scale(0,50)
	G.size(1000 , 250)
	G.title("Years my Followers Created their Account")

	return str(G)

def friends_count(friends, followers):
	friends_count = []
	friend_name = []

	for f in friends:
		friends_count.append(f.friends_count)
		name = f.name
		name = name.split( )
		friend_name.append(name[0])

	G = Line([friends_count[:15]])
	G.label(*friend_name[0:15])
	G.color('76A4FB')
	G.line(2)
	G.marker('o', '0077CC',0,-1,5)
	G.marker('N*c*','black',0,-1,10)
	# G.axes.type('xy')
	# G.axes.label(0, 'Friends')
	# G.axes.label(1, 'Their friends')
	G.axes('y')
	G.axes.range(0,0,500,50)
	G.scale(0,500)
	G.size(1000 , 250)
	G.title("My Friend's Friends")

	return str(G)
