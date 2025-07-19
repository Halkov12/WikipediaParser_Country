import asyncio
from db import db_manager
from models import Country
from parser import ParserFactory
from sqlalchemy import delete

class DataLoader:
    async def run(self):
        await db_manager.init_db()
        parser = ParserFactory.get_parser()
        countries = await parser.parse()
        async with db_manager.AsyncSessionLocal() as session:
            await session.execute(delete(Country))
            await session.commit()
            for c in countries:
                country = Country(name=c.name, region=c.region, population=c.population)
                session.add(country)
            await session.commit()
        print(f"Inserted {len(countries)} countries.")

if __name__ == "__main__":
    asyncio.run(DataLoader().run()) 