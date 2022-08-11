from collections import OrderedDict
import pywikibot
import csv
import main.weblinkchecker as weblinkchecker

def main():
    startarticle = input()
    endarticle = input()
    site = pywikibot.Site("he", "wikipedia")
    page = pywikibot.Page(site, startarticle)
    item = pywikibot.ItemPage.fromPage(page)
    
    weblinkchecker.weblinks_from_text(startarticle)
    g-=gen()


if __name__ == '__main__':
    main()
