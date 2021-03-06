from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from django.template.defaulttags import register
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Q
from .models import Node, Media_Org, Perspective, Link, Node_Dir, Region, Journalist, Breaking_Link, About, Topic_Link, Headline, PoliticalBiasNews, Blog, Analysis, AnalLink, AnalPerspective, PoliticalIssue, STF, STF_Hub, STF_Link, Feature, Feature_Link


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)



def phoebe(request):
	nodes = Node.objects.all().order_by('-date_posted')[0:5]
	blogs= Blog.objects.all().order_by('-date_posted')[0:5]	
	breaking_links = Breaking_Link.objects.all()
	features = Feature_Link.objects.all()
	stfs= STF.objects.all().order_by('-date_updated') [0:5]

	return render(request, 'nodanews/index.html', {'nodes': nodes, 'blogs': blogs, 'breaking_links': breaking_links, 'stfs': stfs, 'features': features,})

def hera(request):
	headlines = Node.objects.all()[0:1]
	nodes = Node.objects.all().order_by('-date_posted')[1:5]
	blogs= Blog.objects.all().order_by('-date_posted')[0:5]	
	breaking_links = Breaking_Link.objects.all().exclude( region__id=9 ).exclude( region__id=10 )
	conservaturds = Breaking_Link.objects.filter( region__id=9 ).order_by('-posted')
	libtards = Breaking_Link.objects.filter( region__id=10 ).order_by('-posted') 	
	
	return render(request, 'nodanews/index.html', {'nodes': nodes, 'breaking_links': breaking_links, 'blogs': blogs, 'conservaturds': conservaturds, 'libtards': libtards, 'headlines': headlines})


def political_issue(request, slug, issue_id):
    issue = get_object_or_404(PoliticalIssue, pk=issue_id)
    issue_links = PoliticalBiasNews.objects.filter(issue__id = issue_id).order_by('-posted')
    return render(request, 'nodanews/issue.html', {'issue': issue, 'issue_links': issue_links})

def about(request):
    abouts = About.objects.all()
    return render(request, 'nodanews/about.html', {'abouts': abouts})

def node_dir(request):
    node_dir_topics = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    breaking_links = Breaking_Link.objects.all()
    node_dirs = Node_Dir.objects.order_by('name')
    nodes_by_dir = {
        n: Node.objects.filter(node_direc__id = n.id).order_by('-date_posted')[0:3] for n in node_dirs
    }
    return render(request, 'nodanews/node-dir.html', {'node_dirs': node_dirs, 'nodes_by_dir': nodes_by_dir, 'node_dir_topics': node_dir_topics, 'breaking_links': breaking_links})

def node_dir_part(request, node_dir_id , slug):
    node_dir = get_object_or_404(Node_Dir, pk=node_dir_id)
    nodes = Node.objects.filter(node_direc__id = node_dir_id)
    stfs = STF.objects.filter(node_dir__id = node_dir_id)
    return render(request, 'nodanews/node-dir_part.html', {'nodes': nodes, 'node_dir': node_dir, 'stfs': stfs})	

def media_dir_athena(request):
	medias = Media_Org.objects.all()
	return render(request, 'nodanews/media-org-directory.html', {'medias': medias})

def archives(request):
    node_dirs = Node_Dir.objects.order_by('name')
    blogs = Blog.objects.all().order_by("-date_posted")
    indepths = Analysis.objects.all().order_by("-date_posted")
    issues = PoliticalIssue.objects.all().order_by("-id")
    nodes_by_dir = {
        n: Node.objects.filter(node_direc__id = n.id).order_by('-date_posted') for n in node_dirs
    }    
    return render(request, 'nodanews/archives.html', {'node_dirs': node_dirs, 'blogs': blogs, 'indepths': indepths, 'issues': issues, 'nodes_by_dir': nodes_by_dir})



def node(request, node_id):
    node = get_object_or_404(Node, pk=node_id)
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    assnodes = Node.objects.filter( node_direc__id = node.node_direc_id)
    perspectives = Perspective.objects.filter( node__id = node_id )
    perspective_links = {
		p: Link.objects.filter(perspective__id = p.id) for p in perspectives
	}
    return render(request, 'nodanews/node.html', {'node': node, 'perspectives': perspective_links, 'node_dirs': node_dirs, 'assnodes': assnodes})

def nodeslug(request, slug, node_id):
    node = get_object_or_404(Node, pk=node_id)
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    assnodes = Node.objects.filter( node_direc__id = node.node_direc_id)
    perspectives = Perspective.objects.filter( node__id = node_id )
    perspective_links = {
		p: Link.objects.filter(perspective__id = p.id) for p in perspectives
	}
    return render(request, 'nodanews/node.html', {'node': node, 'perspectives': perspective_links, 'node_dirs': node_dirs, 'assnodes': assnodes})

def stf_hub(request, slug, stf_hub_id):
	stf_hub = get_object_or_404(STF_Hub, pk=stf_hub_id)
	stfs = STF.objects.filter( hub__id = stf_hub_id)[0:7]
	stf_links = {
		p: STF_Link.objects.filter(story__id = p.id) for p in stfs
	}	
	return render(request, 'nodanews/hub.html', {'stf_hub': stf_hub, 'stfs': stf_links})

