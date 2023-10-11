import io
import os
import pandas as pd
import requests
import zipfile

from src.configuration.config import Configuration as cfg

def unzip_from_url(src, dest="./"):
    zip_data = requests.get(src)
    zip = zipfile.ZipFile(io.BytesIO(zip_data.content))
    zip.extractall(dest)
    print("Download and Unzip complete")

def combine_csv_files(folder_path, retrieve_label=True, retrieve_country=True):
    df = pd.DataFrame()
    file_suffix=".csv"

    # Find all files in folder and subfolders
    for root, _, files in os.walk(folder_path):
        for file in files:
            # If the file is a CSV file get date
            if file.endswith(file_suffix) and 'labeled' in file.lower():        
                file_path = os.path.join(root, file)
                csv_df = pd.read_csv(file_path)

                # Get the subfolder and store as the label
                if retrieve_label:
                    label=os.path.basename(os.path.dirname(file_path))
                    csv_df["label"]=label
                
                if retrieve_country:
                    csv_df=csv_df.assign(country_code=lambda x: _get_country_of_crisis(csv_df["label"]))
                
                # Concatenate new csv data to data frame
                df=pd.concat([df, csv_df])

    return df


def _get_country_of_crisis(crisis):
    mapping = cfg.countries
    country = crisis.map(mapping)
    return country