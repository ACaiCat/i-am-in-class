import main
from app.api import *
from app.client import get_client

if __name__ == "__main__":
    tongji_id = input("请输入统计ID: ")
    client = get_client()
    result = get_tongji(client, GetTongjiVariables(
        _id=tongji_id,
    ))

    main.submit_baoming(client, result.tongji)
