pages = 20
pagesread = 5
days = 3

def formula():
    total_pages = pages - pagesread
    final = total_pages / days
    return final

print(formula())