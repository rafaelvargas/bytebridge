from contextlib import closing
from typing import Iterator, List, Callable

import psycopg
from psycopg.rows import dict_row
import mysql.connector

from ..parsers import parse_query_parameter

CONNECTION_TYPES = {
    "postgresql": (psycopg.connect, {"row_factory": dict_row}),
    "mysql": (mysql.connector.connect, {"dictionary": True})
}


def _generate_insert_statement(target_table: str, column_names: List[str]):
    return f"""
            INSERT INTO {target_table} ({",".join(column_names)})
            VALUES ({",".join(["%s" for _ in range(len(column_names))])})
    """


def _generate_list_of_tuples_from_list_of_dictionaries(list: dict):
    return [tuple(value.values()) for value in list]

def _get_connection_with_cursor_params(connection_type: str) -> Callable:
    if connection_type not in CONNECTION_TYPES:
        raise ValueError("Unsupported connection type")
    return CONNECTION_TYPES[connection_type]

def fetch(
    *,
    connection_type: str,
    source_object: str,
    source_query: str,
    batch_size: int,
    source_parameters: dict,
) -> Iterator[List[dict]]:
    if source_query:
        sql = parse_query_parameter(source_query)
    else:
        sql = f"SELECT * FROM {source_object};"

    client, cursor_params = _get_connection_with_cursor_params(connection_type)
    with closing(
        client(
            host=source_parameters["host"],
            user=source_parameters["user"],
            password=source_parameters["password"],
        ),
    ) as connection:
        with closing(connection.cursor(**cursor_params)) as cursor:
            cursor.execute(sql)
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break
                yield batch


def load(
    *,
    connection_type: str,
    batch_iterator: Iterator[List[dict]],
    target_object: str,
    destination_parameters: dict,
) -> None:
    batch = next(batch_iterator)
    if batch:
        client, cursor_params = _get_connection_with_cursor_params(connection_type)
        column_names = batch[0].keys()
        with closing(
            client(
                host=destination_parameters["host"],
                user=destination_parameters["user"],
                password=destination_parameters["password"],
                autocommit=True,
            ),
        ) as connection:
            with closing(connection.cursor(**cursor_params)) as cursor:
                sql = _generate_insert_statement(
                    target_table=target_object,
                    column_names=column_names,
                )
                cursor.executemany(
                    sql,
                    _generate_list_of_tuples_from_list_of_dictionaries(batch),
                )
                for batch in batch_iterator:
                    cursor.executemany(
                        sql,
                        _generate_list_of_tuples_from_list_of_dictionaries(batch),
                    )
