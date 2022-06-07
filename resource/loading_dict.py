# -*- encoding: utf-8 -*-
'''
@create_time: 2022/06/07 16:17:30
@author: lichunyu
'''

from conf.config import DICT_FILE_PATH
from core.base import DFA


def init_dfa():
    dfa = DFA()
    dfa.parse_text_file(DICT_FILE_PATH)
    return dfa
