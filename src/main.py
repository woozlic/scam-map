from typing import Union
from loguru import logger
from fastapi import FastAPI
from urllib.parse import urlparse
from src.settings import LOGS_PATH
from src.services import get_all_phishing_domains


logger.add(LOGS_PATH / 'main.log', level='INFO')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/phishing/all")
def read_all_phishing_websites():
    try:
        return {"phishing_all": get_all_phishing_domains()}
    except Exception:
        logger.exception('Error getting all phishing domains')
        return {'success': False}


@app.post("/phishing/")
def read_domain_info(url: str):
    try:
        logger.info(f'{url = }')
        domain = urlparse(url).netloc
        if not domain:
            domain = url
        logger.info(f'{domain = }')
        phishing_domains = get_all_phishing_domains()
        if domain in phishing_domains:
            info = {'is_phishing': True}
        else:
            info = {'is_phishing': False}
        return info
    except Exception:
        logger.exception(f'Error getting info about url: {url}')
        return {'success': False}
