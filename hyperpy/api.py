import requests
import os
import pandas as pd

# Set global variables
get_url = "https://api.hypercharts.co/beta/financials"
api_key = os.environ['hypercharts_key']


def get_dataframe(ticker):
    """
        This method will execute an https get request to the hypercharts api
        and cast the list returned to a pandas DataFrame.

        Args:
            ticker (str): ticker symbol

        Returns:
            DataFrame of ticker information
    """

    params = dict(
        symbol=ticker,
        apiKey=api_key)

    r = requests.get(get_url, params=params)

    return pd.DataFrame(r.json())


if __name__ == '__main__':
    # Test get function
    df = get_dataframe(ticker='amzn')
    print(df.head())