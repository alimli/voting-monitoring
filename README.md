# voting-monitoring

Upload to Elasticsearch
```
curl -H 'Content-Type: application/x-ndjson' -u elastic:changeme -XPOST '<elastic_server_ip>:9200/_bulk?pretty' --data-binary @ovo_cb.ndjson
```


curl -H 'Content-Type: application/x-ndjson' -u elastic:changeme -XPOST '10.87.11.73:9200/_bulk?pretty' --data-binary @ysk_cb.ndjson
