import asyncio
from sqlalchemy import select, func
from db import db_manager
from models import Country

class RegionStatsPrinter:
    async def run(self):
        await db_manager.init_db()
        async with db_manager.AsyncSessionLocal() as session:
            result = await session.execute(
                select(
                    Country.region,
                    func.sum(Country.population).label("total_population"),
                    func.max(Country.population).label("max_population"),
                    func.min(Country.population).label("min_population")
                ).group_by(Country.region)
            )
            regions = result.fetchall()
            for region, total, max_pop, min_pop in regions:
                big = await session.execute(
                    select(Country.name, Country.population)
                    .where(Country.region == region)
                    .order_by(Country.population.desc())
                    .limit(1)
                )
                big_name, big_pop = big.first()
                small = await session.execute(
                    select(Country.name, Country.population)
                    .where(Country.region == region)
                    .order_by(Country.population.asc())
                    .limit(1)
                )
                small_name, small_pop = small.first()
                print(f"==============================")
                print(f"Region: {region}")
                print(f"Total population: {total}")
                print(f"Largest country: {big_name}")
                print(f"Population: {big_pop}")
                print(f"Smallest country: {small_name}")
                print(f"Population: {small_pop}")

if __name__ == "__main__":
    asyncio.run(RegionStatsPrinter().run()) 