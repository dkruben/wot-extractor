# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/perk_context_impl_base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/perk_context_impl_base.py
from __future__ import absolute_import
from visual_script.misc import ASPECT

class PerkContextImplBase(object):

    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID):
        self._perksController = perksControllerWeakRef
        self._perkLevel = perkLevel
        self.perkID = perkID
        self.scopeID = scopeID
        self.vehicleID = perksControllerWeakRef.vehicleID

    @property
    def vehicle(self):
        raise NotImplementedError

    @property
    def perkLevel(self):
        raise NotImplementedError

    @perkLevel.setter
    def perkLevel(self, value):
        raise NotImplementedError

    def addFactorModifier(self, factor, value):
        raise NotImplementedError

    def removeFactorModifiers(self, factor, numMods):
        raise NotImplementedError

    def dropAllPerkModifiers(self):
        raise NotImplementedError

    def notifyOnClient(self, *_):
        raise NotImplementedError

    def notifyOnClientRibbon(self, *_):
        raise NotImplementedError


class CrewContextImplBase(PerkContextImplBase):
    ASPECT = ASPECT.ALL

    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID, tmanIdxs):
        super(CrewContextImplBase).__init__(perksControllerWeakRef, perkID, perkLevel, scopeID)
        self._levelOverride = False
        self._tmanIdxs = tmanIdxs
