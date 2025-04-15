from .property import Property
from ..zone_type import ZoneType

class ZoneTypeProperties:
    def __init__(
            self,
            zone_type: ZoneType,
            basic_zone_properties: list[Property],
            basic_zone_geounit_properties: list[Property],
            network_properties: list['NetworkProperties'] | None = None, # type: ignore
            geolevel_properties: list['GeolevelProperties'] | None = None, # type: ignore
        ):
        self._zone_type = zone_type
        self._basic_zone_properties = basic_zone_properties
        self._basic_zone_geounit_properties = basic_zone_geounit_properties
        self._network_properties = network_properties if network_properties else []
        self._geolevel_properties = geolevel_properties if geolevel_properties else []

    @property
    def zone_type(self): return self._zone_type
    @property
    def basic_zone_properties(self): return self._basic_zone_properties
    @property
    def basic_zone_geounit_properties(self): return self._basic_zone_geounit_properties
    @property
    def network_properties(self): return self._network_properties
    @property
    def geolevel_properties(self): return self._geolevel_properties
    @property
    def properties(self): 
        network_properties = [] 
        geolevel_properties = []
        for np in self._network_properties:
            network_properties += np.properties
        for gp in self._geolevel_properties:
            geolevel_properties += gp.properties
        return self._basic_zone_properties + self._basic_zone_geounit_properties + network_properties + geolevel_properties

    def sql_basic_zone_properties(self):
        list_sql = []
        if len(self._basic_zone_properties) == 0:
            return "z.*"
        for prop in self._basic_zone_properties:
            list_sql.append(f"{prop.to_sql(prefix='z')}")
        return ", ".join(list_sql)

    def sql_basic_zone_geounit_properties(self):
        list_sql = []
        if len(self._basic_zone_geounit_properties) == 0:
            return "zg.*"
        for prop in self._basic_zone_geounit_properties:
            list_sql.append(f"{prop.to_sql(prefix='zg')}")
        return ", ".join(list_sql)
    
    def to_sql(self):
        return ""