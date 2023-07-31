# IT-bootcamp
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FArtsiomPH%2FIt-bootcamp%2Fbadge%3Fref%3Dmain&style=flat)](https://actions-badge.atrox.dev/ArtsiomPH/It-bootcamp/goto?ref=main)
[![Coverage Status](https://coveralls.io/repos/github/ArtsiomPH/It-bootcamp/badge.svg?branch=main)](https://coveralls.io/github/ArtsiomPH/It-bootcamp?branch=main)

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
docker-compose run --rm app make lint
```

## Форматирование

```sh
docker-compose run --rm app make format_code
```
