# ByteBridge

A data tool designed to move data seamlessly between various sources and destinations.

## Command Line Interface


### Extracting using SQL queries

```bash
bytebridge transfer 
    --source postgres 
    --query extraction_query.sql 
    --destination parquet 
    --map "ColumnA:column_a,ColumnB:column_b" 
```


## Data Interfaces

### Currently Supported

| Name             | Type          |
|----------------- | --------------|
| PostgreSQL       | Database      |
| Parquet          | File          |



### Planned

| Name             | Type          |
|----------------- | --------------|
| MySQL            | Database      |
| SQLite           | Database      |
| SQL Server       | Database      |
| Oracle           | Database      |
| Clickhouse       | Database      |
| Parquet          | File          |
| CSV              | File          |
| ORC              | File          |
| Avro             | File          |
| Excel (XLSX)     | File          |