import csv
import datetime
import json

index_name = "2023_cb_round1_ysk"
timestamp = datetime.datetime.fromisoformat('2023-05-14T14:00:00').isoformat() + 'Z'

with open("ysk_cb.ndjson", 'w', encoding='utf-8') as of:
    with open("ysk_cb.csv", newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';', quotechar='|')
        next(reader, None)  # skip the headers
        for row in reader:
            city = row[0]
            district = row[1]
            ballotbox = row[2]
            total_votes = int(row[3])
            votes = dict([
                    ('1', int(row[4])),
                    ('2', int(row[5])),
                    ('3', int(row[6])),
                    ('4', int(row[7]))
            ])
            id = "_".join((city, district, ballotbox))
            jsonArray =  dict([
                ('id', id),
                ('city', city),
                ('district', district),
                ('ballot_box_number', ballotbox),
                ('total_votes', total_votes),
                ('votes', votes),
                ('@timestamp', timestamp)
            ])

            jsonRow = json.dumps(jsonArray)
            of.write('{ "index" : { "_index": "' + index_name + '", "_id": "' + id + '" } }\n')
            of.write(jsonRow + '\n')