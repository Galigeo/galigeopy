import pandas as pd
from sqlalchemy import text


class ZoneType:
    def __init__(
        self,
        zone_type_id:int,
        name:str,
        org: 'Org'
    ):
        # Infos
        self._zone_type_id = zone_type_id
        self._name = name
        # Engine
        self._engine = org.engine

    def __str__(self):
        return self.name + " (" + str(self.zone_type_id) + ")"
    
    # Getters and setters
    @property
    def zone_type_id(self): return self._zone_type_id
    @property
    def name(self): return self._name
    
    # Public Methods
    def number_of_zones(self):
        query = text(f"SELECT COUNT(*) FROM ggo_zone WHERE zone_type_id = {self.zone_type_id}")
        with self._engine.connect() as conn:
            result = conn.execute(query)
            return result.scalar()
        
    def getZonesList(self):
        query = text(f"SELECT * FROM ggo_zone WHERE zone_type_id = {self.zone_type_id}")
        return pd.read_sql(query, self._engine)