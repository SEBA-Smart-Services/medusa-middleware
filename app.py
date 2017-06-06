import falcon
import dicttoxml
from wsgiref import simple_server
from waitress import serve
import configparser
import os
from interfaces.solaranalytics import SiteDataResource, SiteListResource, TokenResource
from interfaces.solaranalytics.client import SolarAnalyticsAPI

###################################
# load config

# config file location
DATA_DIR = '%programdata%\\Schneider Electric\\Medusa Middleware\\'
CONFIG_FILE = 'config.ini'

def get_abspath_programdata(path):
    """
    converts %programdata% path variable to system absolute path
    returns absolute path str

    """ 
    return path.lower().replace('%programdata%', os.environ['ProgramData'])

def make_dir(path):
    """
    makes directory when path includes %programdata% path variable
    if not exists

    """
    abspath = get_abspath_programdata(path)
    if not os.path.exists(abspath):
            os.makedirs(abspath)    

# make ProgramData directory for config
make_dir(get_abspath_programdata(DATA_DIR))

# create ConfigParser object
config = configparser.ConfigParser()

# read in config from config files
master_config_file = get_abspath_programdata(DATA_DIR) + CONFIG_FILE
config.read(master_config_file)


###################################
# create Solar Analytics API client
# instantiate SolarAnalyticsAPI first
# so that falcon resources can access it

# config data here temporarily
solar_analytics_client = SolarAnalyticsAPI()
solar_analytics_username = config.get('Solar Analytics', 'username')
solar_analytics_password = config.get('Solar Analytics', 'password')
solar_analytics_site_id = config.get('Solar Analytics', 'site_id')

# authenticate
solar_analytics_client.auth(
    solar_analytics_username,
    solar_analytics_password
)


##################################
# Falcon API

app = application = falcon.API()

# make resources
token = TokenResource()
site_data = SiteDataResource(solar_analytics_client)
site_list = SiteListResource(solar_analytics_client)

# make routes
app.add_route('/solaranalytics/token', token)
app.add_route('/solaranalytics/site_list', site_list)
app.add_route('/solaranalytics/site_data/{site_id}', site_data)


##################################
# serve forever
if __name__ == '__main__':
    host = config.get('Middleware', 'host')
    port = config.get('Middleware', 'port')
    serve(app, host=host, port=port)
    
    # used for testing: try httpd if waitress.serve not working
    # httpd = simple_server.make_server('127.0.0.1', port, app)
    # httpd.serve_forever()
