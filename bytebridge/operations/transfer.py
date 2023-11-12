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
    source_parameters,
    batch_size: int,
    target: str,
    destination_parameters,
):
    batch_iterator = INTERFACES[source_parameters["type"]]["source"](
        query=query,
        source_object=source_object,
        batch_size=batch_size,
        source_parameters=source_parameters,
    )
    INTERFACES[destination_parameters["type"]]["destination"](
        destination_parameters=destination_parameters,
        target=target,
        batch_iterator=batch_iterator,
    )
