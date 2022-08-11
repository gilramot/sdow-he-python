import pywikibot
import weblinkchecker

def main():
    startarticle = input()
    endarticle = input()
    site = pywikibot.Site("he", "wikipedia")
    page = pywikibot.Page(site, startarticle)
    item = pywikibot.ItemPage.fromPage(page)
    
    links1 = weblinkchecker.weblinks_from_text(startarticle)

    def get_links(links):
        a = set()
        for link in links:
            a.update(link)
    
    s = get_links(links1)

if __name__ == '__main__':
    main()
