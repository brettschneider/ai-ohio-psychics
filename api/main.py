#!/usr/bin/env python
"""An API that exposes the chatbot"""
import base64
from typing import Annotated

from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import database.account_info
from chatbot import ChatBot
from database.authentication import authenticate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Credentials(BaseModel):
    username: str
    password: str


@app.post('/api/login')
async def login(creds: Credentials):
    if user := authenticate(creds.username, creds.password):
        str_bytes = creds.username.encode("utf-8")
        b64_bytes = base64.b64encode(str_bytes)
        return {
            "token": b64_bytes.decode("utf-8"),
            "username": database.account_info.get_user_name(creds.username)
        }
    raise HTTPException(status_code=401)


class Prompt(BaseModel):
    query: str


@app.post('/api/chat')
async def chat(prompt: Prompt, x_token: Annotated[str, Header(required=True)]):
    b64_bytes = x_token.encode('utf-8')
    decoded_bytes = base64.b64decode(b64_bytes)
    customer_id = decoded_bytes.decode('utf-8')

    cb = ChatBot(customer_id)

    return StreamingResponse(cb.ask(prompt.query), media_type="text/event-stream", headers={
        "Access-Control-Allow-Origin": "http://localhost:3000"
    })


if __name__ == '__main__':
    from uvicorn import run

    run(app)
