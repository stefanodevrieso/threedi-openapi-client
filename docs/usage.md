### ThreediApiClient


The main entry point to make api calls to the 3Di API V3.0. 

The `ThreediApiClient` class is the main entry point to make
api call to the 3DI API V3.0. It handles the login 
process for you and can be directly used as client for all API endpoints. 

The following three settings are necessary to make requests to the 3Di API:

  - the host name
  - the username to login with and 
  - the user's password

These settings can either be stored in a ".env" file
that can be passed to the `ThreediApiClient` on initialisation, supplied
via environment variables or passed as a config dictionairy.

1) A sample `.env` file could look like this

```
API_HOST=https://api.3di.live/v3.0
API_USERNAME=black.sheep
API_PASSWORD=myverysecretmehhh
```

```python
from threedi_api_client import ThreediApiClient

env_file = "<path>/.env"
api_client = ThreediApiClient(env_file=env_file)
```

2) The enviroment variables are the same as in the .env file:

```
export API_HOST=https://api.3di.live/v3.0
export API_USERNAME=black.sheep
export API_PASSWORD=myverysecretmehhh
```

3) The config keyword argument can be used like:


```python
from threedi_api_client import ThreediApiClient

config = {
    "API_HOST": "https://api.3di.live/v3.0",
    "API_USERNAME": "black.sheep",
    "API_PASSWORD": "myverysecretmehhh"
}

api_client = ThreediApiClient(config=config)
```


### Usage examples

Let's jump right in with an example. To get an instance of the client: 

```python
from threedi_api_client import ThreediApiClient
env_file = "<path>/.env"
api_client = ThreediApiClient(env_file)
```

Now you can easily make use of the api models generated by the openapi client.
Let us create a simulation. We will use a `Simulation` model instance to pass 
data to the API. Some fields are optional but we do need to specify 

- the unique organisation ID we want to run the simulation for 
- the model schema to use for the simulation by referring to the id of 
  the threedimodel resource       
- datetime (in ISO 8601 (UTC) format) for the simulation start
- either a end datetime (also in ISO 8601 (UTC) format) or the duration 
  parameter in seconds
  
  
If you do not know the unique ID for your organisation you can make use of the 
`OrganisationsApi` object that grants access to the `/organisations/` endpoint.         

```python
      
from openapi_client.api import OrganisationsApi

# first get the uuid for the organisation because I just keep forgetting it
from openapi_client.api import OrganisationsApi
organisations_api = OrganisationsApi(api_client)

# I am lazy so I look for an organisation that starts with "nelen", case insensitive 
organisations_api.organisations_list(name__istartswith="nelen")
{'count': 2,
'next': None,
'previous': None,
'results': [{'name': 'Nelen & Schuurmans',
      'unique_id': 'b8f91de705774fe8a4e7cb2d9413bf5c',
      'url': 'https://api.3di.live/v3.0/organisations/61f5a464c35044c19bc7d4b42d7f58cb/'},
     {'name': 'Nelen & Schuurmans alleen werknemers',
      'unique_id': 'e82c74c4fb5846b3ae990c0cc69130c6',
      'url': 'https://api.3di.live/v3.0/organisations/cde64bc165644be9af023fc4fa18d098/'}]}        
```

Now we can create the `Simulation` model instance.

```python
openapi_client.models.simulation.Simulation

# start date will be a datetime object
from datetime import datetime

my_extreme_event_simulation = Simulation(
        name="my extreme event",   # (optional)
        threedimodel=1,            # The model schema to use for the simulation by referring to the id of the threedimodel resource
        organisation='b8f91de705774fe8a4e7cb2d9413bf5c',  
        start_datetime=datetime.utcnow(),  # accepts datetime instance
        duration=7200              # in secs ==> 2 hours 
)
```

The SimulationsApi object gives use access to the `/simulations/`  endpoint.

```python
from openapi_client import SimulationsApi
simulations_api = SimulationsApi(api_client)

simulations_api.simulations_create(my_extreme_event_simulation)
{'created': 'now',
'duration': 7200,
'duration_humanized': '2 hours, 0 minutes, 0 seconds',
'end_datetime': '2019-11-04T16:19:46Z',
'id': 631,
'name': 'my extreme event',
'organisation': 'b8f91de705774fe8a4e7cb2d9413bf5c',
'organisation_name': 'Nelen & Schuurmans',
'slug': 'my-extreme-event-378f55a5-06df-4021-8fb6-65bbb70519dc',
'start_datetime': '2019-11-04T14:19:46Z',
'threedimodel': 'https://api.3di.live/v3.0/threedimodels/1/',
'threedimodel_id': '1',
'url': 'https://api.3di.live/v3.0/simulations/631/',
'user': 'lars.claussen',
'uuid': '378f55a5-06df-4021-8fb6-65bbb70519dc'}
```

