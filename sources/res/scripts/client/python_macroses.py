# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/python_macroses.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/python_macroses.py
from __future__ import absolute_import
import ResMgr
from debug_utils import LOG_ERROR
_MACROSES_XML = 'scripts/python_macroses.xml'
g_macroses = {}

def init():
    global g_macroses
    section = ResMgr.openSection(_MACROSES_XML)
    if section is not None:
        for macros in section.values():
            command = macros['id'].asString
            if command in g_macroses:
                LOG_ERROR(('Command "{}" duplicated in python_macroses.xml. Also check in extensions').format(command))
            else:
                g_macroses[command] = macros.asString

    return
