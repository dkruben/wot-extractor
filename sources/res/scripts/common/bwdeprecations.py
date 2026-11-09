# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/bwdeprecations.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/bwdeprecations.py
from __future__ import absolute_import
import functools, warnings, BigWorld

def deprecatedAlias(method, oldname):

    def warnAndCallWrapper(*args, **kwargs):
        warnings.warn('%s.%s is deprecated, use %s.%s instead' % (
         method.__module__, oldname, method.__module__, method.__name__), DeprecationWarning, 2)
        return method(*args, **kwargs)

    return functools.wraps(method)(warnAndCallWrapper)


def addDeprecatedAliasOf(module, newname, oldname):
    if not hasattr(module, newname):
        return
    if hasattr(module, oldname):
        return
    method = getattr(module, newname)
    setattr(module, oldname, deprecatedAlias(method, oldname))


if BigWorld.component == 'client':
    addDeprecatedAliasOf(BigWorld, 'serverTime', 'stime')
addDeprecatedAliasOf(BigWorld, 'ThirdPersonTargetingMatrix', 'ThirdPersonTargettingMatrix')
addDeprecatedAliasOf(BigWorld, 'MouseTargetingMatrix', 'MouseTargettingMatrix')
if BigWorld.component == 'client':
    if not hasattr(BigWorld, 'cachedEntities'):
        BigWorld.cachedEntities = {}
    if not hasattr(BigWorld, 'allEntities'):
        BigWorld.allEntities = BigWorld.entities
if BigWorld.component == 'cell':
    import OldSpaceData
