from typing import Iterator

import pyarrow
from pyarrow import parquet


def load(*, filepath: str, batch_iterator: Iterator[dict]):
    first_batch = next(batch_iterator)
    if first_batch:
        record_batch = pyarrow.RecordBatch.from_pylist(first_batch)
        with parquet.ParquetWriter(filepath, record_batch.schema) as writer:
            writer.write_batch(record_batch)
            for batch in batch_iterator:
                writer.write_batch(batch=pyarrow.RecordBatch.from_pylist(batch))
