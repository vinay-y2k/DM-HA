
import requests
from requests.exceptions import ConnectionError,Timeout,RequestException
import pandas as pd
import urllib3
import os

# This hides the messy console warnings about "Insecure Requests"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MY_API_KEY = os.environ.get('MY_API_KEY')

params = {'output' :'json',
          'X-API-KEY' : MY_API_KEY }
try:
    response = requests.get(url='https://ooavl-216-212-32-129.a.free.pinggy.link/get-data',params=params,verify=False)
    response.raise_for_status()

    # Check if 'gzip' is in the Content-Encoding header
    encoding = response.headers.get('Content-Encoding')

    if encoding == 'gzip':
        print(f"✅ Success! The data was compressed using: {encoding}")
    else:
        print("❌ The data was NOT compressed.")
        print(f"Current headers: {response.headers}")

    data = response.json()
    df = pd.DataFrame(data=data)
    print(df.info())    
except RequestException as e:
    print(f"Error {e} has occurred")
    


