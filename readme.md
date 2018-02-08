# pycrawler

sandbox for collective intelligence engineering with python

## setup with local

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## setup with docker

```
docker build -t ubuntu-phantom .
docker run -it ubuntu-phantom
python3 ~file_path~
```

## memo

部分的にchrome headless modeを使う
[プロキシサーバー使ってみる](http://www.cybersyndrome.net/plr6.html)

kerasの理解が追いつかなかったのでここを参考にして復習する
[無から始めるkeras](https://qiita.com/Ishotihadus/items/6ecf5684c2cbaaa6a5ef)

## airflow

```
export AIRFLOW_HOME=~/work/pycrawler/airflow
airflow initdb
```
