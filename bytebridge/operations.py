from .interfaces.database import fetch as db_fetch
from .interfaces.database import load as db_load
from .interfaces.file import fetch as file_fetch
from .interfaces.file import load as file_load

INTERFACES = {
    "postgresql": {"source": db_fetch, "destination": db_load},
    "mysql": {"source": db_fetch, "destination": db_load},
    "parquet": {"source": file_fetch, "destination": file_load},
}


def transfer(
    *,
    source_query: str,
    source_object: str,
    source_connection,
    batch_size: int,
    target_object: str,
    destination_connection,
):
    batch_iterator = INTERFACES[source_connection["type"]]["source"](
        connection_type=source_connection["type"],
        source_query=source_query,
        source_object=source_object,
        batch_size=batch_size,
        source_parameters=source_connection.get("parameters"),
    )
    INTERFACES[destination_connection["type"]]["destination"](
        connection_type=destination_connection["type"],
        batch_iterator=batch_iterator,
        target_object=target_object,
        destination_parameters=destination_connection.get("parameters"),
    )
