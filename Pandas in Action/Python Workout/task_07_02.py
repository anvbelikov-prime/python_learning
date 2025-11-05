def hide_authors(pages, authors):
    for author in authors:
        pages = pages.replace(author, '_' * 10)
    return pages

print(hide_authors('This is a page by Belikov Anton. Belikov A. is a great specialist in many fields of computer science.', ['Belikov Anton', 'Belikov A.']))
