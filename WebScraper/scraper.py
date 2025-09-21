import wikipediaapi

def get_wiki(title):
    wiki = wikipediaapi.Wikipedia(
        user_agent="Mozilla 5.0",
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
    )

    page = wiki.page(title)
    if page.exists():
        return f"{page.title} - {page.text[:1000]}"
    else:
        return "Failed"


title = input("What do you want to search: ")
print(get_wiki(title))