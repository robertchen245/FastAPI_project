from fastapi import FastAPI, Path
from typing import Annotated
from datetime import datetime

app = FastAPI()


@app.get("/{time}")
async def get_datetime(
    time: Annotated[datetime, Path(description="type the second from 1970")]
):
    return {"time": time}
