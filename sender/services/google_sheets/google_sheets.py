import base64
from io import BytesIO

import numpy as np

from services.credentials import read_table
from services.files import file_service


def write_by_file_url(files: list[str], config: dict, list_name: str) -> None:
    table = read_table(config['url'], list_name)
    google_doc = table[1]
    cols = file_service.find_filters(config)
    ranges = file_service.find_doc_range(google_doc, config)
    aggregated_result = []

    for f in files:
        t = BytesIO(base64.b64decode(f))
        body = file_service.count_days(google_doc, file_service.get_data_from_file(t), cols)
        aggregated_result += [body]

    aggregated_result = np.array(aggregated_result)

    result = np.zeros(shape=(len(aggregated_result[0]), len(aggregated_result[0][0])))

    for k, v in enumerate(aggregated_result):
        for i in range(len(result)):
            result[i] = np.sum([result[i], v[i]], axis=0)

    result = np.transpose(result)

    result = [[clean_zeros(val) for val in sublist] for sublist in result]

    google_doc.update(ranges, result)


def clean_zeros(a):
    if a == 0:
        a = ''
    else:
        a = int(a)
    return a


def get_lists(url):  # for interface use
    google_doc = read_table(url)
    worksheets = google_doc[0].worksheets()
    lists = []
    for ws in worksheets:
        lists.append(ws.title)

    return lists
