# this is for fast create a array :D
names = """obs
year
month
day
date
latitude
longitude
zon.winds
mer.winds
humidity
air temp.
s.s.temp.""".split('\n')
print(names)

import pandas as pd
nino = pd.read_csv('data/tao-all2.dat.gz', names = names, header = None, sep = " ")
nino.head()
