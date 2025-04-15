from ..geolevel import Geolevel
from .property import Property

class GeolevelProperties:
    # Constructor
    def __init__(self, geolevel: Geolevel, geoleveldata_type_properties: list['GeoleveldataTypeProperties']): # type: ignore
        self._geolevel = geolevel
        self._geoleveldata_type_properties = geoleveldata_type_properties if geoleveldata_type_properties else []

    # Getters and setters
    @property
    def geolevel(self): return self._geolevel
    @property
    def geoleveldata_type_properties(self): return self._geoleveldata_type_properties
    @property
    def properties(self):
        geoleveldata_type_properties = []
        for gdtp in self._geoleveldata_type_properties:
            geoleveldata_type_properties += gdtp.properties
        return geoleveldata_type_properties

    def sql_geoleveldata_type_properties(self):
        list_sql = []
        if len(self._geoleveldata_type_properties) == 0:
            return "gd.*"
        for prop in self._geoleveldata_type_properties:
            list_sql.append(f"{prop.to_sql(prefix='gd')}")
        return ", ".join(list_sql)
    
    def to_sql(self):
        q = f"""
        SELECT
            {self.sql_geoleveldata_type_properties()}
        FROM ggo_geoleveldata AS gd
        WHERE gd.geoleveldata_type_id = {self._geolevel.geoleveldata_type_id}
        """
        return q