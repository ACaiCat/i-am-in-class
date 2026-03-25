import gql

from app.models import BaomingsResponse, TongjiResponse, CreateBaomingResponse
from app.params import GetAllBaomingRecordsVariables, GetTongjiVariables, CreateBaomingVariables
from app.queries import GET_ALL_BAOMING_RECORDS_QUERY, GET_TONGJI_QUERY, CREATE_BAOMING_QUERY
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from gql.transport.exceptions import TransportServerError

@retry(
    retry=retry_if_exception_type(TransportServerError),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=10, max=20),
    reraise=True
)
def get_all_baoming_records(client: gql.Client, variables: GetAllBaomingRecordsVariables) -> BaomingsResponse:
    query = GET_ALL_BAOMING_RECORDS_QUERY
    query.variable_values = dict(variables.model_dump(by_alias=True))
    query.operation_name = "getAllBaomingRecords"
    result = client.execute(query)
    parsed = BaomingsResponse.model_validate(result)
    return parsed



@retry(
    retry=retry_if_exception_type(TransportServerError),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=10, max=20),
    reraise=True
)
def get_tongji(client: gql.Client, variables: GetTongjiVariables) -> TongjiResponse:
    query = GET_TONGJI_QUERY
    query.variable_values = dict(variables.model_dump(by_alias=True))
    query.operation_name = "getTongji"
    result = client.execute(query)
    parsed = TongjiResponse.model_validate(result)
    return parsed

@retry(
    retry=retry_if_exception_type(TransportServerError),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=10, max=20),
    reraise=True
)
def create_baoming(client: gql.Client, variables: CreateBaomingVariables) -> CreateBaomingResponse:
    query = CREATE_BAOMING_QUERY
    query.variable_values = {
        "input": variables.model_dump(by_alias=True, mode="json")
    }
    query.operation_name = "createBaomingByInput"
    result = client.execute(query)
    parsed = CreateBaomingResponse.model_validate(result, strict=False)
    return parsed
