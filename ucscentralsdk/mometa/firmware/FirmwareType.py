"""This module contains the general information for FirmwareType ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class FirmwareTypeConsts():
    EP_ADAPTOR = "adaptor"
    EP_BLADE_BIOS = "blade-bios"
    EP_BLADE_CONTROLLER = "blade-controller"
    EP_BOARD_CONTROLLER = "board-controller"
    EP_CATALOG = "catalog"
    EP_CMC = "cmc"
    EP_CORE = "core"
    EP_DEBUG_PLUG_IN = "debug-plug-in"
    EP_DIAG = "diag"
    EP_FEX = "fex"
    EP_FLEXFLASH_CONTROLLER = "flexflash-controller"
    EP_GRAPHICS_CARD = "graphics-card"
    EP_HOST_HBA = "host-hba"
    EP_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    EP_HOST_NIC = "host-nic"
    EP_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    EP_IDENTIFIER_MGR = "identifier-mgr"
    EP_IOCARD = "iocard"
    EP_LOCAL_DISK = "local-disk"
    EP_MGMT_EXT = "mgmt-ext"
    EP_OPERATION_MGR = "operation-mgr"
    EP_POLICY_MGR = "policy-mgr"
    EP_PROVIDER = "provider"
    EP_PSU = "psu"
    EP_RESOURCE_AGGR = "resource-aggr"
    EP_SAS_EXPANDER = "sas-expander"
    EP_SERVICE_REG = "service-reg"
    EP_STATS_MGR = "stats-mgr"
    EP_STORAGE_BROKER = "storage-broker"
    EP_STORAGE_CONTROLLER = "storage-controller"
    EP_SWITCH = "switch"
    EP_SWITCH_KERNEL = "switch-kernel"
    EP_SWITCH_SOFTWARE = "switch-software"
    EP_SYSTEM = "system"
    EP_UNSPECIFIED = "unspecified"


class FirmwareType(ManagedObject):
    """This is FirmwareType class."""

    consts = FirmwareTypeConsts()
    naming_props = set([u'invTag'])

    mo_meta = MoMeta("FirmwareType", "firmwareType", "fw-type-[inv_tag]", VersionMeta.Version101a, "InputOutput", 0x3f, [], [""], [u'capabilityCatalogue'], [u'firmwareDependency'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep": MoPropertyMeta("ep", "ep", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "catalog", "cmc", "core", "debug-plug-in", "diag", "fex", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "identifier-mgr", "iocard", "local-disk", "mgmt-ext", "operation-mgr", "policy-mgr", "provider", "psu", "resource-aggr", "sas-expander", "service-reg", "stats-mgr", "storage-broker", "storage-controller", "switch", "switch-kernel", "switch-software", "system", "unspecified"], []), 
        "inv_tag": MoPropertyMeta("inv_tag", "invTag", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "max_ver": MoPropertyMeta("max_ver", "maxVer", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "min_ver": MoPropertyMeta("min_ver", "minVer", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_order": MoPropertyMeta("update_order", "updateOrder", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ep": "ep", 
        "invTag": "inv_tag", 
        "maxVer": "max_ver", 
        "minVer": "min_ver", 
        "rn": "rn", 
        "status": "status", 
        "updateOrder": "update_order", 
    }

    def __init__(self, parent_mo_or_dn, inv_tag, **kwargs):
        self._dirty_mask = 0
        self.inv_tag = inv_tag
        self.child_action = None
        self.ep = None
        self.max_ver = None
        self.min_ver = None
        self.status = None
        self.update_order = None

        ManagedObject.__init__(self, "FirmwareType", parent_mo_or_dn, **kwargs)

