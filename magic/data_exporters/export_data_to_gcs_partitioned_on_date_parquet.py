import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["GCP_SERVICE_ACCOUNT_PATH"]

bucket_name = "mage-storage-data-engineering" 
project_id = "testapp-322c6"

table_name = "nyc_taxi_table"

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    data["tpep_pickup_date"] = data["tpep_pickup_datetime"].dt.date
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=["tpep_pickup_date"],
        filesystem=gcs
    )