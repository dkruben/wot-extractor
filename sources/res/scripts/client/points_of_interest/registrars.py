# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/points_of_interest/registrars.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/points_of_interest/registrars.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from points_of_interest.managers import PoiStateCreateSystem, PoiStateUpdateSystem, PoiViewStateSystem, PoiSoundSystem
_UPDATE_PERIOD = 0.2

@registerModule
class PointsOfInterestModule(object):
    name = 'POI Module'
    desc = 'Stuff for points of interest'
    group = 'Battle'
    systems = [
     CGF.RegisterSystem(PoiStateCreateSystem, domain=CGF.Domain.Client),
     CGF.RegisterSystem(PoiViewStateSystem, domain=CGF.Domain.Client, updateAfter=(
      CGF.TransformUpdateSystem,), updatePeriod=_UPDATE_PERIOD, perTickUpdate=True),
     CGF.RegisterSystem(PoiSoundSystem, domain=CGF.Domain.Client, updatePeriod=_UPDATE_PERIOD),
     CGF.RegisterSystem(PoiStateUpdateSystem, domain=CGF.Domain.Client, updateAfter=(
      CGF.TransformUpdateSystem, PoiStateCreateSystem, PoiSoundSystem), updatePeriod=_UPDATE_PERIOD)]
    components = []
