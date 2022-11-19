import io
import gzip
import csv
import os

data = [['col1','col2','col3','col4'],
        ['data','data','three','four'],
        ['data','data','three','four'],
        ['data','data','three','four']]

buff = io.StringIO()
writer = csv.writer(buff)

writer.writerow(data)
print(buff.getvalue().encode("utf-8"))

print("writing data to gzipped file.")

d = gzip.compress(buff.getvalue().encode("utf-8"))
f = open("data/foo.csv.gz", "wb")
f.write(d)
f.close()