# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/common/fort_rush_common/cgf/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/common/fort_rush_common/cgf/__init__.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
import CGF
if TYPE_CHECKING:
    from typing import List, Optional, TypeVar
    from CGF import ComponentAccessor
    T = TypeVar('T')

def getTopMostGO(go):
    if not go.valid:
        return None
    else:
        hierarchyManager = CGF.findHierarchySingleton(go.spaceID)
        if not hierarchyManager:
            return None
        return hierarchyManager.getTopMostParent(go)


def findFirstComponentInHierarchy(root, componentType):
    components = CGF.findInHierarchyWithComponent(root, componentType, True)
    if components:
        return components[0]
    else:
        return
