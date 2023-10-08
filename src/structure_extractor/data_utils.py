import io
import requests
import zipfile


def unzip_from_url(src, dest="./"):
    zip_data = requests.get(src)
    zip = zipfile.ZipFile(io.BytesIO(zip_data.content))

    zip.extractall("content/crisis_data")