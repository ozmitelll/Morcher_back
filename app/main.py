from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def health():
    return {
        'Application Name': 'Morcher',
        'Version': '0.0.1',
        'Author': 'Kirill Ozmitel',
        'Date': datetime.now().strftime("%d/%m/%Y"),
        'Status': 'OK'
        }
