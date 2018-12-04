from django.conf.urls import url, include


from . import views

urlpatterns = [
	url(r'^$', views.athena, name='index'),
	url(r'^test/$', views.hera, name='hera'),	
	url(r'^about/$', views.about, name='about'),
	url(r'^archives/$', views.archives, name='archives'),	
	url(r'^node-dir/$', views.node_dir, name='node_dir_index'),
	url(r'^node-dir/(?P<node_dir_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.node_dir_part, name='node_dir'),
	url(r'^media_dir/$', views.media_dir, name='media_dir_index'),
	url(r'^media-org-directory/$', views.media_dir_athena, name='media_dir_test'),	
	url(r'^node/(?P<node_id>[0-9]+)/$', views.node, name='node'),
	url(r'^node/(?P<node_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.nodeslug, name='nodes with slugs'),
	url(r'^media_dir/(?P<media_org_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.media_org, name='media_org'),
	url(r'^blog/(?P<blog_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.blog, name='blog'),
	url(r'^in-depth/(?P<analysis_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.analysis, name='in-depth'),
	url(r'^journalist/(?P<journalist_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.journalist, name='journalist'),
	url(r'^issue/(?P<issue_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.political_issue, name='political issue'),	
]