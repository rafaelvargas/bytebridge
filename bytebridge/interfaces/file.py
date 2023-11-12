from typing import Iterator, List

import pyarrow
from pyarrow import parquet


def fetch(
    *,
    connection_type: str,
    source_object: str,
    source_query: str,
    batch_size: int,
    source_parameters: dict = None,
) -> Iterator[List[dict]]:
    parquet_file = parquet.ParquetFile(source_object)
    for batch in parquet_file.iter_batches(batch_size=batch_size):
        yield batch.to_pylist()


def load(
    *,
    connection_type: str,
    target_object: str,
    batch_iterator: Iterator[dict],
    destination_parameters: str,
):
    first_batch = next(batch_iterator)
    if first_batch:
        record_batch = pyarrow.RecordBatch.from_pylist(first_batch)
        with parquet.ParquetWriter(target_object, record_batch.schema) as writer:
            writer.write_batch(record_batch)
            for batch in batch_iterator:
                writer.write_batch(batch=pyarrow.RecordBatch.from_pylist(batch))
