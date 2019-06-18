from django.db import models
from datetime import datetime
from django.db.models.aggregates import Count

class Headline(models.Model):
    url = models.CharField(max_length=300, default=' ')
    title = models.CharField(max_length=150, default=' ')
    image = models.ImageField(upload_to='media/temp', default='')

class Region(models.Model):
    name = models.CharField(max_length=100, default='')
    color = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)    

class Node_Dir(models.Model):
    name = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=False)
    date_updated = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(default=' ')
    region = models.ForeignKey(
        'Region',
        default=8,
        null=True,
        on_delete=models.PROTECT,)
    banner = models.ImageField(upload_to='media/nodes', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')    
   



    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ('name',)

class STF_Hub(models.Model):
    name = models.CharField(max_length=100, default='')
    banner = models.ImageField(upload_to='media/nodes')
    credit = models.CharField(max_length=200, default='')     
    date_updated = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(default='', blank=True)
    node_dir = models.ForeignKey(
        'Node_Dir',
        on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return self.name

class Node(models.Model):
    headline = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=100, default='')
    date_posted = models.DateField()
    lead = models.TextField(default='')
    head_image = models.ImageField(upload_to='media/nodes', default='')
    credit1 = models.CharField(max_length=200, default='')        
    my_take = models.TextField()
    video_embed1 = models.CharField(max_length=500, default='', blank=True)    
    my_take2 = models.TextField(default='')
    video_embed2 = models.CharField(max_length=500, default='', blank=True)    
    foot_image = models.ImageField(upload_to='media/nodes', default='')
    credit2 = models.CharField(max_length=200, default='')    
    video_embed3 = models.CharField(max_length=500, default='', blank=True)    
    node_direc = models.ForeignKey(
        'Node_Dir',
        on_delete=models.PROTECT,)
    region = models.ForeignKey('Region',
    default=1,
    null=True,
    on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return "{}/{}".format(self.headline, self.country)
    class Meta:
        ordering = ('-date_posted',)

class Perspective(models.Model):
    name = models.CharField(max_length=47, default='')
    node = models.ForeignKey(
        'Node',
        on_delete=models.CASCADE,)
    
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
    region = models.ForeignKey('Region',
    default=1,
    null=True,
    on_delete=models.PROTECT,)
    date_founded = models.DateField(default='1956-02-27')
    logo = models.ImageField(upload_to='media/logos')
    description = models.TextField()
    ready = models.BooleanField(default=False)
    political_lean = models.ForeignKey(
        'Political_Lean',
        default=1,
        null=True,
        on_delete=models.PROTECT,)
    media_character = models.ForeignKey(
        'Media_Character',
        default=1,
        null=True,
        on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=100, default=' ')

    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        
class STF(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/nodes', default='')
    credit = models.CharField(max_length=200, default='')     
    update = models.TextField()
    date_updated = models.DateTimeField()
    videoQ = models.BooleanField(default=False)
    video = models.CharField(max_length=500, default='', blank=True) 
    STF_Hub= models.ForeignKey(
        'STF_Hub',
        on_delete=models.PROTECT)
    node_dir = models.ForeignKey(
        'Node_Dir',
        on_delete=models.PROTECT,)

    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return "{}/{}".format(self.headline, self.STF_Hub)

class Journalist(models.Model):
    name = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=200, default='')
    organization = models.ForeignKey(
        'Media_Org',
        on_delete=models.PROTECT,)
    bio = models.TextField(default='bio goes here')
    picture = models.ImageField(upload_to='media/logos', default=" ")
    slug = models.SlugField(max_length=100, default=' ')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        
class Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    perspective = models.ForeignKey(
        'Perspective',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.id, self.perspective)

class STF_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    STF = models.ForeignKey(
        'STF',
        on_delete=models.CASCADE,)
    def __str__(self):
        return "{}/{}".format(self.id, self.STF)

class Topic_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    posted = models.DateTimeField(default=datetime.now, blank=True)
    region = models.ForeignKey(
        'Region',
        default=8,
        null=True,
        on_delete=models.PROTECT,)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    node_dir = models.ForeignKey(
        'Node_Dir',
        on_delete=models.CASCADE,)
    journalist = models.ForeignKey('Journalist',
    null=True,
    blank=True,
    on_delete=models.PROTECT,)	
    def __str__(self):
        return "{}/{}".format(self.id, self.node_dir.name)



class Breaking_Link(models.Model):
    url = models.CharField(max_length=300, default='')
    title = models.CharField(max_length=150, default='')
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    posted = models.DateTimeField(default=datetime.now, blank=True)
    region = models.ForeignKey(
        'Region',
        default=8,
        null=True,
        on_delete=models.PROTECT,)
    journalist = models.ForeignKey('Journalist',
    null=True,
    blank=True,
    on_delete=models.PROTECT,)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/temp', default='', blank=True)

    def __str__(self):
        return "{}/{}".format(self.id, self.media)

    class Meta:
        ordering = ('-posted',)

    
        
class About(models.Model):
    description = models.TextField()


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

############################### Old Stuff Below ######################################
        
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
    node_direc = models.ForeignKey(
        'Node_Dir',
        on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=200, default=' ') 
    def __str__(self):
        return "{}".format(self.headline)
    class Meta:
        ordering = ('-date_posted',)

class AnalPerspective(models.Model):
    name = models.CharField(max_length=47, default='')
    article = models.ForeignKey(
        'Analysis',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.article, self.name)
    class Meta:
        ordering = ('-id',)

class PoliticalIssue(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="description goes here")
    head_image = models.ImageField(upload_to='media/nodes', default='')
    slug = models.SlugField(max_length=100, default=' ')    
    def __str__(self):
        return "{}".format(self.name)
    class Meta:
        ordering = ('-id',)

class PoliticalBiasNews(models.Model):
    url = models.CharField(max_length=300, default='')
    title = models.CharField(max_length=150, default='')
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    posted = models.DateTimeField(default=datetime.now, blank=True)
    region = models.ForeignKey(
        'Region',
        default=9,
        null=True,
        on_delete=models.CASCADE,)
    conservative = models.BooleanField(default=False)
    liberal = models.BooleanField(default=True)
    issue = models.ForeignKey(
        'PoliticalIssue',
        default=1,
        on_delete=models.CASCADE,)	
    def __str__(self):
        return "{}/{}".format(self.id, self.issue.name)

    class Meta:
        ordering = ('-posted',)

class AnalLink(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    media = models.ForeignKey('Media_Org',
    blank=True,
    null=True,
    on_delete=models.CASCADE,)
    academic = models.BooleanField(default=False)
    author = models.ForeignKey(
        'Journalist',
        null=True,
        blank=True,
        on_delete=models.CASCADE,)
    perspective = models.ForeignKey(
        'AnalPerspective',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.id, self.perspective)
