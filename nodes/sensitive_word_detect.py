import json

from msf import node_register

from core.base import DFA


@node_register()
def detect(**kwds):
    cxt = kwds.get("_context")
    if cxt.get("health", True) is False:
        return
    text = cxt.get("text")
    resource = kwds.get("_resource")
    dfa = resource.get("dfa")
    res = dfa.detect(text)
    cxt["output"] = res
    return