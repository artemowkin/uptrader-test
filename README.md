# Тестовое задание для UpTrader

Ссылка на онлайн версию: http://185.20.225.178/menus

> Админка расположена на `/admin/`, Логин и пароль: `admin`, `admin`

## Запуск dev окружения

Для запуска приложения локально используется следующая команда:

```
$ make docker-dev-start
```

Для того, чтобы убить `dev` окружение, можно выполнить антипод команду:

```
$ make docker-dev-stop
```

## Запуск prod окружения

Для запуска production окружения сперва необходимо создать файл `.env.prod` по аналогии с `.env.local`:

```
# Postgresql configuration
POSTGRES_DB="menutree"
POSTGRES_USER="django"
POSTGRES_PASSWORD="django"

# App configuration
DJANGO_DB_NAME="menutree"
DJANGO_DB_USER="django"
DJANGO_DB_PASSWORD="django"
DJANGO_DB_HOST="db"
DJANGO_DB_PORT=5432
```

После этого выполнить команду:

```
$ make docker-prod-start
```

Если нужно убить production окружение, вот команда:

```
$ make docker-prod-stop
```