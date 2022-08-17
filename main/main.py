import wikipediaapi
startarticle = ''
endarticle = ''
wiki_wiki = wikipediaapi.Wikipedia('en')

def get_all_links_rec(pages, num, endarticle):
    new_pages = []
    for page in pages:
        for i in page.links:
            new_pages += wiki_wiki.page(i)
        if endarticle == page:
            print("finished in " + num + " steps")
    get_all_links_rec(new_pages, num+1, endarticle)
    
def get_links(page):
    lings = page.links
    for i in range (len(lings)):
        print(list(lings.keys())[i])
    
    

def main():
    startarticle = input("enter start article: ")
    endarticle = input("Enter end article: ")
    page_py = wiki_wiki.page(startarticle)
    get_links(page_py)
    exit(0)
    get_all_links_rec([page_py], 0 ,endarticle)
    
if __name__ == '__main__':
    main()