import pandas as pd

url = "https://raw.githubusercontent.com/sulchan/Data205/master/ChinookAlbums.csv"
df = pd.read_csv(url)
print(df.head())