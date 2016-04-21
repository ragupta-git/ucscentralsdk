"""This module contains the general information for AaaUserPreferences ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class AaaUserPreferencesConsts():
    FORCE_ESTIMATE_IMPACT_FALSE = "false"
    FORCE_ESTIMATE_IMPACT_NO = "no"
    FORCE_ESTIMATE_IMPACT_TRUE = "true"
    FORCE_ESTIMATE_IMPACT_YES = "yes"


class AaaUserPreferences(ManagedObject):
    """This is AaaUserPreferences class."""

    consts = AaaUserPreferencesConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AaaUserPreferences", "aaaUserPreferences", "pref-[name]", VersionMeta.Version131a, "InputOutput", 0x3fff, [], ["aaa", "admin", "read-only"], [u'aaaUserEp'], [], ["Get", "Set"])

    prop_meta = {
        "basic_widget_disabled": MoPropertyMeta("basic_widget_disabled", "basicWidgetDisabled", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dashboard": MoPropertyMeta("dashboard", "dashboard", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "feature_tour_disabled": MoPropertyMeta("feature_tour_disabled", "featureTourDisabled", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "force_estimate_impact": MoPropertyMeta("force_estimate_impact", "forceEstimateImpact", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []), 
        "language": MoPropertyMeta("language", "language", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x100, None, None, r"""[a-zA-Z][a-zA-Z0-9@_.\-\\]{0,67}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "saved_queries": MoPropertyMeta("saved_queries", "savedQueries", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []), 
        "session_timeout": MoPropertyMeta("session_timeout", "sessionTimeout", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], ["5-120"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "welcome_widget_disabled": MoPropertyMeta("welcome_widget_disabled", "welcomeWidgetDisabled", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], []), 
    }

    prop_map = {
        "basicWidgetDisabled": "basic_widget_disabled", 
        "childAction": "child_action", 
        "dashboard": "dashboard", 
        "descr": "descr", 
        "dn": "dn", 
        "featureTourDisabled": "feature_tour_disabled", 
        "forceEstimateImpact": "force_estimate_impact", 
        "language": "language", 
        "name": "name", 
        "rn": "rn", 
        "savedQueries": "saved_queries", 
        "sessionTimeout": "session_timeout", 
        "status": "status", 
        "welcomeWidgetDisabled": "welcome_widget_disabled", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.basic_widget_disabled = None
        self.child_action = None
        self.dashboard = None
        self.descr = None
        self.feature_tour_disabled = None
        self.force_estimate_impact = None
        self.language = None
        self.saved_queries = None
        self.session_timeout = None
        self.status = None
        self.welcome_widget_disabled = None

        ManagedObject.__init__(self, "AaaUserPreferences", parent_mo_or_dn, **kwargs)

