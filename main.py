
import asyncio
from typing import Dict, Optional, Union, List, Type

from fastapi import FastAPI, HTTPException, Request , Query , Header
from pydantic import BaseModel


# page description
description = """
Test Application

## Users

You will be able to:

* Read Account Information with filteration using account id

## Authentication

No Auhtenitcation is required for this application

## Resources

The account information is colllected from X webiste


## Errors

Please note that all account ids are integer data types


"""

# description for the endpoints
tags_metadata = [
    {
        "name": "individual accounts",
        "description": "Get Individual accounts at once.",
    },
    {
        "name": "multiple accounts",
        "description": "Get Multiple Accounts at once."
    ,
    },
]

# instance. edit the page
app = FastAPI(
    title="Test Application Aisa Kajouk",
    description=description,
    version="0.0.1",
    contact={
        "name": "Aisa Kajouk",
        "email": "test_email@test.com",
    },
    openapi_tags = tags_metadata,
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)    


class Account(BaseModel):
    ### BaseModel.the field of data will be inherited form here 
    name: str
    description: Optional[str] = None
    balance: float
    active: bool = True
    id : int

# # testing
accounts = dict()
accounts[1] = 123
accounts[2] = 234
accounts[3] = 456

# original endpoint
@app.get("/{account_id}" , tags=['individual accounts']) #, response_model = Account  could add response model
async def get_account(account_id: int) -> Optional[Account] :
    if account_id in accounts:
        return  accounts[account_id]
    else:
        return None



# Suggested endpoint
@app.get("/accountS" , response_model= Account, tags=['multiple accounts'])
async def get_account(   account_ids : Optional[List[int]] = Query(None) ) -> Optional[Account]: # added account ids as a an optional query parameter

    query_items = {  "account_id": account_ids  } 
    return query_items



# # # run
# # # uvicorn main:app --reload
