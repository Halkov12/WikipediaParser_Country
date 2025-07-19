import asyncio
from db import init_db, AsyncSessionLocal
from models import Country
from parser import get_parser
from sqlalchemy import delete

async def main():
    await init_db()
    parser = get_parser()
    countries = await parser.parse()
    async with AsyncSessionLocal() as session:
        await session.execute(delete(Country))
        await session.commit()
        for c in countries:
            country = Country(name=c.name, region=c.region, population=c.population)
            session.add(country)
        await session.commit()
    print(f"Inserted {len(countries)} countries.")

if __name__ == "__main__":
    asyncio.run(main()) 