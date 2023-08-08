from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response():
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, POST_SCHEMA):
        if isinstance(self.response_json, list):
            for post in self.response_json:
                validate(post, POST_SCHEMA)
        else:
            validate(self.response_json, POST_SCHEMA)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value

class Response_pydantic():
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for post in self.response_json:
                schema.model_validate(post)
        else:
            schema.model_validate(self.response_json)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self