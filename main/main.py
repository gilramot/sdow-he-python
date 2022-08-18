from gettext import find
import wikipediaapi
startarticle = ''
endarticle = ''
wiki_wiki = wikipediaapi.Wikipedia('he')

def get_all_links_rec(pages, num, endarticle):
    new_pages = []
    for page in pages:
        page_py = wiki_wiki.page(page)
        new_pages_from_page = get_links(page_py)
        if find(new_pages_from_page, endarticle):
            print("finished in " + num + " steps")
            exit(0)
        new_pages+=new_pages_from_page
    get_all_links_rec(new_pages, num+1, endarticle)
    
def get_links(page):
    lings = page.links
    returnlinks = []
    forbidden_titles = ["שיחה:","משתמש:","שיחת משתמש:","ויקיפדיה:","שיחת ויקיפדיה:","קובץ:","שיחת קובץ:","מדיה ויקי:","שיחת מדיה ויקי:","תבנית:","שיחת תבנית:","עזרה:","שיחת עזרה:","קטגוריה:","שיחת קטגוריה:","פורטל:","שיחת פורטל:","ספר:","שיחת ספר:","טיוטה:","שיחת טיוטה:","TimedText:","TimedText talk:","יחידה:","שיחת יחידה:","גאדג'ט:","שיחת גאדג'ט:","הגדרת גאדג'ט:"]
    for i in range (len(lings)):
        res = list(filter(list(lings.keys())[i].startswith, forbidden_titles)) != []
        if not res:
            returnlinks.append(list(lings.keys())[i])
    return returnlinks
            
    

def main():
    startarticle = input("enter start article: ")
    endarticle = input("Enter end article: ")
    page_py = wiki_wiki.page(startarticle)
    get_all_links_rec([page_py], 0 ,endarticle)
    
if __name__ == '__main__':
    main()