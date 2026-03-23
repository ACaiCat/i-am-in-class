import gql

from app.models import BaomingsResponse, TongjiResponse, CreateBaomingResponse
from app.params import GetAllBaomingRecordsVariables, GetTongjiVariables, CreateBaomingVariables
from app.queries import GET_ALL_BAOMING_RECORDS_QUERY, GET_TONGJI_QUERY, CREATE_BAOMING_QUERY


def get_all_baoming_records(client: gql.Client, variables: GetAllBaomingRecordsVariables) -> BaomingsResponse:
    query = GET_ALL_BAOMING_RECORDS_QUERY
    query.variable_values = dict(variables.model_dump(by_alias=True))
    query.operation_name = "getAllBaomingRecords"
    result = client.execute(query)
    parsed = BaomingsResponse.model_validate(result)
    return parsed


def get_tongji(client: gql.Client, variables: GetTongjiVariables) -> TongjiResponse:
    query = GET_TONGJI_QUERY
    query.variable_values = dict(variables.model_dump(by_alias=True))
    query.operation_name = "getTongji"
    result = client.execute(query)
    parsed = TongjiResponse.model_validate(result)
    return parsed


def create_baoming(client: gql.Client, variables: CreateBaomingVariables) -> CreateBaomingResponse:
    query = CREATE_BAOMING_QUERY
    query.variable_values = {
        "input": variables.model_dump(by_alias=True, mode="json")
    }
    query.operation_name = "createBaomingByInput"
    result = client.execute(query)
    parsed = CreateBaomingResponse.model_validate(result, strict=False)
    return parsed
