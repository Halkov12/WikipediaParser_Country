import aiohttp
from selectolax.parser import HTMLParser
from typing import List
import re
from config import DATA_SOURCE

def clean_name(name: str) -> str:
    return re.sub(r'\[.*?\]', '', name).strip()

class CountryData:
    def __init__(self, name: str, region: str, population: int):
        self.name = name
        self.region = region
        self.population = population

class WikipediaParser:
    URL = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959"

    async def fetch(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.URL) as resp:
                return await resp.text()

    async def parse(self) -> List[CountryData]:
        html = await self.fetch()
        tree = HTMLParser(html)
        table = tree.css_first("table.wikitable")
        countries = []
        if not table:
            return countries
        rows = table.css("tr")[1:]
        for i, row in enumerate(rows):
            if i == 0:
                continue
            cells = row.css("td")
            if len(cells) < 6:
                continue
            name = clean_name(cells[0].text(strip=True))
            region = cells[4].text(strip=True)
            pop_text = cells[2].text(strip=True)
            pop_text = re.sub(r"[^\d]", "", pop_text)
            if not pop_text:
                continue
            population = int(pop_text)
            countries.append(CountryData(name, region, population))
        return countries

class StatisticstimesParser:
    URL = "https://statisticstimes.com/demographics/countries-by-population.php"

    async def fetch(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.URL) as resp:
                return await resp.text()

    async def parse(self) -> List[CountryData]:
        html = await self.fetch()
        tree = HTMLParser(html)
        table = tree.css_first("table#table_id")
        countries = []
        if not table:
            return countries
        rows = table.css("tr")[1:]
        for i, row in enumerate(rows):
            if i == 0:
                continue
            cells = row.css("td")
            if len(cells) < 9:
                continue
            name = clean_name(cells[0].text(strip=True))
            region = cells[8].text(strip=True)
            pop_text = cells[1].text(strip=True)
            pop_text = re.sub(r"[^\d]", "", pop_text)
            if not pop_text:
                continue
            population = int(pop_text)
            countries.append(CountryData(name, region, population))
        return countries

class ParserFactory:
    @staticmethod
    def get_parser():
        if DATA_SOURCE == "statisticstimes":
            return StatisticstimesParser()
        return WikipediaParser() 