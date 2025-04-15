from .property import Property
from ..distancier_session import DistancierSession

class DistancierProperties:
    def __init__(
            self,
            distancier_session: DistancierSession,
            basic_distancier_properties: list[Property],
            geolevel_properties: list['GeolevelProperties'] | None = None, # type: ignore
            network_properties: list['NetworkProperties'] | None = None # type: ignore
            ):
        self._distancier_session = distancier_session
        self._distancier_properties = basic_distancier_properties
        self._geolevel_properties = geolevel_properties if geolevel_properties else []
        self._network_properties = network_properties if network_properties else []

    @property
    def distancier_session(self): return self._distancier_session
    @property
    def distancier_properties(self): return self._distancier_properties
    @property
    def geolevel_properties(self): return self._geolevel_properties
    @property
    def network_properties(self): return self._network_properties
    @property
    def properties(self):
        return self._distancier_properties + self._geolevel_properties + self._network_properties

    def sql_distancier_properties(self):
        list_sql = []
        if len(self._distancier_properties) == 0:
            return "ds.*"
        for prop in self._distancier_properties:
            list_sql.append(f"{prop.to_sql(prefix='ds')}")
        return ", ".join(list_sql)