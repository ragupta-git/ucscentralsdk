"""This module contains the general information for ComputeEnvFeatMask ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ComputeEnvFeatMaskConsts():
    pass


class ComputeEnvFeatMask(ManagedObject):
    """This is ComputeEnvFeatMask class."""

    consts = ComputeEnvFeatMaskConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeEnvFeatMask", "computeEnvFeatMask", "env-feat-mask", VersionMeta.Version112a, "InputOutput", 0xf, [], ["read-only"], [u'computeSystem', u'extpolDomain', u'lsServer'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feat_mask": MoPropertyMeta("feat_mask", "featMask", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|remote_operation_feature_mask|ucs_registration_feature_mask|power_group_feature_mask|estimate_impact_on_reconnect_feature_mask|health_reporting_feature_mask|dc_power_group_feature_mask),){0,7}(defaultValue|none|remote_operation_feature_mask|ucs_registration_feature_mask|power_group_feature_mask|estimate_impact_on_reconnect_feature_mask|health_reporting_feature_mask|dc_power_group_feature_mask){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "featMask": "feat_mask", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.feat_mask = None
        self.status = None

        ManagedObject.__init__(self, "ComputeEnvFeatMask", parent_mo_or_dn, **kwargs)

