from django.conf.urls import url, include


from . import views

urlpatterns = [
	url(r'^$', views.cassandra, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^node-dir/$', views.node_dir, name='node_dir_index'),
	url(r'^node-dir/(?P<node_dir_id>[0-9]+)/$', views.node_dir_part, name='node_dir'),
	url(r'^media_dir/$', views.media_dir, name='media_dir_index'),
	url(r'^media_dir/africa/$', views.media_dir_africa, name='media_dir_africa'),
	url(r'^media_dir/asia/$', views.media_dir_asia, name='media_dir_asia'),
	url(r'^media_dir/europe/$', views.media_dir_europe, name='media_dir_europe'),
	url(r'^media_dir/me/$', views.media_dir_me, name='media_dir_me'),
	url(r'^media_dir/namerica/$', views.media_dir_namerica, name='media_dir_namerica'),
	url(r'^media_dir/samerica/$', views.media_dir_samerica, name='media_dir_samerica'),
	url(r'^media_dir/sasia/$', views.media_dir_sasia, name='media_dir_sasia'),
	url(r'^media_dir/independent/$', views.media_dir_independent, name='media_dir_independent'),
	url(r'^media_dir/stateowned/$', views.media_dir_stateowned, name='media_dir_stateowned'),
	url(r'^media_dir/globalist/$', views.media_dir_globalist, name='media_dir_globalist'),
	url(r'^media_dir/nationalist/$', views.media_dir_nationalist, name='media_dir_nationalist'),
	url(r'^media_dir/farright/$', views.media_dir_farright, name='media_dir_farright'),
	url(r'^media_dir/farleft/$', views.media_dir_farleft, name='media_dir_farleft'),
	url(r'^media_dir/moderate/$', views.media_dir_moderate, name='media_dir_moderate'),
	url(r'^media_dir/conservative/$', views.media_dir_conservative, name='media_dir_conservative'),
	url(r'^media_dir/liberal/$', views.media_dir_liberal, name='media_dir_liberal'),	
	url(r'^node/(?P<node_id>[0-9]+)/$', views.node, name='node'),
	url(r'^media_dir/(?P<media_org_id>[0-9]+)/$', views.media_org, name='media_org'),
	url(r'^blog/(?P<slug>[\w-]+)/$', views.blog, name='blog'),
	url(r'^blog-list/$', views.blog_list, name='blog_list'),
	url(r'^in-depth/(?P<slug>[\w-]+)/$', views.analysis, name='in-depth'),	
]