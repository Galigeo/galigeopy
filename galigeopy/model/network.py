import pandas as pd
import geopandas as gpd
from shapely import wkt

from galigeopy.model.poi import Poi

class Network:
    # Constructor
    def __init__(
            self,
            network_id:int,
            org_id:int,
            name:str,
            brand:str,
            network_type_id:str,
            is_default:bool,
            created_at:str,
            created_by:str,
            last_updated_at:str,
            last_updated_by:str,
            geolevel_id:int,
            org:any
    ):
        # Infos
        self._network_id = network_id
        self._org_id = org_id
        self._name = name
        self._brand = brand
        self._network_type_id = network_type_id
        self._is_default = is_default
        self._created_at = created_at
        self._created_by = created_by
        self._last_updated_at = last_updated_at
        self._last_updated_by = last_updated_by
        self._geolevel_id = geolevel_id
        self._engine = org.engine

    # Getters and setters
    @property
    def network_id(self): return self._network_id
    @property
    def org_id(self): return self._org_id
    @property
    def name(self): return self._name
    @property
    def brand(self): return self._brand
    @property
    def network_type_id(self): return self._network_type_id
    @property
    def is_default(self): return self._is_default
    @property
    def created_at(self): return self._created_at
    @property
    def created_by(self): return self._created_by
    @property
    def last_updated_at(self): return self._last_updated_at
    @property
    def last_updated_by(self): return self._last_updated_by
    @property
    def geolevel_id(self): return self._geolevel_id

    # Magic Methods
    def __str__(self):
        return f"Network({self._network_id}, {self._name}, {self._brand})"
    
    # Public Methods
    def getPoisList(self)->gpd.GeoDataFrame:
        # Query
        query = f"SELECT * FROM ggo_poi WHERE network_id = {self._network_id}"
        # Get data from query
        gdf = gpd.read_postgis(query, self._engine, geom_col="geom")
        # return df
        return gdf
    
    def getPoiByCode(self, code:str)->Poi:
        # Query
        query = f"SELECT * FROM ggo_poi WHERE id = '{code}'"
        gdf = gpd.read_postgis(query, self._engine, geom_col="geom")
        # Data
        if len(gdf) > 0:
            data = gdf.iloc[0].to_dict()
            data.update({"network": self})
            return Poi(**data)
        else:
            raise Warning(f"Poi with code {code} not found in Network {self._name}")
        