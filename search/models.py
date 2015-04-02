from django.db import models
import webby

# Create your models here.
class Search(models.Model):
    trend = models.CharField(max_length=240)
    
    
    def __unicode__(self):
        return unicode(self.trend)
    

    def get_table(self, url):
        self.spider = webby.Crawler(url)
        self.parse = webby.Parser(self.spider.source)
        print self.spider
        print self.parse
        
    