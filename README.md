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
virtualenv venv && source venv/bin/activate
pip3 install flask PyMySQL flask-sqlacodegen Flask-SQLAlchemy SQLAlchemy
```

## Run

### flask 앱 실행

```sh
flask run
```

### db 로그인
docker의 bash로 들어가서 mysql 로그인을 한다.

```sh
mysql -u wool -p
Enter password: qwerqwer123
```

이제 postman에서 테스트해보세요
