from collections import OrderedDict
import pywikibot
import csv

def main():
    startarticle = input()
    endarticle = input()
    site = pywikibot.Site("he", "wikipedia")
    page = pywikibot.Page(site, startarticle)
    item = pywikibot.ItemPage.fromPage(page)
    
    print("works!")


if __name__ == '__main__':
    main()
