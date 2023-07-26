# It-bootcamp
Тестовое задание для IT-Bootcamp<br />
Проект упакован в докер контейнер.

## Запуск проекта

```sh
docker-compose build
docker-compose up
```

## Создание суперпользователя

```sh
docker-compose run --rm app make create_admin
```

## Запуск тестов

```sh
docker-compose run --rm app pytest
```

## Запуск линтеров

```sh
docker-compose run --rm app make check
```

Тестовая база данных формируется при запуске контейнера.
