from msf import node_register


@node_register()
def load_text(**kwds):
    cxt = kwds.get("_context")
    if cxt.get("health", True) is False:
        return
    param = kwds.get("_param")
    text = param.get("text", "")
    file_path = param.get("file_path", "")
    if text:
        cxt["text"] = text
        return
    elif file_path:
        with open(file_path, "r") as f:
            text = f.read()
        cxt["text"] = text
        return
    else:
        cxt["health"] = False
        return