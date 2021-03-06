"""This module contains the general information for ComputeDomainQual ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ComputeDomainQualConsts():
    pass


class ComputeDomainQual(ManagedObject):
    """This is ComputeDomainQual class."""

    consts = ComputeDomainQualConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ComputeDomainQual", "computeDomainQual", "Domain-qualifier-[name]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin", "pn-policy", "read-only"], [u'computeQual'], [u'computeChassisQual', u'computeDomainGroupQual', u'computeDomainNameQual', u'computeOwnerQual', u'computeProductFamilyQual', u'computeRackQual', u'computeSiteQual', u'computeSystemAddrQual'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "ComputeDomainQual", parent_mo_or_dn, **kwargs)

