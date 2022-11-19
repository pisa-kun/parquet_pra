import gzip

with gzip.open("data/foo.csv.gz", "rb") as f:
    for buff in f.readlines():
        print(buff)

with gzip.open("data/foo.csv.gz", "rb") as f:
    data = f.read()
    print(data)