# Django - celery - redis 정리

- Django를 사용한 비동기 처리 작업들을 정리하며 오랜만에 사용해보고자 함.
- Django의 DB, Redis는 docker를 통하여 localhost에서 사용한다. 

- project 이름은 config로 한다.
- app은 app_<name> 형식으로 사용한다.

- settings의 하드코딩된 값을은 secret.json이라는 파일에서 따로 관리한다.