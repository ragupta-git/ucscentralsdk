"""This module contains the general information for LstorageRequestCtx ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class LstorageRequestCtxConsts():
    pass


class LstorageRequestCtx(ManagedObject):
    """This is LstorageRequestCtx class."""

    consts = LstorageRequestCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageRequestCtx", "lstorageRequestCtx", "", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "assigned_volume": MoPropertyMeta("assigned_volume", "assignedVolume", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_dn": MoPropertyMeta("cons_dn", "consDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "request_size": MoPropertyMeta("request_size", "requestSize", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "volume_pool_name": MoPropertyMeta("volume_pool_name", "volumePoolName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "assignedVolume": "assigned_volume", 
        "childAction": "child_action", 
        "consDn": "cons_dn", 
        "dn": "dn", 
        "requestSize": "request_size", 
        "rn": "rn", 
        "status": "status", 
        "volumePoolName": "volume_pool_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.assigned_volume = None
        self.child_action = None
        self.cons_dn = None
        self.request_size = None
        self.status = None
        self.volume_pool_name = None

        ManagedObject.__init__(self, "LstorageRequestCtx", parent_mo_or_dn, **kwargs)

