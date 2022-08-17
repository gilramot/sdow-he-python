import pywikibot
import weblinkchecker
startarticle = ''
endarticle = ''

def merge(g1, g2):
    for i in g1:
        yield i
    for i in g2:
        yield i

def get_links(gen_of_links):
    a = set()
    for link in gen_of_links:
            a.update(link)
    return a

def get_all_links_rec(gen_of_links, num, endarticle):
    s = get_links(gen_of_links)
    if endarticle in s:
        print("finished " + num)
    else:
        num += 1
        new_s = set()
        bool = True
        for article in s:
            if bool:
                olinks = article.links
                bool = False
            else:
                plinks = article.links
                links = merge(olinks, plinks)
        get_all_links_rec(olinks, num)

def main():
    startarticle = input("enter start article: ")
    endarticle = input("Enter end article: ")
    print("")
    links_gen = weblinkchecker.weblinks_from_text(startarticle)
    print(links_gen)
    print(type(links_gen))
    get_all_links_rec(links_gen, 1)
    
if __name__ == '__main__':
    main()