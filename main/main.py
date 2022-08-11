import pywikibot
import weblinkchecker
startarticle = ''
endarticle = ''
def get_links(links):
    a = set()
    for link in links:
            a.update(link)
    return a

def get_all_links(gen_of_links):
    b = set()
    for links in gen_of_links:
        b.update(get_links(links))
    return b

def get_all_links_rec(gen_of_links, num):
    s = set()
    s = get_all_links(gen_of_links)
    if endarticle in s:
        print("finished " + num)
    else:
        num += 1
        new_s = set()
        for article in s:
            g = (weblinkchecker.weblinks_from_text(article))
        get_all_links_rec(g, num)

def main():
    startarticle = input("enter start article: ")
    endarticle = input("Enter end article: ")
    print("")
    links1 = weblinkchecker.weblinks_from_text(startarticle)
    print(links1)
    print(type(links1))
    get_all_links_rec(links1, 1)
    
if __name__ == '__main__':
    main()
