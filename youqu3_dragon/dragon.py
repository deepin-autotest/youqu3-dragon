#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

dragon = APIRouter()

templates = Jinja2Templates(directory="templates")

hi = f"""
Hey! Welcome to use YouQu3.
"""
about_url = "https://github.com/funny-dream/youqu3"


@dragon.get("/")
async def hello(request: Request):
    return templates.TemplateResponse(
        "hello.html",
        {
            "request": request,
            "title": "Dragon",
            "hi": hi,
        }
    )