# WikipediaParser_Country

## Опис

Сервіс асинхронно парсить дані по населенню країн з Wikipedia або Statisticstimes, зберігає у Postgres і виводить агреговану статистику по регіонах.

## Запуск

1. Клонувати репозиторій:

```bash
git clone <your_repo_url>
cd WikipediaParser_Country
```

2. Запустити Postgres та get_data (парсинг і збереження):

```bash
docker-compose up --build get_data
```

3. Вивести агреговані дані по регіонах:

```bash
docker-compose up print_data
```

## Змінні оточення

- `DATA_SOURCE` — джерело даних (`wikipedia` або `statisticstimes`)
- `DATABASE_URL` — підключення до Postgres (налаштовано у docker-compose.yml)

### Щоб парсити з Statisticstimes:

Відредагуйте `docker-compose.yml`:

```
    environment:
      - DATABASE_URL=postgresql+asyncpg://user:password@db:5432/countries
      - DATA_SOURCE=statisticstimes
```

## Структура
- Весь код у папці `src/`
- Дані зберігаються у таблиці `countries` (name, region, population)
- Агрегація робиться одним SQL-запитом

## Додатково
- Для зміни джерела даних змініть DATA_SOURCE у docker-compose.yml
- Для асинхронної версії використовується SQLAlchemy 2.0 async, aiohttp, selectolax 