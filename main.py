from fastapi import FastAPI, WebSocket
import asyncio
from mainfuncUsingPandas import *
import os
from fixes import Fixes
import pickle

app = FastAPI()

with open('model.pkl','rb') as f:
    model = pickle.load(f)

@app.websocket('/ws')
async def websocketEndpoint(websocket: WebSocket):
    await websocket.accept()
    fixes = Fixes()
    try:
        data = initialize_attributes()
        while True:
            data = apply_event(random.choice(events), data)
            # pred = model.predict(data)
            # data = fixes.apply_fixes(data,pred)
            await websocket.send_json(data.to_dict(orient='records')[0])
            await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket Error: {e}")
    finally:
        await websocket.close()

if __name__ == '__main__':
    os.system('uvicorn main:app --reload')