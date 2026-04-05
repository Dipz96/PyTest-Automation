# utils/helpers.py

from urllib.parse import urlparse, parse_qs

def get_page(endpoint):
    parsed = urlparse(endpoint)
    params = parse_qs(parsed.query)

    # convert {"page": ["2"]} → {"page": "2"}
    return {k: v[0] for k, v in params.items()}


def get_execution_time(endpoint):
    parsed = urlparse(endpoint)
    params = parse_qs(parsed.query)

    return float(params["delay"][0])