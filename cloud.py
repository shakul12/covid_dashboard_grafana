
from influxdb import InfluxDBClient
import datetime
client= InfluxDBClient(host="localhost",port=8086)
client.switch_database("covid")

file= open("a4eq3bobt7olorw2gvtkknpqejx74x","r")
content= file.read()

colList= content.split("\n")

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

final_str=""
for row in colList:
	row= row.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
	if len(row.strip())!=0:
		count= int(row[:1])
		val= str(row[2:])+" "
		final_str+=val*count

out = wordListToFreqDict(final_str.split(" "))

for key, val in out.items():
	if len(key.strip())==0:
		continue
	json_body=[{
	"measurement":"CovidCloud",
	"tags":{"words":key},
        "fields":{"Freq":int(val), "words":key}
	}]
	client.write_points(json_body)
print("done")
