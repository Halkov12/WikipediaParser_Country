# Parser_Country

## Description

The service asynchronously parses country population data from Wikipedia or Statisticstimes, stores it in Postgres, and outputs aggregated statistics by region.

## Launch

1. Clone the repository:

```bash
git clone <your_repo_url>
cd WikipediaParser_Country
```

2. Run get_data (parsing and saving):

```bash
docker-compose up --build get_data
```

3. Display aggregated data by region:

```bash
docker-compose up print_data
```

## Environment

- `DATA_SOURCE` — (`wikipedia` or `statisticstimes`)
- `DATABASE_URL` — Postgres connection


## Structure
- All code in the `src/` folder
- Data stored in the `countries` (name, region, population)
- Aggregation done with a single SQL query

## Additional info
- To change the data source, modify DATA_SOURCE in docker-compose.yml
- Async version uses SQLAlchemy 2.0 async, aiohttp, selectolax
