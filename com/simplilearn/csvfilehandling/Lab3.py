import csv

with open('bookauthor.csv', mode='w') as file:

    writer=csv.writer(file,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Title', 'Author', 'Genre', 'SubGenre', 'Height', 'Publisher'])
    writer.writerow(['Fundamentals of Wavelets', 'Goswami, Jaideva', 'tech', 'signal_processing', '228', 'Wiley'])
    writer.writerow(['Data Smart', 'Foreman, John', 'tech', 'data_science', '235', 'Wiley'])
    writer.writerow(['God Created the Integers', 'Hawking, Stephen', 'tech', 'mathematics', '197', 'Penguin'])
