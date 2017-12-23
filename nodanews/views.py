from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from django.template.defaulttags import register
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import F, Q
from .models import Node, Media_Org, Perspective, Link, Node_Dir, Region, Journalist, Breaking_Link, About, LiveVideo, Breaking_Category


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	livevideos = LiveVideo.objects.filter( region__id=8 )
	nodes_by_dir = {
		n: Node.objects.filter(node_direc__id = n.id).order_by('-date_posted')[0:1] for n in node_dirs
	}
	return render(request, 'nodanews/index.html', {'nodes_by_dir': nodes_by_dir, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})		

def index_asia(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.filter( region__id=1 ).order_by('-posted')
	livevideos = LiveVideo.objects.filter( region__id=1 )
	nodes = Node.objects.filter( region__id=1 ).order_by('-date_posted')
	return render(request, 'nodanews/blue.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})

def index_africa(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	nodes = Node.objects.filter( region__id=3 ).order_by('-date_posted')
	breaking_links = Breaking_Link.objects.filter( region__id=3 ).order_by('-posted')
	livevideos = LiveVideo.objects.filter( region__id=3 )
	return render(request, 'nodanews/green.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})
	
def index_sasia(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	nodes = Node.objects.filter( region__id=6 ).order_by('-date_posted')
	breaking_links = Breaking_Link.objects.filter( region__id=6 ).order_by('-posted')
	livevideos = LiveVideo.objects.filter( region__id=6 )
	return render(request, 'nodanews/cyan.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})
	
def index_me(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	nodes = Node.objects.filter( region__id=7 ).order_by('-date_posted')
	breaking_links = Breaking_Link.objects.filter( region__id=7 ).order_by('-posted')
	livevideos = LiveVideo.objects.filter( region__id=7 )
	return render(request, 'nodanews/purple.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})
	
def index_namerica(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	nodes = Node.objects.filter( region__id=4 ).order_by('-date_posted')
	breaking_links = Breaking_Link.objects.filter( region__id=4 ).order_by('-posted')
	livevideos = LiveVideo.objects.filter( region__id=4 )
	return render(request, 'nodanews/orange.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})
	
def index_samerica(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')	
	nodes = Node.objects.filter( region__id=5 ).order_by('-date_posted')
	breaking_links = Breaking_Link.objects.filter( region__id=5 ).order_by('-posted')
	livevideos = LiveVideo.objects.filter( region__id=5 )
	return render(request, 'nodanews/yellow.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})
	
def index_europe(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')	
	nodes = Node.objects.filter( region__id=2 ).order_by('-date_posted')
	breaking_links = Breaking_Link.objects.filter( region__id=2 ).order_by('-posted')
	livevideos = LiveVideo.objects.filter( region__id=2 )
	return render(request, 'nodanews/red.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})

def index_editorials(request):
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')	
    nodes = Node.objects.filter( editorial=True).order_by('-date_posted')
    breaking_links = Breaking_Link.objects.all()
    livevideos = LiveVideo.objects.filter( region__id=8 )
    return render(request, 'nodanews/editorials.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos})
    
def index_analysis(request):
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')	
    nodes = Node.objects.filter( analysis=True).order_by('-date_posted')
    breaking_links = Breaking_Link.objects.all()
    livevideos = LiveVideo.objects.filter( region__id=8 )
    return render(request, 'nodanews/analysis.html', {'nodes': nodes, 'node_dirs': node_dirs, 'breaking_links': breaking_links, 'livevideos': livevideos}) 
    
def about(request):
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    breaking_links = Breaking_Link.objects.all()
    abouts = About.objects.all()
    return render(request, 'nodanews/about.html', {'node_dirs': node_dirs, 'breaking_links': breaking_links, 'abouts': abouts})

def node_dir(request):
    node_dir_topics = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    breaking_links = Breaking_Link.objects.all()
    node_dirs = Node_Dir.objects.order_by('name')
    nodes_by_dir = {
        n: Node.objects.filter(node_direc__id = n.id).order_by('-date_posted')[0:3] for n in node_dirs
    }
    return render(request, 'nodanews/node-dir.html', {'node_dirs': node_dirs, 'nodes_by_dir': nodes_by_dir, 'node_dir_topics': node_dir_topics, 'breaking_links': breaking_links})

def node_dir_part(request, node_dir_id):
    node_dirs = get_object_or_404(Node_Dir, pk=node_dir_id)
    breaking_links = Breaking_Link.objects.all()
    asswebs = Breaking_Link.objects.filter( category__id = node_dir_part.category_id)    
    node_dir_topics = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    nodes = Node.objects.filter(node_direc__id = node_dir_id)
    return render(request, 'nodanews/node-dir_part.html', {'nodes': nodes, 'asswebs': asswebs, 'node_dirs': node_dirs, 'node_dir_topics': node_dir_topics, 'breaking_links': breaking_links})	

def media_dir(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.order_by('name')
	return render(request, 'nodanews/media_dir.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_africa(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(region__id =3 ).order_by('name')
	return render(request, 'nodanews/media_dir/africa.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_asia(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(region__id =1 ).order_by('name')
	return render(request, 'nodanews/media_dir/asia.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_europe(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(region__id =2 ).order_by('name')
	return render(request, 'nodanews/media_dir/europe.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_namerica(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(region__id =4 ).order_by('name')
	return render(request, 'nodanews/media_dir/namerica.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_samerica(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(region__id =5 ).order_by('name')
	return render(request, 'nodanews/media_dir/samerica.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_me(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(region__id =7 ).order_by('name')
	return render(request, 'nodanews/media_dir/me.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_sasia(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(region__id =6 ).order_by('name')
	return render(request, 'nodanews/media_dir/sasia.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_farleft(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(political_lean__id =5 ).order_by('name')
	return render(request, 'nodanews/media_dir/farleft.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_farright(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(political_lean__id =4 ).order_by('name')
	return render(request, 'nodanews/media_dir/farright.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_moderate(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(political_lean__id =3 ).order_by('name')
	return render(request, 'nodanews/media_dir/moderate.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})


def media_dir_conservative(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(political_lean__id =2 ).order_by('name')
	return render(request, 'nodanews/media_dir/conservative.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_liberal(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(political_lean__id =1 ).order_by('name')
	return render(request, 'nodanews/media_dir/liberal.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_independent(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(media_character__id =4 ).order_by('name')
	return render(request, 'nodanews/media_dir/independent.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_stateowned(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(media_character__id =3 ).order_by('name')
	return render(request, 'nodanews/media_dir/stateowned.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_globalist(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(media_character__id =2 ).order_by('name')
	return render(request, 'nodanews/media_dir/globalist.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})

def media_dir_nationalist(request):
	node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
	breaking_links = Breaking_Link.objects.all()
	media_orgs = Media_Org.objects.filter(media_character__id =1 ).order_by('name')
	return render(request, 'nodanews/media_dir/nationalist.html', {'media_orgs': media_orgs, 'node_dirs': node_dirs, 'breaking_links': breaking_links})


def node(request, node_id):
    node = get_object_or_404(Node, pk=node_id)
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    asswebs = Breaking_Link.objects.filter( category__id = node.category_id)
    assnodes = Node.objects.filter( node_direc__id = node.node_direc_id)
    perspectives = Perspective.objects.filter( node__id = node_id )
    perspective_links = {
		p: Link.objects.filter(perspective__id = p.id) for p in perspectives
	}
    return render(request, 'nodanews/node.html', {'node': node, 'perspectives': perspective_links, 'node_dirs': node_dirs, 'asswebs': asswebs, 'assnodes': assnodes})


def media_org(request, media_org_id):
    media_org = get_object_or_404(Media_Org, pk=media_org_id)
    breaking_links = Breaking_Link.objects.all()
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')	
    journalists = Journalist.objects.filter( organization__id = media_org_id )
    return render(request, 'nodanews/media_org.html', {'media_org': media_org, 'journalists': journalists, 'node_dirs': node_dirs, 'breaking_links': breaking_links})	