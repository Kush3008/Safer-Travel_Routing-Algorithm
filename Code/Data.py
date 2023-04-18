import pandas as pd

data = pd.read_csv('C:\\Users\\akush\\Desktop\\Algo 2\\Code\\code\\Crime.csv', sep='\t')

data['crime_rate'] = data['totalcrime'] / data['totarea']

highest_crime_rate_row = data.sort_values('crime_rate', ascending=False).iloc[0]

print(highest_crime_rate_row)
