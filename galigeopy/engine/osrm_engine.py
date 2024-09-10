import requests

class OsrmEngine:
    def __init__(self, osrm_url:str, verified_url:bool=True):
        self._osrm_url = osrm_url
        self._verified_url = verified_url

    # Getters and setters
    @property
    def osrm_url(self): return self._osrm_url
    @property
    def verified_url(self): return self._verified_url

    def get_route(self, start, end,
        alternatives:bool=False,
        steps:bool=False,
        annotations:bool=False,
        geometries:str="polyline",
        overview:str="simplified",
        continue_straight:str="default",

    )->list:
        url = f"{self.osrm_url.removesuffix('/')}/route/v1/driving/{start['lng']},{start['lat']};{end['lng']},{end['lat']}"
        # Properties
        url += f"?alternatives={str(alternatives).lower()}"
        url += f"&steps={str(steps).lower()}"
        url += f"&annotations={str(annotations).lower()}"
        url += f"&geometries={geometries}"
        url += f"&overview={overview}"
        url += f"&continue_straight={continue_straight}"
        response = requests.get(url, verify=self.verified_url)
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        data = response.json()
        if data["code"] != "Ok":
            raise Exception(f"Error {data['code']}: {data['message']}")
        return data["routes"]
    