def stf_hubx(request, slug, stf_hub_id):
	stf_hub = get_object_or_404(STF_Hub, pk=stf_hub_id)
	stfs = STF.objects.filter( hub__id = stf_hub_id)
	stf_links = {
		p: STF_Link.objects.filter(story__id = p.id) for p in stfs
	}	
	return render(request, 'nodanews/hubx.html', {'stf_hub': stf_hub, 'stfs': stf_links})	

def stf(request, slug, stf_id):
	stf = get_object_or_404(STF, pk=stf_id)
	stf_links = STF_Link.objects.filter( story__id = stf_id)
	return render(request, 'nodanews/story.html', {'stf': stf, 'stf_links': stf_links})
	
def analysis(request, slug, analysis_id):
    analysis = get_object_or_404(Analysis, pk=analysis_id)
    perspectives = AnalPerspective.objects.filter( article__id = analysis_id )
    perspective_links = {
		p: AnalLink.objects.filter(perspective__id = p.id) for p in perspectives
	}
    return render(request, 'nodanews/in-depth.html', {'analysis': analysis, 'perspectives': perspective_links})
    
def blog(request, slug, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'nodanews/blog.html', {'blog': blog})
	

def media_org(request, slug, media_org_id):
    media_org = get_object_or_404(Media_Org, pk=media_org_id)
    journalists = Journalist.objects.filter( organization__id = media_org_id )
    return render(request, 'nodanews/media_org.html', {'media_org': media_org, 'journalists': journalists,})	

def journalist(request, slug, journalist_id):
	journalist = get_object_or_404(Journalist, pk=journalist_id)
	return render(request, 'nodanews/journalist.html', {'journalist': journalist})
	
	
	########################## DEPRECATED ###################
def athena(request):
	headlines = Headline.objects.all()
	breaking_links = Breaking_Link.objects.all()
	topics = Node_Dir.objects.filter(active=True).order_by('-date_updated')	
	topics_by_dir = {
        n: Topic_Link.objects.filter(node_dir__id = n.id).order_by('-posted')[0:5] for n in topics
    }	
	return render(request, 'nodanews/athena.html', {'headlines': headlines, 'breaking_links': breaking_links, 'topics': topics, 'topics_by_dir': topics_by_dir})

def diana(request):
	return render (request, 'nodanews/index.html')
#def diana(request):
#	issues = PoliticalIssue.objects.all()[0:3]
#	opeds = Breaking_Link.objects.filter( region__id=8 )
#	breaking_links = Breaking_Link.objects.all().exclude( region__id=8 )
#	headlines = Headline.objects.all()
#	conservaturds = PoliticalBiasNews.objects.filter( region__id=9 ).order_by('-posted')
#	libtards = PoliticalBiasNews.objects.filter( region__id=10 ).order_by('-posted')    
#	videos = LiveVideo.objects.filter( region__id=8 )
#	indepths = Analysis.objects.all()[0:4]
#	blogs = Blog.objects.all()[0:5]
#	recents = Node.objects.all()[1:4]
#	issue_links = {
 #       n: PoliticalBiasNews.objects.filter(issue__id = n.id).order_by('-posted') for n in issues
    #}
#	return render(request, 'nodanews/index.html', {'recents': recents, 'issues': issues, 'issue_links': issue_links, 'opeds': opeds, 'conservaturds': conservaturds, 'headlines': headlines, 'libtards': libtards, 'breaking_links': breaking_links, 'blogs': blogs, 'indepths': indepths})


#def cassandra(request):
 #   opeds = Node.objects.all()[3:8]
  #  nodes = Node.objects.all()[0:3]
   # headlines = Headline.objects.all()
#    conservaturds = PoliticalBiasNews.objects.filter( region__id=9 ).order_by('-posted')
 #   libtards = PoliticalBiasNews.objects.filter( region__id=10 ).order_by('-posted')    
# #   videos = LiveVideo.objects.filter( region__id=8 )
  #  asias = Breaking_Link.objects.filter( region__id=1 ).order_by('-posted')
   # africas = Breaking_Link.objects.filter( region__id=3 ).order_by('-posted')
    #sasias = Breaking_Link.objects.filter( region__id=6 ).order_by('-posted')
#    mes = Breaking_Link.objects.filter( region__id=7 ).order_by('-posted')
 #   namericas = Breaking_Link.objects.filter( region__id=4 ).order_by('-posted')
  #  samericas = Breaking_Link.objects.filter( region__id=5 ).order_by('-posted')
   # europes = Breaking_Link.objects.filter( region__id=2 ).order_by('-posted')
 #   latests = Breaking_Link.objects.all()[0:20]
#    return render(request, 'nodanews/cassandra.html', {'opeds': opeds, 'conservaturds': conservaturds, 'nodes': nodes, 'asias': asias, 'latests': latests, 'headlines': headlines, 'africas': africas, 'sasias': sasias, 'mes': mes, 'namericas': namericas, 'samericas': samericas, 'libtards': libtards, 'europes': europes})

#def node_new(request, slug, node_id):
 #   node = get_object_or_404(Node, pk=node_id)
#    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
#    assnodes = Node.objects.filter( node_direc__id = node.node_direc_id)
#    perspectives = Perspective.objects.filter( node__id = node_id )
#    perspective_links = {
#		p: Link.objects.filter(perspective__id = p.id) for p in perspectives
#	}
 #   return render(request, 'nodanews/node_new.html', {'node': node, 'perspectives': perspective_links, 'node_dirs': node_dirs, 'assnodes': assnodes})
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

	
	