# NASA APOD Fetcher (Async Version)

This is an asynchronous Python tool to fetch Astronomy Picture of the Day (APOD) from NASA's official API using `httpx` and `asyncio`. It's designed for efficient, fast, and secure data fetching — especially suitable for high-performance applications or APIs with rate limits.

## Features

- **Async API Requests**: Uses `httpx` and `asyncio` to make non-blocking HTTP requests.
- **Secure API Key Handling**: Reads API keys securely from `.env` files using `python-dotenv`.
- **Multiple Requests**: Can send multiple async requests efficiently.
- **JSON Response Handling**: Parses and prints clean and readable data like title, date, and explanation.
- **Error Handling**: Robust error checking for failed or invalid requests.
 
## Technologies Used

- Python 3.10+
- [httpx](https://www.python-httpx.org/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- NASA APOD API

## Setup Instructions

1. **clone the repo** 
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd clients_Notes/nasa_apod_fetcher
