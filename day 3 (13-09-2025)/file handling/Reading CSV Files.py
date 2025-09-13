import csv
import io


csv_data = """Year,Industry,Value
2014,Manufacturing,769400
2014,Manufacturing,48000
2014,Manufacturing,12
"""
csvfile = io.StringIO(csv_data)
csvreader = csv.reader(csvfile)
for row in csvreader:
    print(row)
