from django.db import models
from datetime import datetime
from django.db.models.aggregates import Count
from random import randint

class Node_Dir(models.Model):
    name = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=False)
    date_updated = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(default=' ')
    banner = models.ImageField(upload_to='media/nodes', default='', blank=True)
    related = models.ManyToManyField("self", blank=True)

    def __str__(self):
	    return self.name

    
    class Meta:
	    ordering = ('name',)   
	    
class Region(models.Model):
    name = models.CharField(max_length=100, default='')
    color = models.CharField(max_length=100, default='')
    
    def __str__(self):
	    return self.name
    class Meta:
	    ordering = ('name',)    

    		
class Node(models.Model):
    headline = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField()
    my_take = models.TextField()
    head_image = models.ImageField(upload_to='media/nodes', default='')
    foot_image = models.ImageField(upload_to='media/nodes', default='')
    video_embed1 = models.CharField(max_length=500, default='', blank=True)
    video_embed2 = models.CharField(max_length=500, default='', blank=True)
    video_embed3 = models.CharField(max_length=500, default='', blank=True)    
    node_direc = models.ForeignKey(Node_Dir)
    region = models.ForeignKey(Region, default=1, null=True)

    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def __str__(self):
        return "{}/{}".format(self.headline, self.country)
    class Meta:
        ordering = ('-date_posted',)

class Blog(models.Model):
    headline = models.CharField(max_length=200, default='')
    date_posted = models.DateField()
    head_image = models.ImageField(upload_to='media/nodes', default='')
    text = models.TextField()
    slug = models.SlugField(max_length=200, default=' ')    
    def __str__(self):
        return "{}".format(self.headline)
    class Meta:
        ordering = ('-date_posted',)
        
class Analysis(models.Model):
    headline = models.CharField(max_length=200, default='')
    date_posted = models.DateField()
    head_image = models.ImageField(upload_to='media/nodes', default='')
    summary = models.TextField()
    text1 = models.TextField()
    second_image = models.ImageField(upload_to='media/nodes', default='')
    text2 = models.TextField()
    pop_out_quote = models.TextField()
    video_embed1 = models.CharField(max_length=500, default='', blank=True)
    video_embed2 = models.CharField(max_length=500, default='', blank=True)
    video_embed3 = models.CharField(max_length=500, default='', blank=True)    
    node_direc = models.ForeignKey(Node_Dir)
    slug = models.SlugField(max_length=200, default=' ') 
    def __str__(self):
        return "{}".format(self.headline)
    class Meta:
        ordering = ('-date_posted',)

class AnalPerspective(models.Model):
    name = models.CharField(max_length=47, default='')
    article = models.ForeignKey(Analysis)
    
    def __str__(self):
	    return "{}/{}".format(self.article, self.name)
    class Meta:
	    ordering = ('-id',)


class Perspective(models.Model):
    name = models.CharField(max_length=47, default='')
    node = models.ForeignKey(Node)
    
    def __str__(self):
	    return "{}/{}".format(self.node, self.name)
    class Meta:
	    ordering = ('-id',)
	    
class Political_Lean(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Media_Character(models.Model):
    name = models.CharField(max_length=100)
	
    def __str__(self):
        return self.name


class Media_Org(models.Model):
    name = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField()
    home_page = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=100, default='')
    region = models.ForeignKey(Region, default=1, null=True)
    date_founded = models.DateField(default='1956-02-27')
    logo = models.ImageField(upload_to='media/logos')
    description = models.TextField()
    ready = models.BooleanField(default=False)
    political_lean = models.ForeignKey(Political_Lean, default=1, null=True)
    media_character = models.ForeignKey(Media_Character, default=1, null=True)
    slug = models.SlugField(max_length=100, default=' ')

	
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
	    
class Journalist(models.Model):
	name = models.CharField(max_length=200, default='')
	contact = models.CharField(max_length=200, default='')
	organization = models.ForeignKey(Media_Org)
	bio = models.TextField(default='bio goes here')
	picture = models.ImageField(upload_to='media/logos', default=" ")
    
	def __str__(self):
		return self.name
	class Meta:
		ordering = ('name',)
		
class Headline(models.Model):
	url = models.CharField(max_length=300, default=' ')
	title = models.CharField(max_length=150, default=' ')
	image = models.ImageField(upload_to='media/temp', default='')
	banner = models.BooleanField(default=False)

class Link(models.Model):
	url = models.CharField(max_length=300, default='', blank=True)
	title = models.CharField(max_length=150, default='', blank=True)
	media = models.ForeignKey(Media_Org)
	perspective = models.ForeignKey(Perspective)
	
	def __str__(self):
	    return "{}/{}".format(self.id, self.perspective)

class AnalLink(models.Model):
	url = models.CharField(max_length=300, default='', blank=True)
	title = models.CharField(max_length=150, default='', blank=True)
	media = models.ForeignKey(Media_Org)
	perspective = models.ForeignKey(AnalPerspective)
	
	def __str__(self):
	    return "{}/{}".format(self.id, self.perspective)

class Breaking_Link(models.Model):
	url = models.CharField(max_length=300, default='')
	title = models.CharField(max_length=150, default='')
	media = models.ForeignKey(Media_Org)
	posted = models.DateTimeField(default=datetime.now, blank=True)
	region = models.ForeignKey(Region, default=8, null=True)
	imageQ = models.BooleanField(default=False)
	image = models.ImageField(upload_to='media/temp', default='', blank=True)

	def __str__(self):
	    return "{}/{}".format(self.id, self.media)

	class Meta:
		ordering = ('-posted',)

class PoliticalBiasNews(models.Model):
	url = models.CharField(max_length=300, default='')
	title = models.CharField(max_length=150, default='')
	media = models.ForeignKey(Media_Org)
	posted = models.DateTimeField(default=datetime.now, blank=True)
	region = models.ForeignKey(Region, default=9, null=True)
	def __str__(self):
	    return "{}/{}".format(self.id, self.media)

	class Meta:
		ordering = ('-posted',)

    
	    
class About(models.Model):
    description = models.TextField()

class LiveVideo(models.Model):
    name1 = models.CharField(max_length=200, default='name goes here')
    video1 = models.CharField(max_length=500, default='', blank=True)
    name2 = models.CharField(max_length=200, default='name goes here')
    video2 = models.CharField(max_length=500, default='', blank=True)
    name3 = models.CharField(max_length=200, default='name goes here')
    video3 = models.CharField(max_length=500, default='', blank=True)
    region = models.ForeignKey(Region, default=8, null=True)

    
    def __str__(self):
	    return "{}".format(self.region.name)
