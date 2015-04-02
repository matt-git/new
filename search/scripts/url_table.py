from search import models
import webby

def run(*args):
    try:
        
        spider = webby.Crawler(args[0])
        parse = webby.Parser(spider.source)
        print parse
        print spider.directory
        print spider.get_url()
        
    except ValueError:
        print "I was thrown"
    
    