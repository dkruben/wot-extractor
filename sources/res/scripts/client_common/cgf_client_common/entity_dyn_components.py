# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/cgf_client_common/entity_dyn_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/cgf_client_common/entity_dyn_components.py
from __future__ import absolute_import
import BigWorld
from constants import IS_EDITOR

class DynamicScriptComponentStub(object):
    pass


ReplicableDynamicScriptComponent = (IS_EDITOR or BigWorld).DynamicScriptComponent if 1 else DynamicScriptComponentStub
