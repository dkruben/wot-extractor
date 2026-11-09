# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/cgf/cgf_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/cgf/cgf_module.py
from __future__ import absolute_import
import CGF
from CapturePointComponent import CapturePointMarkerAnchor
from cgf_script.registration import registerModule, bonusCapsPredicate
from fort_rush.cgf.capture_point import CapturePointMarkerAnchorGizmoSystem, CapturePointSystem
from fort_rush.cgf.damage_resistance import FortRushDamageResistanceSystem
from fort_rush_common.fort_rush_constants import ARENA_BONUS_TYPE_CAPS
from VehicleExpirableComponent import VehicleExpirableComponent

@registerModule
class FortRushClientModule(object):
    name = 'Fort Rush Client Module'
    desc = 'Fort Rush systems that works on client'
    group = 'Fort Rush'
    systems = [
     CGF.RegisterSystem(CapturePointSystem, domain=CGF.Domain.Client, predicate=(lambda spaceID: bonusCapsPredicate(ARENA_BONUS_TYPE_CAPS.FORT_RUSH, spaceID))),
     CGF.RegisterSystem(FortRushDamageResistanceSystem, domain=CGF.Domain.Client, predicate=(lambda spaceID: bonusCapsPredicate(ARENA_BONUS_TYPE_CAPS.FORT_RUSH, spaceID))),
     CGF.RegisterSystem(CapturePointMarkerAnchorGizmoSystem, domain=CGF.Domain.Editor)]
    components = [
     CapturePointMarkerAnchor,
     VehicleExpirableComponent]
