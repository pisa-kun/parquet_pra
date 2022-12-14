### pythonで　parquet処理

#### Parquetの特徴
- 列指向データファイル形式
  - 列ごとに整理されるため、ストレージ容量を節約
- 効率的なデータ圧縮と符号化形式を提供
- あらゆる言語に対応するオープンソースのファイル形式
- 構造化データだけでなく、あらゆる種類のデータを保存可能

#### 列志向フォーマットでデータを保存するメリット

- csvのような行指向ファイルと比較すると、列指向ストレージは*非関連データ*を迅速にスキップでき、集計クエリの時間が短縮される

[参照](https://www.databricks.com/jp/glossary/what-is-parquet#:~:text=Parquet%20%E3%81%A8%E3%81%AF,%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E5%90%91%E4%B8%8A%E3%81%95%E3%81%9B%E3%81%BE%E3%81%99%E3%80%82)

#### csvのデメリット
- Amazon AthenaやSpectrumではクエリごとにスキャンしたデータ量で課金される
  - Parquetではストレージ必要量は少なくとも3分の1削減され、スキャンとデシリアライズに必要な時間の大幅な改善で全体のコストが削減される。

|  データセット |  Amazon S3でのデータサイズ  | クエリの実行時間  |  スキャンデータ  |  コスト  |
| ---- | ---- | ---- | ---- | ---- | 
|  csvファイルのデータ  |  1TB  | 236s  | 1.15TB  |  $5.75  |
|  Apache Parquet形式のデータ  |  130GB  | 6.78s  | 2.51GB  |  $0.01  |
|  削減率  |  87%  | 34倍速  | 99%  |  99.7%  |

#### 特徴(追記)
- twitter社とcloudera社で共同開発されたストレージ形式
- バイナリ形式なのでcsvファイルと比較すると視認性は落ちる

- *行分析*においては、特定の列に対しての計算をすることが多いので列指向が有利
- また、同一列であれば項目の属性も同じため圧縮が効きやすい
[参照](https://www.souichi.club/technology/apache-parquet/)

#### snowflakeとparquet

この記事で紹介されている
https://zenn.dev/kyami/articles/40771c49741c01


#### glue job

https://www.cloudnotes.tech/entry/glue-csv-parquet-athena

#### parquet default compress

https://www.techscore.com/blog/2019/12/07/parquet_examine/

> 同じ CSV ファイルを gzip 圧縮したもの、Parquet に変換したもの（Parquet はデフォルトで Snappy 圧縮されます）を用意し、サイズを計測しました。


```
gzip が早々に頭打ちになったのに比べて、Parquet は継続的にサイズを小さくし続けていることが分かります。更にデータ件数が増えれば、gzip の10分の1、もとの CSV ファイルの100分の1程度にもなりそうです。ただし、ある程度のファイルサイズが無ければ恩恵を受けられないことも分かりました。
```

#### pyspark

https://dk521123.hatenablog.com/entry/2021/04/11/101305