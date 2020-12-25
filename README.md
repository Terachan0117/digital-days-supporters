# デジタルの日 参加企業・団体の取り組み 一覧

内閣官房 [デジタルの日ホームページ(https://digital-days.digital.go.jp/)](https://digital-days.digital.go.jp/) で公開されている参加企業・団体の取り組みの一覧をスクレイピングし、CSVとJSON形式にしたものです。

# Requirement
* Selenium
* Chromedriver

# Installation
ChromeDriver のバージョンは、使用している Chrome のバージョンと同じにする必要があります。

## pip
```bash
>> pip install selenium
>> pip install chromedriver-binary==<version>
```
## conda
```bash
>> conda install selenium
>> conda install python-chromedriver-binary==<version>
```

# Usage
```bash
>> git clone https://github.com/Terachan0117/digital-days-supporters.git
>> cd digital-days-supporters
>> python main.py
```

# Note
本ソフトウェアは、内閣官房が公式に提供しているものではありません。

本ソフトウェアにて提供する情報の正確性・妥当性につきましては細心の注意を払っておりますが、当作者はその保証をするものではありません。本ソフトウェアの利用によって利用者や第三者等にネットワーク障害等による損害、データの損失その他あらゆる不具合、不都合が生じた場合について、裁判所またはそれに準ずる機関で当作者の重過失が認められた場合を除き、当作者では一切の責任を負いません。

本ソフトウェアは、内閣官房 [デジタルの日ホームページ(https://digital-days.digital.go.jp/)](https://digital-days.digital.go.jp/) にて公開されているデータをスクレイピングしています。
本ソフトウェアを利用される際は、システムへの負荷の観点からアクセス頻度を常識的な範囲内に調整するようにして下さい。

# Author
* Terachan

# Contact
お問合わせは、[こちら](https://tera-chan.com#contact)からお願いいたします。

# License
本ソフトウェアは、[MITライセンス](./LICENSE)の下提供されています。