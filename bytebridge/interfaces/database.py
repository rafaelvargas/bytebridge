from contextlib import closing
from typing import Iterator, List

import psycopg
from psycopg.rows import dict_row

from ..parsers import parse_query_parameter


def fetch(connection_parameters, query: str, batch_size: int) -> Iterator[List[dict]]:
    sql = parse_query_parameter(query)
    with closing(
        psycopg.connect(**connection_parameters, row_factory=dict_row)
    ) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(sql)
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break
                yield batch
