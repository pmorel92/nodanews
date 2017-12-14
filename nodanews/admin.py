from django.contrib import admin

from .models import Node, Media_Org, Link, Perspective, Node_Dir, Region, Journalist, Breaking_Link, Political_Lean, Media_Character, About, LiveVideo, Breaking_Category


class Media_OrgAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'country', 'ready', 'political_lean', 'media_character', 'region']
    search_fields = ['name']


class NodeAdmin(admin.ModelAdmin):
    
    list_display = ['headline', 'hotness', 'region', 'node_direc', 'date_posted', 'editorial', 'analysis', 'category']


class LinkAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'media', 'perspective']

class JournalistAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'organization']
    search_fields = ['organization']
    
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']

class Node_DirAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_updated', 'active']

class Breaking_LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'media', 'region', 'posted', 'category']
    date_hierarchy = 'posted'

admin.site.register(Node, NodeAdmin)
admin.site.register(Node_Dir, Node_DirAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Perspective)
admin.site.register(Political_Lean)
admin.site.register(About)
admin.site.register(LiveVideo)
admin.site.register(Media_Character)
admin.site.register(Journalist, JournalistAdmin)
admin.site.register(Media_Org, Media_OrgAdmin)
admin.site.register(Breaking_Link, Breaking_LinkAdmin)
admin.site.register(Breaking_Category)