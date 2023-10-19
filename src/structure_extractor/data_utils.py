import io
import os
import pandas as pd
import re
import requests
import zipfile

from .config import Configuration as cfg

def unzip_from_url(src, dest="./"):
    zip_data = requests.get(src)
    zip = zipfile.ZipFile(io.BytesIO(zip_data.content))
    zip.extractall(dest)
    print("Download and Unzip complete")

def combine_csv_files(folder_path, retrieve_label=True, retrieve_year=True,
                      retrieve_country=True, retrieve_event=True, min_tweet_len=6):
    df = pd.DataFrame()
    file_suffix=".csv"

    # Find all files in folder and subfolders
    for root, _, files in os.walk(folder_path):
        for file in files:
            # If the file is a CSV file get date
            if file.endswith(file_suffix) and 'labeled' in file.lower():        
                file_path = os.path.join(root, file)
                csv_df = pd.read_csv(file_path)

                label=os.path.basename(os.path.dirname(file_path))

                # If min tweet length is zero then nothing to do else exlcude these records
                if min_tweet_len != 0:
                    csv_df=csv_df[csv_df.apply(lambda x: _get_message_length(x["Tweet Text"])>=min_tweet_len, axis=1)]

                # Get the subfolder and store as the label
                if retrieve_label:
                    csv_df["label"]=label
                
                # Get the year of the event from the label
                if retrieve_year:
                    csv_df["year"]=_get_year_of_crisis(label)

                if retrieve_country:
                    csv_df["country_code"]=_get_country_of_crisis(label)

                if retrieve_event:
                    csv_df["crisis_type"]=_get_crisis_type(label)
                
                # Concatenate new csv data to data frame
                df=pd.concat([df, csv_df])

    return df


def _get_year_of_crisis(crisis):
    year=crisis[0:4]
    return year


def _get_country_of_crisis(crisis):
    mapping = cfg.countries
    country = mapping[crisis]
    return country


def _get_crisis_type(crisis):
    mapping = cfg.crisis_type
    event = mapping[crisis]
    return event


def _get_message_length(message):
    words=re.sub(r'#\S+|@\S+|http\S+', '', message).split()
    num_of_words=len(words)
    return num_of_words