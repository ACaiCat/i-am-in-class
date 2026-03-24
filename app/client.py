from gql import Client
from gql.transport.requests import RequestsHTTPTransport

from app.config import settings

GRAPHQL_URL = "https://www.aiphoto8.cn/api/graphql"


def get_client() -> Client:
    transport = RequestsHTTPTransport(
        url=GRAPHQL_URL,
        headers={"Authorization": settings.authorization},
    )
    return Client(transport=transport, fetch_schema_from_transport=False)
