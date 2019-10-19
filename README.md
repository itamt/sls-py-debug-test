## Overview

Example for debugging serverless framework app on local with PyCharm


## How to

```bash
# prepare .env file
cp .env.sample .env

docker-compose build --no-cache
docker-compose up -d

# setup project interpreter on PyCharm (./screenshot/1.png - 2.png)
# and
# setup run configuration on PyCharm (./screenshot/3.png)
# and
# start debug server on host PyCharm

docker-compose exec slsapp sls invoke local --function hello
# => debug

docker-compose exec slsapp sls offline --host 0.0.0.0
# => localhost:3000 on host
# => debug
```


## ref.

[1](https://scrapbox.io/tasuwo/AWS_SAM_CLI_で立ち上げた_Lambda_をリモートデバッグする)

[2](https://dev.classmethod.jp/server-side/serverless/python-remote-debug/)

[3](https://qiita.com/masahiro-fukushima/items/67959a0dfede69c9d653)

[4](https://stackoverflow.com/questions/36058776/django-docker-remote-debug-using-pydev)
