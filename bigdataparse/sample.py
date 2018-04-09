lines =[]
file_name = /Users/kkshmz/4th-yr/bigdataparse/73.csv
N=1000
with open(file_name) as f:
    lines.extend(f.readline() for i in xrange(N))