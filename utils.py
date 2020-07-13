from sodapy import Socrata

def create_client(app_token=None, timeout=180):
    """
    Returns a Socrata client to query data.seattle.gov and resets the
    timeout to 180 seconds if nothing is specified
    """
    client = Socrata("data.seattle.gov", app_token)
    client.timeout=timeout
    return client

def query_checkout_data(client, query, )
