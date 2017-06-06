import requests
import base64
import json
import datetime as dt


class SolarAnalyticsAPI():

    def __init__(self):
        BASE_URL =  "https://portal.solaranalytics.com.au/api/v2/"
        self.BASE_URL = BASE_URL
        self.last_response = None
        self.token = {
            "value": None,
            "expiry": None
        }

    def make_url(self, resource):
        """
        returns complete url for a resource
        """
        return self.BASE_URL + resource[1:]

    def request(self, resource, headers=None, params=None, body=None):
        """
        base method for all requests
        pass in resource, headers, params and body as per resource requirement
        """
        url = self.make_url(resource)
        response = requests.get(url, headers=headers, params=params, data=json.dumps(body))
        self.last_response = response.text
        # check HTTP response is in 2xx range
        if response.status_code in range(200, 300):
            resp_json = json.loads(response.text)
            return resp_json
        else:
            print("Request failed with status code " + str(response.status_code))
            return None

    def create_auth_header(self, use_token=True, username=None, password=None):
        """
        returns a dict containing Authorization header.
        if use_token = True, returns:
            {
                "Authorization": "Basic base64(<token value>:x)"
            }
        if use_token = False, returns:
            {
                "Authorization": "Basic base64(<username>:<password>)"
            }
        """
        auth_value = 'Basic '
        if use_token:
            challenge = self.token['value']
            answer = 'x'
        else:
            challenge = username
            answer = password

        # python version compatibility!
        # python 2 base64.b64encode() accepts string
        # python 3 base64.b64encode() requires bytes object
        try:
            auth_value += base64.b64encode(':'.join([challenge, answer]))
        except:
            unencoded = ':'.join([challenge, answer])
            print(unencoded)
            encoded = base64.b64encode(unencoded.encode('ascii'))
            auth_value += encoded.decode()
        return {'Authorization': str(auth_value)}

    def calc_expiry(self, start, duration):
        """
        calculate token expiry based on:
        start datetime
        token duration in seconds
        """
        expiry = start + dt.timedelta(seconds=int(duration))
        return expiry

    ###################################################################
    # requests
    ###################################################################
    def auth(self, username, password):
        """
        auth request
        """
        resource = "/token"
        # create authorisation header
        headers = self.create_auth_header(
            use_token=False,
            username=username,
            password=password
        )
        # get dt immediately prior to request to calculate token expiry
        start = dt.datetime.now()
        # make auth request
        print("\nrequesting authorisation token:")
        response = self.request(resource, headers)
        # check response
        if response is not None:
            self.token['value'] = response['token']
            expiry = self.calc_expiry(start, response['duration'])
            self.token['expiry'] = expiry

    def site_list(self):
        """
        site_list request
        """
        resource = "/site_list"
        # create authorisation header
        headers = self.create_auth_header()
        # make request
        print("\nrequesting site_list:")
        response = self.request(resource, headers)
        # check HTTP response is in 2xx range
        if response is not None:
            return response

    def site_data(self, site_id):
        """
        site_data request
        """
        resource = '/'.join(['/site_data', str(site_id)])
        # create authorisation header
        headers = self.create_auth_header()
        # make request
        print("\nrequesting site_data for site_id " + str(site_id) + ":")
        response = self.request(resource, headers)
        # check HTTP response is in 2xx range
        if response is not None:
            return response


# testing
if __name__ == '__main__':
    
    print("Testing")

    api = SolarAnalyticsAPI()
    api.auth("test@example.com", "password")
    print(api.token)
    site_list = api.site_list()

    for site in site_list['data']['sites']:
        print(site['site_name'])
        print('\n')
    print(site_list)

    site_id = 1
    site_data = api.site_data(site_id)
    print(site_data)