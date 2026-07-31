import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI
import os
from TestProxyForTG.src.prox_checker.main import run as start, load_proxies
app = FastAPI()
load_dotenv()
@app.get("/")
async def home():
    await asyncio.sleep(20)
    my_url = f"https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/getMe"
    my_concurrency = 100
    my_timeout = 5
    proxies = await load_proxies()
    result = await start(proxies, my_concurrency, my_timeout, url=my_url)
    return {"result": result}

