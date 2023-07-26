# It-bootcamp
Тестовое задание для IT-Bootcamp<br/>
Проект упакован в докер контейнер.

## Запуск проекта

```sh
docker-compose build
docker-compose up
```

## Создание суперпользователя

Логин: admin<br>
Пароль: admin

```sh
docker-compose run --rm app make create_admin
```

## Создание тестовой базы данных

```sh
docker-compose run --rm app make base
```

## Запуск тестов

```sh
docker-compose run --rm app pytest
```

## Запуск линтеров

```sh
docker-compose run --rm app make check
```

## Форматирование

```sh
docker-compose run --rm app make format_code
```

Тестовая база данных формируется при запуске контейнера.
