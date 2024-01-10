user=input("Enter name: ")
name= user or 'N/A'
print(name)

#Remove letters in a string
l=['www.google.com','www.yahoo.com','www.wikipedia.com','www.prasanna.com']
for link in l:
    print(link.removeprefix('www.'))
    print(link.removesuffix('.com'))
    print("\t")
    