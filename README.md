# 我真的在教室上课

秒应小程序自动打卡，仅支持有截止时间的打卡

## 快速开始

```shell
git clone https://github.com/ACaiCat/i-am-in-class.git
cd i-am-in-class

cp .example.env .env
code .env

uv sync
uv run main.py
```

## 认证

自己用Requable抓包拿JWT，如果手机没root抓不了https，就抓电脑小程序，那个JWT有效期3年。