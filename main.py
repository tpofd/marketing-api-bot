from fastapi import FastAPI
from requests_html import HTMLSession

app = FastAPI()


@app.get("/yandex_metric_last_week_visits")
async def yandex_metric_last_week_visits(metric_access_token, metric_app_id):

    """
    :param metric_access_token: user oauth Yandex Metric token
    :param metric_app_id: counter id
    :return: json with information about visits on last week
    """

    session = HTMLSession()

    metrika_headers = {

        'GET': '/management/v1/counters HTTP/1.1',
        'Host': 'api-metrika.yandex.net',
        'Authorization': metric_access_token,
        'Content-Type': 'application/x-yametrika+json'

    }
    metrika_url = f'https://api-metrika.yandex.net/stat/v1/data?metrics=ym:s:visits&id={metric_app_id}'

    json_content_response = session.get(metrika_url, headers=metrika_headers).json()

    return json_content_response


@app.get("/")
async def root():
    return {"message": "Hello World"}
