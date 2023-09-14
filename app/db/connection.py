import asyncio

import motor.motor_asyncio

from app.config import config


async def connect_to_mongodb():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        config.MONGODB_URL
    )
    db = client["my_database"]  # database name
    return db


db = asyncio.run(connect_to_mongodb())

collection = db["userbase"]  # collection name
