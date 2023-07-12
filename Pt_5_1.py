import csv

header = ["Book", "Author", "Year of release"]
books = [["Eragon", "Christopher Paolini", "2003"],
         ["Pandora Hearts", "Jun Mochizuki", "2006"],
         ["The Silmarillion", "John Ronald Reuel Tolkien", "1977"],
         ["The Murder of Roger Ackroyd", "Agatha Christie", "1926"],
         ["Hell's Paradise: Jigokuraku", "Yuki Kaku", "2018"]]

filename = "favourite_books.csv"

with open(filename, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(books)
