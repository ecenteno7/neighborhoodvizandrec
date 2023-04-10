
import pandas as pd
import pyarrow.parquet as pq


def convert_pq_to_csv(filename):

    print("Converting "+filename+" to csv.")
    # Read the Parquet file into a Pandas DataFrame
    parquet_file = pq.ParquetFile(filename)
    df = parquet_file.read().to_pandas()

    output_name = filename[:-7]+'csv'
    # Write the DataFrame to a CSV file
    df.to_csv(output_name, index=False)


    print(output_name + "  written")
    return

# filename = "flask//data//nyc/yellow_tripdata_2022-01.parquet"   # NYC yellow cab data
filename = "flask//data//nyc/fhvhv_tripdata_2022-01.parquet"    #for hire high volume data

convert_pq_to_csv(filename)