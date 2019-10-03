from django.contrib import admin

from .models import Node, Media_Org, Link, Perspective, Node_Dir, Region, Journalist, Breaking_Link, Political_Lean, Media_Character, About, Topic_Link, Headline, PoliticalBiasNews, Blog, Analysis, AnalLink, AnalPerspective, PoliticalIssue, STF, STF_Hub, STF_Link, Feature, Feature_Link


class Media_OrgAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'country', 'ready', 'slug', 'region']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}

class NodeAdmin(admin.ModelAdmin):
    
    list_display = ['headline', 'region', 'node_direc', 'date_posted']

class LinkAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'media', 'perspective']

class AnalLinkAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'media', 'perspective']

class JournalistAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'organization']
    search_fields = ['organization']
    
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']

class Node_DirAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_updated', 'active']

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ['headline', 'date_posted', 'node_direc']

class Breaking_LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'media', 'posted', 'imageQ']
    date_hierarchy = 'posted'

class Topic_LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'media', 'region', 'posted', 'node_dir']
    date_hierarchy = 'posted'

class PoliticalBiasNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'media', 'conservative', 'liberal', 'posted']
    date_hierarchy = 'posted'

class BlogAdmin(admin.ModelAdmin):
    list_display = ['headline', 'date_posted']

class STF_HubAdmin(admin.ModelAdmin):
    list_display = ['name', 'node_dir', 'date_updated']

class STFAdmin(admin.ModelAdmin):
    list_display = ['headline', 'hub', 'date_updated']

class STF_LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'media', 'story']

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name']

class Feature_LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'media', 'posted', 'feature']
    

admin.site.register(Node, NodeAdmin)
admin.site.register(Node_Dir, Node_DirAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Perspective)
admin.site.register(Political_Lean)
admin.site.register(About)
admin.site.register(Topic_Link, Topic_LinkAdmin)
admin.site.register(Media_Character)
admin.site.register(Journalist, JournalistAdmin)
admin.site.register(Media_Org, Media_OrgAdmin)
admin.site.register(Breaking_Link, Breaking_LinkAdmin)
admin.site.register(Headline)
admin.site.register(PoliticalBiasNews, PoliticalBiasNewsAdmin)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(AnalLink, AnalLinkAdmin)
admin.site.register(AnalPerspective)
admin.site.register(Blog, BlogAdmin)
admin.site.register(PoliticalIssue)
admin.site.register(STF, STFAdmin)
admin.site.register(STF_Link, STF_LinkAdmin)
admin.site.register(STF_Hub, STF_HubAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Feature_Link, Feature_LinkAdmin)