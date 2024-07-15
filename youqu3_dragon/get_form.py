#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from fastapi import APIRouter

form = APIRouter()


@form.get("/form/")
async def get_form(
        git_url: str,
        git_branch: str,
        runway: str
):
    a = {
        "git_url": git_url,
        "git_branch": git_branch,
        "runway": runway
    }
    print(a)
    return a
