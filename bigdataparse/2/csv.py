import csv

#setup the input 
reader = csv.DictReader(open('/Users/kkshmz/4th-yr/bigdataparse/2/kumamotodata.txt', 'rb'), delimiter='\t')  
with open('/Users/kkshmz/4th-yr/bigdataparse/2/kumamotodata.txt', 'rb') as input_file:
    reader = csv.reader(input_file, delimiter=' ', quoting = csv.QUOTE_NONE)
    
    with open('reddit.csv', 'wb') as output_file:
        writer = csv.writer(output_file)

        for row in reader:
            writer.writerow(row)


    spamreader = csv.reader
for row in reader:
spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print ', '.join(row)