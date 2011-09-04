from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tracker.views',
	url(r'^(?P<db>(\w+/|))challenges/$', 'challengeindex'),
	url(r'^(?P<db>(\w+/|))challenge/(?P<id>-?\d+)/$', 'challenge'),
	url(r'^(?P<db>(\w+/|))choices/$', 'choiceindex'),
	url(r'^(?P<db>(\w+/|))choice/(?P<id>-?\d+)/$', 'choice'),
	url(r'^(?P<db>(\w+/|))choiceoption/(?P<id>-?\d+)/$', 'choiceoption'),
	url(r'^(?P<db>(\w+/|))donors/$', 'donorindex'),
	url(r'^(?P<db>(\w+/|))donor/(?P<id>-?\d+)/$', 'donor'),
	url(r'^(?P<db>(\w+/|))donations/$', 'donationindex'),
	url(r'^(?P<db>(\w+/|))donation/(?P<id>-?\d+)/$', 'donation'),
	url(r'^(?P<db>(\w+/|))games/$', 'gameindex'),
	url(r'^(?P<db>(\w+/|))game/(?P<id>-?\d+)/$', 'game'),
	url(r'^(?P<db>(\w+/|))prizes/$', 'prizeindex'),
	url(r'^dbs/$', 'dbindex'),
	url(r'^(?P<db>(\w+/|))$', 'index'),
	url(r'^$', 'index'),
)
