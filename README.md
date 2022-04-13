# Сервис по сбору статистики
## Инструкция по развертыванию проекта

Склонировать репозиторий: 
```bash
git clone https://github.com/viktornikolaev1995/counter_of_statistics.git
```

### Настройка проекта

Перейти в папку проекта: `cd 
counter_of_statistics`

Внесите при необходимости корректировки в переменные окружения, находящиеся в файле `.env`

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

Проект доступен по адресу http://127.0.0.1:8000/

К API есть документация по адресу http://127.0.0.1:8000/redoc/, http://127.0.0.1:8000/docs/

### Для просмотра запущенных контейнеров

```bash
docker-compose ps
```

### Для просмотра списка образов

```bash
docker-compose images
```

### Для просмотра журнала сервисов

```bash
docker-compose logs -f app
```

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Остановка контейнеров с последующим их удалением

Для остановки и удаления контейнеров выполните команду:

```bash
docker-compose down
```