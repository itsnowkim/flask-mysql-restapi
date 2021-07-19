# flask-mysql-restapi

Flask + MySql로 만든 간단한 CRUD입니다.
Flask app은 로컬에서, MySql은 컨테이너에서 실행하면 되도록 만들었습니다.

## Install

### container 생성 - mysql 컨테이너

```sh
$ docker-compose up -d
```

### flask 설치 및 실행

```sh
$ virtualenv venv && source venv/bin/activate
(venv) $ pip3 install flask PyMySQL flask-sqlacodegen Flask-SQLAlchemy SQLAlchemy
```

## Run

```sh
$ flask run
```

이제 postman에서 테스트해보세요
