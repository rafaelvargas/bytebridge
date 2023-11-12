import json


def parse_json_file(filepath: str) -> dict:
    with open(filepath) as file:
        json_content: dict = json.load(file)
        return json_content


def parse_query_parameter(query: str) -> str:
    if query.endswith((".sql",)):
        with open(query) as file:
            query_file_content: str = file.read()
            return query_file_content
    return query
