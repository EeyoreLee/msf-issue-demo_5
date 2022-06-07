from msf import Engine

from conf.path_conf import NODE_CONF, PATH_CONF
from nodes import *
from resource.loading_dict import init_dfa


def response_package_v1(result):
    response = {
        'code': 200,
        'msg': 'success',
        'data': None
    }
    if not isinstance(result, tuple):
        response['data'] = result
        if response["code"] == 200:
            response["success"] = True
        else:
            response["success"] = False
        return response

    if len(result) == 1:
        response['data'] = result

    elif len(result) == 2:
        response['data'] = result[0]
        if isinstance(result[1], int):
            response['code'] = result[1]
        elif isinstance(result[1], str):
            response['msg'] = result[1]
        else:
            raise Exception('non std format data')

    elif len(result) == 3:
        response['data'] = result[0]
        if isinstance(result[1], int) and isinstance(result[2], str):
            response['code'] = result[1]
            response['msg'] = result[2]
        elif isinstance(result[1], str) and isinstance(result[2], int):
            response['msg'] = result[1]
            response['code'] = result[2]
        else:
            raise Exception('non std format data')
    else:
        raise Exception('non std format data')

    if response["code"] == 200:
        response["success"] = True
    else:
        response["success"] = False

    return response


config = {
    'NODE_CONF': NODE_CONF,
    'PATH_CONF': PATH_CONF
}
resource = {}
resource['dfa'] = init_dfa()
resource["lock"] = False
engine = Engine(config, resource, name='sensitive_word_detection')
engine.response_package = response_package_v1
app = engine.app
