import pandas as pd
from sqlalchemy import text

class Zone:
    # Constructor
    def __init__(
        self,
        zone_id:int,
        properties:dict,
        geolevel_id:int,
        zone_type_id:int,
        poi_id:int,
        parent_zone_id:int,
        org:'Org'
    ):
        # Infos
        self._zone_id = zone_id
        self._properties = properties
        self._geolevel_id = geolevel_id
        self._zone_type_id = zone_type_id
        self._poi_id = poi_id
        self._parent_zone_id = parent_zone_id
        # Engine
        self._org = org