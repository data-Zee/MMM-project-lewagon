import pandas as pd

from google.cloud import bigquery
#from colorama import Fore, Style
#from pathlib import Path

from mmmproject.model.params import *

def get_data(csv_path: str):
    df = pd.read_csv(csv_path)
    df = df.drop(columns='Unnamed: 0')
    df['Day'] = pd.to_datetime(df['Day'])
    df.set_index('Day', inplace=True)
    df = df.rename(columns={"fb_costs": "facebook", "google_costs": "google", "tt_costs": "tiktok"})

    # create a simple_df
    simple_df = df.drop(columns = ['fb_impressions', 'fb_clicks', 'google_impressions', 'google_clicks', 'tt_impressions', 'tt_clicks'])
    X_simple = simple_df.drop(columns = ['orders', 'total_sales']) # 2 channels: facebook and google
    y_simple = simple_df['total_sales'] # for now lets just use total_sales and exclude orders

    print("✅ data cleaned")

    return X_simple, y_simple



# def get_data_with_cache(
#         gcp_project:str,
#         query:str,
#         cache_path:Path,
#         data_has_header=True
#     ) -> pd.DataFrame:
#     """
#     Retrieve `query` data from BigQuery, or from `cache_path` if the file exists
#     Store at `cache_path` if retrieved from BigQuery for future use
#     """
#     if cache_path.is_file():
#         print(Fore.BLUE + "\nLoad data from local CSV..." + Style.RESET_ALL)
#         df = pd.read_csv(cache_path, header='infer' if data_has_header else None)
#     else:
#         print(Fore.BLUE + "\nLoad data from BigQuery server..." + Style.RESET_ALL)
#         client = bigquery.Client(project=gcp_project)
#         query_job = client.query(query)
#         result = query_job.result()
#         df = result.to_dataframe()

#         # Store as CSV if the BQ query returned at least one valid line
#         if df.shape[0] > 1:
#             df.to_csv(cache_path, header=data_has_header, index=False)

#     print(f"✅ Data loaded, with shape {df.shape}")

#     return df

# def load_data_to_bq(
#         data: pd.DataFrame,
#         gcp_project:str,
#         bq_dataset:str,
#         table: str,
#         truncate: bool
#     ) -> None:
#     """
#     - Save the DataFrame to BigQuery
#     - Empty the table beforehand if `truncate` is True, append otherwise
#     """

#     assert isinstance(data, pd.DataFrame)
#     full_table_name = f"{gcp_project}.{bq_dataset}.{table}"
#     print(Fore.BLUE + f"\nSave data to BigQuery @ {full_table_name}...:" + Style.RESET_ALL)

#     # Load data onto full_table_name

#     # 🎯 HINT for "*** TypeError: expected bytes, int found":
#     # After preprocessing the data, your original column names are gone (print it to check),
#     # so ensure that your column names are *strings* that start with either
#     # a *letter* or an *underscore*, as BQ does not accept anything else

#     client = bigquery.Client()

#     write_mode = "WRITE_TRUNCATE" # or "WRITE_APPEND"
#     job_config = bigquery.LoadJobConfig(write_disposition=write_mode)
#     data.columns = [str(x) for x in data.columns]
#     job = client.load_table_from_dataframe(data, table, job_config=job_config)
#     result = job.result()

#     print(f"✅ Data saved to bigquery, with shape {data.shape}")
