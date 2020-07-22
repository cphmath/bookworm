from sodapy import Socrata


def create_client(app_token=None, timeout=180):
    """
    Return a Socrata client to query data.seattle.gov and reset the
    timeout to 180 seconds if nothing is specified
    """
    client = Socrata("data.seattle.gov", app_token)
    client.timeout = timeout
    return client


def query_data(client, dataset_id, query):
    """
    Take a data.seattle.gov Socrata client and a SOQL query and return
    a pandas dataframe with the appropriate data.
    """
    return client.get(dataset_id, query=query)


def get_book_checkouts_by_month()
