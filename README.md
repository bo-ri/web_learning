## setup
1. `$ docker-compose build`
1. `$ docker-compose up`
1. 出てくるtokenをコピー，localhost:8888へアクセスしてtokenを使ってlogin
1. ブラウザでterminalを開く．(bashでも可)
1. `$ python`入力(python起動)
1. 以下入力
``` 
>> from IPython.lib import passwd
>> passwd()
```
1. 任意のパスワード入力
1. `'sha1:???????????????????????????'`の形式でキーを得られるため，コピー
1. Docker-compose.yml開いてコメントアウトしている行の最後に貼り付け
1. 一個上の行削除

以降`$ docker-compose up -d`で起動，localhost:8888で接続
`$ docker-compose down`で終了


## 任意のmodule追加する場合
- Dockerfileに書く
- pipなら`USER root`の上に追記
- apt-getなら`USER root`の下に追記する
- `$ docker-compose build`でbuildし直すと反映される．パスワードとかはそのまま．