Simulations allow for adding an arbitrary number of events to them like

- rain events
- sources and sinks
- initial conditions
- laterals
- saved states
- structure controls

All of them have their own openapi client model. To add a constant rain event 
to the simulation you would do the following.

```python

from openapi_client.models import ConstantRain
const_rain = ConstantRain(
    simulation=631,   # the ID we got from our create call above
    offset=60,        # let the rain start after one minute
    duration=5000,    # let the rain last for 5000 secs
    value=0.0006,     # not too extreme after all...;-)
    units="m/s"       # the only unit supported for now
)
simulations_api.simulations_events_rain_constant_create(631, const_rain)
{'duration': 5000,
'offset': 60,
'simulation': 'https://api.3di.live/v3.0/simulations/631/',
'units': 'm/s',
'url': 'https://api.3di.live/v3.0/simulations/631/events/rain/constant/17/',
'value': 0.0006}
``` 
 
If you want to see which events are defined on a given simulation
```python
simulations_api.simulations_events(631)
{'boundaries': None,
'breach': [],
'filerasterrain': [],
'filerastersourcessinks': [],
'filetimeseriesrain': [],
'filetimeseriessourcessinks': [],
'initial_groundwaterlevel': None,
'initial_onedwaterlevel': None,
'initial_onedwaterlevelpredefined': None,
'initial_savedstate': None,
'initial_twodwaterlevel': None,
'laterals': [],
'lizardrasterrain': [],
'lizardrastersourcessinks': [],
'lizardtimeseriesrain': [],
'lizardtimeseriessourcessinks': [],
'savedstates': [],
'timedstructurecontrol': [],
'timeseriesrain': [{'constant': True,
                'duration': 5000,
                'interpolate': False,
                'offset': 60,
                'simulation': 'https://api.3di.live/v3.0/simulations/631/',
                'units': 'm/s',
                'url': 'https://api.3di.live/v3.0/simulations/631/events/rain/timeseries/17/',
                'values': [[0.0, 0.0006], [5000.0, 0.0]]}],
'timeseriessourcessinks': []}
```

To list all file resources get yourself an instance of the `FilesApi` class

```python
    files = FilesApi(api_client)
    files.files_list()                                                                                                                
    {'count': 3064,
    'next': 'https://api.3di.live/v3.0/files/?limit=10&offset=10',
    'previous': None,
    'results': [{'bucket': '3di',
            'etag': None,
            'expiry_date': '2019-08-16',
            'filename': 'precipitation_1.nc',
            'id': 2,
            ..
``` 


### Advanced usage

Upload example (rain raster upload). You need to install the python 
`requests` library to run this example.

   
```python
import requests
from openapi_client import SimulationsApi

simulation_pk = 1
filename = 'bergermeer_rasters_from_geotiffs.nc'
local_file_path = './data/bergermeer_rasters_from_geotiffs.nc'

# Use the api_client as created in the code block
# above
sim_api = SimulationsApi(api_client)

# Create rain raster upload resource in API
# returns a 'file_upload' instance containing a
# put_url property which is the URL to the object
# storage object to be uploaded with an HTTP PUT requests.
file_upload = sim_api.simulations_events_rain_rasters_upload(
    filename, simulation_pk)

# Open the local file in binary mode for uploading
with open(local_file_path, 'rb') as f: 
    # Requests automatically streams the file this way
    requests.put(file_upload.put_url, data=f)
```


### Async client

The ThreediApiClient also provides an asynchronous api client. To use the async-client 
make sure you import from the `aio` submodule. The async-client works the same as the 
synchronous client, except all api calls are coroutines.

For example, to asynchronously request files from the api:

```python
import asyncio

from openapi_client.api.files_api import FilesApi
from threedi_api_client.aio.threedi_api_client import ThreediApiClient


config = {
    "API_HOST": "https://api.3di.live/v3.0",
    "API_USERNAME": "black.sheep",
    "API_PASSWORD": "myverysecretmehhh"
}


async def main():
    async with ThreediApiClient(config=config) as api_client:
        files_api = FilesApi(api_client)
        print(await files_api.files_list())


if __name__ == '__main__':
    asyncio.run(main())
```
