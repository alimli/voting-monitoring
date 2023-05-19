# voting-monitoring

## Python Environment
```
pyenv virtualenv 3.9 ovo_sonuc
```

## Data
Tüm veri setini [bu linkten de](https://drive.google.com/drive/folders/1jqCxJ4qrfKzqNkErT_SsdLSWv9kfWo5p?usp=sharing) indirebilirsiniz.

### Oy ve Ötesi
Oy ve Ötesi verileri için [bu repodan](https://github.com/mkeremavci/OvO-Data-Scraping) Cumhurbaşkanlığı verilerini içeren ovo_cb.json indirilir. ```convert_ovo_cb_to_ndjson.py``` ile  ovo_cb.ndjson dosyası üretilir.

Aşağıdaki komutla veriseti ElasticSearch'e yüklenir. Kullanıcı adı, şifre, ip bilgilerini değiştirebilirsiniz.
```
curl -H 'Content-Type: application/x-ndjson' -u elastic:password -XPOST 'elastic_server:9200/_bulk?pretty' --data-binary @ovo_cb.ndjson
```

### YSK
YSK verileri için [bu repodan](https://github.com/muratuygun/YskConsole) karşılaştırma verilerini içeren excel dosyası indirilir. Toplam oy sayısını hesaplayan bir formül sütunu eklenir. Diğer OvO verilerini içeren ve ilgisi olmayan sütunlar silinir. Excel CSV'olarak ysk_cb.csv olarak kaydedilir.  ```convert_ysk_cb_to_ndjson.py``` ile  ysk_cb.ndjson dosyası üretilir.

Aşağıdaki komutla veriseti ElasticSearch'e yüklenir. Kullanıcı adı, şifre, ip bilgilerini değiştirebilirsiniz.
```
curl -H 'Content-Type: application/x-ndjson' -u elastic:password -XPOST 'elastic_server:9200/_bulk?pretty' --data-binary @ysk_cb.ndjson
```

### Elastic Search
Bu aşamada Elastic Search'de iki adet index'imiz yaratıldı. Ek bir işleme gerek yok.
1. 2023_cb_round1_ovo
2. 2023_cb_round1_ysk

### Grafana
Bu iki index için Datasource yaratılır.
Pattern: No Pattern
ES Version: 7.10+

2023_cb_round1_dashboard.json dosyasını dashboard olarak içeri aktarın.
