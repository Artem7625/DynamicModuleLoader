import json
from typing import Any, Dict, List, TypeAlias

import requests  # type: ignore


request_data: TypeAlias = Dict[str, str | Dict[str, Dict[str, str]]]
response_data: TypeAlias = Dict[str, str | Dict[str, Dict[str, List[str]]]]


def get_json_data(path: str) -> Dict[Any, Any]:
    """Loads a JSON data with request param."""

    with open(path, 'r', encoding='utf-8') as load_file:
        data: Dict[Any, Any] = json.load(load_file)

    return data


def make_post_req(url: str) -> response_data:
    """Makes post request with JSON param."""

    headers = {"Content-Type": "application/json"}
    data: request_data = get_json_data(path='data.json')

    with requests.Session() as session:
        with session.post(url=url, headers=headers, json=data) as response:
            return response.json()


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/json'
    print(make_post_req(url=url))
