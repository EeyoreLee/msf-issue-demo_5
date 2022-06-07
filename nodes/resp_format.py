from msf import node_register


@node_register()
def response_format(**kwds):
    cxt = kwds.get("_context")
    if cxt.get("health", True) is False:
        return {}, 400, "Parameter error"
    output = cxt.get("output")
    return {"result": output, "prop": {}}