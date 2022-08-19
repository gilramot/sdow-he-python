from gettext import find
import wikipediaapi
startarticle = ''
endarticle = ''
wiki_wiki = wikipediaapi.Wikipedia('he')

def get_all_links_rec(pages, num, endarticle):
    new_pages = []
    for page in pages:
        wiki_page = wiki_wiki.page(page)
        new_links_pages = get_links(wiki_page)
        if endarticle == page:
            print(num)
            return 0
        new_pages.extend(new_links_pages)
    get_all_links_rec(new_pages, num+1, endarticle)
    
def get_links(page):
    lings = page.links
    returnarticles = []
    forbidden_titles = ["שיחה:","משתמש:","שיחת משתמש:","ויקיפדיה:","שיחת ויקיפדיה:","קובץ:","שיחת קובץ:","מדיה ויקי:","שיחת מדיה ויקי:","תבנית:","שיחת תבנית:","עזרה:","שיחת עזרה:","קטגוריה:","שיחת קטגוריה:","פורטל:","שיחת פורטל:","ספר:","שיחת ספר:","טיוטה:","שיחת טיוטה:","TimedText:","TimedText talk:","יחידה:","שיחת יחידה:","גאדג'ט:","שיחת גאדג'ט:","הגדרת גאדג'ט:", "Main Page", "נושא:"]
    for i in range (len(lings)):
        res = list(filter(list(lings.keys())[i].startswith, forbidden_titles)) != []
        if not res:
            returnarticles.append(list(lings.keys())[i])
    return returnarticles
    
    

def main():
    startarticle = input("enter start article: ")
    endarticle = input("Enter end article: ")
    get_all_links_rec([startarticle], 0 ,endarticle)
if __name__ == '__main__':
    main()