import json
import datetime

index_name = "2023_cb_round1_ovo"
timestamp = datetime.datetime.fromisoformat('2023-05-14T14:00:00').isoformat() + 'Z'

with open("ovo_cb.ndjson", 'w', encoding='utf-8') as of:
    with open("ovo_cb.json", "rb") as f:
        data = json.load(f)
        for city in data:
            # print(city)
            for district in data[city]['ilceler']:
                # print(district)
                for ballotbox in data[city]['ilceler'][district]['sandiklar']:
                    # print(ballotbox)
                    ballotdata = data[city]['ilceler'][district]['sandiklar'][ballotbox]
                    votes = dict([
                            ('1', ballotdata['adaylar']['RECEP TAYYİP ERDOĞAN']),
                            ('2', ballotdata['adaylar']['MUHARREM İNCE']),
                            ('3', ballotdata['adaylar']['KEMAL KILIÇDAROĞLU']),
                            ('4', ballotdata['adaylar']['SİNAN OĞAN'])
                    ])
                    id = "_".join((city, district, ballotbox))
                    jsonArray =  dict([
                        ('id', id),
                        ('city', city),
                        ('district', district),
                        ('ballot_box_number', ballotbox),
                        ('total_votes', ballotdata['total_vote']),
                        ('report_received', ballotdata['tutanak']),
                        ('votes', votes),
                        ('@timestamp', timestamp)
                    ])

                    jsonRow = json.dumps(jsonArray)
                    of.write('{ "index" : { "_index": "' + index_name + '", "_id": "' + id + '" } }\n')
                    of.write(jsonRow + '\n')