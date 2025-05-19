import os
import asyncio
import httpx
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")
BASE_URL = "https://api.nasa.gov/planetary/apod"

def get_date_range(days: int):
    today = datetime.today()
    return [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days)]

async def fetch_apod(client, date):
    params = {
        "api_key": API_KEY,
        "date": date
    }
    try:
        response = await client.get(BASE_URL, params=params, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        return {
            "date": date,
            "title": data.get("title"),
            "url": data.get("url"),
            "explanation": data.get("explanation")[:100]
        }
    except httpx.HTTPError as e:
        return {"date": date, "error": str(e)}


async def main():
    dates = get_date_range(5)  
    async with httpx.AsyncClient() as client:
        tasks = [fetch_apod(client, date) for date in dates]
        results = await asyncio.gather(*tasks)


    for res in results:
        print(f"\nDate: {res["date"]}")
        if "error" in res:
            print(f"Error: {res["error"]}")
        else:
            print(f"Title: {res["title"]}")
            print(f"URL: {res["url"]}")
            print(f"Summary: {res["explanation"]}")

if __name__ == "__main__":
    asyncio.run(main())
