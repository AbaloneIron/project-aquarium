import datetime
from django.db import models
from django.forms import ModelForm

FISH_CHOICES = (
    ('FF', 'Freshwater Fish'),
    ('FS', 'Freshwater Snails'),
    ('FC', 'Freshwater Crestations'),
    ('SF', 'Senior'),
)

class Aquarium(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    
    def __unicode__(self):
        return self.name
    
class Analysis(models.Model):
    aquarium = models.ForeignKey('Aquarium')
    ph = models.DecimalField(max_digits=3, decimal_places=1)
    ammonia = models.DecimalField(max_digits=3, decimal_places=2)
    nitrite = models.DecimalField(max_digits=3, decimal_places=0)
    nitrate = models.DecimalField(max_digits=3, decimal_places=0)
    temp = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    note = models.CharField(max_length=200, blank=True)
    #analysis_date = models.DateField(auto_now=False, auto_now_add=True)
    analysis_date = models.DateField()
    
    def __unicode__(self):
        #return self.analysis
        return u'%s - %s (%s)' % (self.id, self.analysis_date, self.aquarium)
        
    class Meta:
        verbose_name_plural='Analyses'
        
class Fish(models.Model):
    aquarium = models.ForeignKey('Aquarium')
    name = models.CharField(max_length=60, null=False)
    category = models.CharField(max_length=2)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    size = models.CharField(max_length=2)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)    
    
    def __unicode__(self):
        #return fish object descriptor
        return u'%s %s - %s' % (self.quantity, self.size, self.name)
    
    class Meta:
        verbose_name_plural='Fishes'
        
class FishForm(ModelForm):
    class Meta:
        model = Fish
        fields = ['category', 'name', 'quantity', 'size',]    
        
class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = ['ph', 'ammonia', 'nitrite', 'nitrate', 'temp', 'note', 'analysis_date']
        
class AquariumForm(ModelForm):
    class Meta:
        model = Aquarium
        fields = ['name', 'description', 'volume']