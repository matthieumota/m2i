from fastapi import FastAPI, Depends, HTTPException, status, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import os
import random
import time

app = FastAPI()
security = HTTPBearer()

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

@app.post('/login')
async def login(
  username: str = Body(...),
  password: str = Body(...)
):
  if username != 'fiorella' or password != 'password':
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
      detail='Login ou mot de passe incorrect',
    )

  return {'access_token': API_TOKEN}

@app.get('/status')
async def get_status(app: str = 'unknown', credentials: HTTPAuthorizationCredentials = Depends(security)):
  token = credentials.credentials

  if token != API_TOKEN:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail='Token invalide'
    )

  app_status = random.choice(['OK', 'DEGRADED', 'DOWN'])
  time.sleep(0.5)

  return {
    'app': app,
    'status': app_status,
    'response_time': 0,
    'timestamp': time.time(),
  }
