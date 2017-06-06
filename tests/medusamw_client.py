import requests
import json

def request(base_url, resource, port=80, headers=None, params=None, body=None):
    """
    base method for all requests
    pass in resource, headers, params and body as per resource requirement
    """
    url = make_url(base_url, resource, port)
    print(url)
    response = requests.get(url, headers=headers, params=params, data=json.dumps(body))
    self.last_response = response.text
    # check HTTP response is in 2xx range
    if response.status_code in range(200, 300):
        resp_json = json.loads(response.text)
        return resp_json
    else:
        print("Request failed with status code " + str(response.status_code))
        return None

def make_url(BASE_URL, resource, port='80'):
    """
    returns complete url for a resource
    """
    return BASE_URL + ':' +str(port) + resource


if __name__ == '__main__':

    resource = '/test'
    port = '8069'
    base_url = "http://127.0.0.1"
    url = make_url(base_url, resource, port)
    print(url)

    response = requests.get(url)
    print(response.text)

    site_data_url = make_url(base_url, '/solaranalytics/site_data/23511', port=8069)
    print(site_data_url)
    site_data_resp = requests.get(site_data_url)
    print('\nsite_data:\n')
    print(site_data_resp.text)
