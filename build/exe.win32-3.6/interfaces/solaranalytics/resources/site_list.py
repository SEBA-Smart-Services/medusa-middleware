import falcon
import dicttoxml


class SiteListResource(object):
    """
    accepts request GET /solaranalytics/site_data/{site_id}

    fetches data from Solar Analytics API in JSON format
    converts to XML

    responds to client with site data XML for "site_id"

    accepts query parameters
    eg ?tstart=20150115&tend=20150120&gran=day&raw=true&trunc=false
    and simply appends to the request to Solar Analytics API

    """

    def __init__(self, solar_analytics_client):
        self.solar_analytics_client = solar_analytics_client

    def on_get(self, req, resp):
        """Handles GET requests"""

        print(req.query_string)
        # send request to from Solar Analytics API
        # gets JSON response
        site_data_json = self.solar_analytics_client.site_list(query_params=req.query_string)
        # convert JSON response to XML
        site_data_xml = dicttoxml.dicttoxml(site_data_json, attr_type=False)

        resp.status = falcon.HTTP_200  # This is the default status
        resp.set_header("Content-Type", "text/xml")
        resp.body = site_data_xml

        req_data = req.stream.read()
        print(req_data)
