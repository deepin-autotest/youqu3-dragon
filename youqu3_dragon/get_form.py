#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
import os

from fastapi import APIRouter

form = APIRouter()


@form.get("/form/")
async def get_form(
        git_url: str,
        git_branch: str,
        git_user: str,
        git_password: str,
        clients: str,
        tags: str,
        keywords: str,
        task_id: str,
        fillback_user: str,
        fillback_password: str,
):
    data = {
        "git_url": git_url,
        "git_branch": git_branch,
        "git_user": git_user,
        "git_password": git_password,
        "clients": clients,
        "tags": tags,
        "keywords": keywords,
        "task_id": task_id,
        "fillback_user": fillback_user,
        "fillback_password": fillback_password,
    }
    youqu_cmds = ["youqu3-cargo", "run"]
    tags = data.get("tags")
    if tags:
        youqu_cmds.extend(["--tags", tags])
    youqu_cmd = " ".join(youqu_cmds)
    # os.system(youqu_cmd)
    print(data)
    return youqu_cmds
