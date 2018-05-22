BitMEX-API-python
=====================

A lightweight script to connect BitMEX REST API.  
This script is based on the official code below, to fix some points for Python 2.x and 3.x.

* [BitMEX API Connectors - Python-SwaggerPy](https://github.com/BitMEX/api-connectors/tree/master/official-http/python-swaggerpy)

The code is pretty small, just a script file in 110 lines. That's because it loads official Swagger Spec's json.  
So, you can compare with the official code very easily :smile:

## Fixed Points

#### 1. Support for Python 2.x
Default code has Import Error and Functional Error of `bytes`, if you use Python 2.x.  

This code is fixed to use in Python 2.x and 3.x.

#### 2. Remove needless Warnings
Default code often display Warnings such below.  
`xxx format is not registered with bravado-core!`  
This is caused by Swagger Spec's format. SwaggerClient doesn't know formats such `JSON` or `guid`.

This code is fixed to ignore the formats and deal as just string.  

## Requirements

```
$ pip install -r requirements.txt
```
or just

```
$ pip install bravado
```

## Installation
Please download the code and embed a file below to your project.  
You can use it just like `sample.py`, it's very easy. :smile:

```
bitmex.py
```

## Info
If you are happy and want to support us by donate :wink:  
  
BTC: 3BMEXGQ14aQdc5fPgbgwmUKN3UnNbDJ3UB  



***  
  
***  


日本語 (Japanese)
=====================

BitMEX の REST API に接続するとても軽量なスクリプトです。  
以下の BitMEX 公式のコードを修正したもので、Python 2系と3系で簡単に使えるようにしています。

* [BitMEX API Connectors - Python-SwaggerPy](https://github.com/BitMEX/api-connectors/tree/master/official-http/python-swaggerpy)

コード構成はとても小さく、ファイル１つでわずか110行以下のコードになっています。  
（BitMEX が Swagger を採用しており、APIの仕様を読み込む形式をとっているためです。）  
公式のコードとの差分も目視ですぐにチェックできます。


## 修正箇所

#### 1. Python 2系のサポート
公式のコードは、Python 2系で使おうとすると、インポートエラーと `bytes` 関数の動作の違いでエラーが起こります。

このライブラリはその問題を解消し、Python 2系と3系で動作するようになっています。

#### 2. 頻出する Warning が出ないように
公式のコードでは、主要な API で以下のような警告が頻発します。  
`xxx format is not registered with bravado-core!`  

これは、公式のコードが Swagger という仕組みを使っている中で、一部の仕様が解釈されていないために起こるものです。`JSON` や `guid` という format がそれに当たります。  
機能上の問題はないですが、コンソールにずっと出ていると何かと困ります。

このライブラリでは、特に必要性のない `JSON` や `guid` という仕様で警告が出ないようにする処理が追加されています。

## 動作要件
必要なモジュールを以下で追加します。

```
$ pip install -r requirements.txt
```
または単に、

```
$ pip install bravado
```

## 導入
このリポジトリのコードをダウンロードし、以下のファイル１つを配置するだけです。  
同梱の `sample.py` のように簡単に導入できます。使い方は公式のものと同じです。 :smile:

```
bitmex.py
```

## その他
このライブラリに、サポート・チップをいただける方は :wink:  
  
BTC: 3BMEXGQ14aQdc5fPgbgwmUKN3UnNbDJ3UB 
