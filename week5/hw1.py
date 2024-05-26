import csv

with open('book.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Author', 'Year'])
    writer.writerow(['To Kill a Mockingbird','Harper Lee',1960])
    writer.writerow(['1984','George Orwell',1949])
    writer.writerow(['The Great Gatsby','F. Scott Fitzgerald',1925])
    writer.writerow(['Pride and Prejudice','Jane Austen',1813])
    writer.writerow(['The Catcher in the Rye','J.D. Salinger',1951])
    writer.writerow(['The cat','Rada',2008])

with open('book.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    new_book = [(Title, Author, Year) for Title, Author, Year in reader if float(Year) > 2000]

    with open('book_new.csv', 'w') as writfile:
        writer = csv.writer(writfile)
        writer.writerow(['Title', 'Author', 'Year'])
        for i in new_book:
            writer.writerow([i[0], i[1], i[2]])