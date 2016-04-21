"""This module contains the general information for NetworkSystemCACert ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class NetworkSystemCACertConsts():
    pass


class NetworkSystemCACert(ManagedObject):
    """This is NetworkSystemCACert class."""

    consts = NetworkSystemCACertConsts()
    naming_props = set([])

    mo_meta = MoMeta("NetworkSystemCACert", "networkSystemCACert", "system-ca-cert", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin", "read-only"], [u'networkElement'], [], [None])

    prop_meta = {
        "checksum": MoPropertyMeta("checksum", "checksum", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "checksum": "checksum", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.checksum = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "NetworkSystemCACert", parent_mo_or_dn, **kwargs)
