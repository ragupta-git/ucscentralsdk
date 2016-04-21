"""This module contains the meta information of ConfigGetAckables ExternalMethod."""

from ..ucscentralcoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetAckables", "configGetAckables", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "out_catalog": MethodPropertyMeta("OutCatalog", "outCatalog", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "outCatalog": "out_catalog",
}

