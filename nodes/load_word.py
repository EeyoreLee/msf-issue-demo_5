# -*- encoding: utf-8 -*-
'''
@create_time: 2022/06/07 18:07:59
@author: lichunyu
'''
from msf import node_register

from core.base import DFA


@node_register()
def clean(**kwds):
    _resource = kwds.get("_resource", {})
    dfa: DFA = _resource.get("dfa")
    dfa.clean_all()
    return None