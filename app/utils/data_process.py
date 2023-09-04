from distutils.version import StrictVersion
from typing import Dict

from models.models import FuncData


def _sort_versions(data):
    """Sorts a dictionary by version values in "ident" field."""

    # geting a dictionary wity version data.
    inner_data: Dict[str, Dict[str, str]] = data.get('data', {})

    # dictionary sort
    sorted_inner_data = dict(
        sorted(
            inner_data.items(),
            key=lambda x: StrictVersion(x[1]["ident"])
        )
    )
    data["data"] = sorted_inner_data


def _split_values(data):
    """Splits data into a value field."""

    data_dict: dict = data.dict()

    for _, error_data in data_dict.get('data', {}).items():
        value = error_data.get('value', '').strip().split()
        error_data['value'] = value

    return data_dict


def dict_data_process(data: FuncData):
    """Form a dictionary to response."""

    sort_data = _split_values(data=data)
    _sort_versions(data=sort_data)

    return sort_data
