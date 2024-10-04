import pandas as pd
import geopandas as gpd
from sqlalchemy import text

from .geolevel import Geolevel
from .network import Network

class DistancierSession:
    # Constructor
    def __init__(
            self,
            session_id:int,
            name:str,
            engine:str,
            id_start:int,
            id_end:int,
            type_start:str,
            type_end:str,
            direction:str,
            max_distance:int,
            max_time:int,
            max_calc_out:int,
            no_route:bool,
            org:'Org' # type: ignore
    ):
        self._session_id = session_id
        self._name = name
        self._engine = engine
        self._id_start = id_start
        self._id_end = id_end
        self._type_start = type_start
        self._type_end = type_end
        self._direction = direction
        self._max_distance = max_distance
        self._max_time = max_time
        self._max_calc_out = max_calc_out
        self._no_route = no_route
        self._org = org

    # Getters and setters
    @property
    def session_id(self): return self._session_id
    @property
    def name(self): return self._name
    @property
    def engine(self): return self._engine
    @property
    def id_start(self): return self._id_start
    @property
    def id_end(self): return self._id_end
    @property
    def type_start(self): return self._type_start
    @property
    def type_end(self): return self._type_end
    @property
    def direction(self): return self._direction
    @property
    def max_distance(self): return self._max_distance
    @property
    def max_time(self): return self._max_time
    @property
    def max_calc_out(self): return self._max_calc_out
    @property
    def no_route(self): return self._no_route
    @property
    def org(self): return self._org

    # Magic Method
    def __str__(self) -> str:
        return f"DistancierSession({self._session_id} - {self._name})"
    
    # Public Methods
    def getStartingObject(self)->Network|Geolevel:
        if self._type_start == 'network':
            return self._org.getNetworkById(self._id_start)
        elif self._type_start == 'geolevel':
            return self._org.getGeolevelById(self._id_start)
        else:
            raise ValueError(f"Type start {self._type_start} doesn't exist.")
        
    def getEndingObject(self)->Network|Geolevel:
        if self._type_end == 'network':
            return self._orh.getNetworkById(self._id_end)
        elif self._type_end == 'geolevel':
            return self._org.getGeolevelById(self._id_end)
        else:
            raise ValueError(f"Type end {self.type_end} doesn't exist.")
        
    def getDistancier(self)->pd.DataFrame:
        # Query
        q = f"SELECT * FROM ggo_distancier WHERE session_id = {self._session_id}"
        # Df
        return self._org.query_df(q)
    
    def to_json(self):
        return {
            "session_id": self._session_id,
            "name": self.name,
            "engine": self._engine,
            "id_start": self._id_start,
            "id_end": self._id_end,
            "type_start": self._type_start,
            "type_end": self._type_end,
            "direction": self._direction,
            "max_distance": self._max_distance,
            "max_time": self._max_time,
            "max_calc_out": self._max_calc_out,
            "no_route": self._no_route
        }
    
    def getPoisIdList(self)->list:
        pois_ids_list = []
        if self._type_start == 'network':
            q = f"SELECT poi_id_start FROM ggo_distancier WHERE session_id = {self._session_id}"
            df = self._org.query_df(q)
            pois_ids_list += df['poi_id_start'].tolist()
        if self._type_end == 'network':
            q = f"SELECT poi_id_end FROM ggo_distancier WHERE session_id = {self._session_id}"
            df = self._org.query_df(q)
            pois_ids_list += df['poi_id_end'].tolist()
        return pois_ids_list
    
    def getGeounitCodeList(self)->list:
        geounit_code_list = []
        if self._type_start == 'geolevel':
            q = f"SELECT geounit_code_start FROM ggo_distancier WHERE session_id = {self._session_id}"
            df = self._org.query_df(q)
            geounit_code_list += df['geounit_code_start'].tolist()
        if self._type_end == 'geolevel':
            q = f"SELECT geounit_code_end FROM ggo_distancier WHERE session_id = {self._session_id}"
            df = self._org.query_df(q)
            geounit_code_list += df['geounit_code_end'].tolist()
        return geounit_code_list