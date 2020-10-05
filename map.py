import pandas as pd 
from influxdb import InfluxDBClient

client= InfluxDBClient(host="localhost",port=8086)
client.switch_database("covid")

df= pd.read_csv("countries.csv")
df.dropna(inplace=True)
print(df.shape)


for row_ind, row in df.iloc[1:].iterrows():
	json_body=[{
	"measurement":"CovidMap",
	"tags":{"Country":row[0]},
	"fields":{
	"name":row[0],
	"latitude":row[2],
	"longitude":row[3],
	"metric":row[4]
	}
	}]
	client.write_points(json_body)
print("done")