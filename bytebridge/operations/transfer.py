from ..interfaces.database import fetch as db_fetch
from ..interfaces.database import load as db_load
from ..interfaces.file import fetch as file_fetch
from ..interfaces.file import load as file_load

INTERFACES = {
    "database": {"source": db_fetch, "destination": db_load},
    "file": {"source": file_fetch, "destination": file_load},
}


def transfer(
    *,
    query: str,
    source_object: str,
    source_connection,
    batch_size: int,
    target: str,
    destination_connection,
):
    batch_iterator = INTERFACES[source_connection["type"]]["source"](
        query=query,
        source_object=source_object,
        batch_size=batch_size,
        source_parameters=source_connection.get("parameters"),
    )
    INTERFACES[destination_connection["type"]]["destination"](
        destination_parameters=destination_connection.get("parameters"),
        target=target,
        batch_iterator=batch_iterator,
    )
