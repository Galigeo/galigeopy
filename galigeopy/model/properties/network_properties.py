from .property import Property
from .zone_type_properties import ZoneTypeProperties
from .distancier_properties import DistancierProperties
from ..network import Network

class NetworkProperties:
    def __init__(self, network: Network, basic_network_properties: list[Property], zone_type_properties: list[ZoneTypeProperties], distancier_properties: list[DistancierProperties]):
        self._network = network
        self._basic_network_properties = basic_network_properties
        self._zone_type_properties = zone_type_properties
        self._distancier_properties = distancier_properties

    @property
    def network(self): return self._network
    @property
    def basic_network_properties(self): return self._basic_network_properties
    @property
    def zone_type_properties(self): return self._zone_type_properties
    @property
    def distancier_properties(self): return self._distancier_properties
    @property
    def properties(self):
        return self._basic_network_properties + [zt.properties for zt in self._zone_type_properties]
    
    def sql_basic_network_properties(self):
        list_sql = []
        if len (self._basic_network_properties) == 0:
            return "p.*"
        for prop in self._basic_network_properties:
            list_sql.append(f"{prop.to_sql(prefix='p')}")
        return ", ".join(list_sql)
    
    def to_sql(self):
        q = f"""
        SELECT
            {self.sql_basic_network_properties()}
        FROM ggo_poi AS p
        WHERE p.network_id = {self._network.network_id}
        """
        return q
    