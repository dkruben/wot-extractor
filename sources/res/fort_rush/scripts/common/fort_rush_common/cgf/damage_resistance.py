# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/common/fort_rush_common/cgf/damage_resistance.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/common/fort_rush_common/cgf/damage_resistance.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty
from constants import ATTACK_REASON
UNRESISTED_ATTACK_REASON_IDS = frozenset((
 ATTACK_REASON.getIndex(ATTACK_REASON.WORLD_COLLISION),
 ATTACK_REASON.getIndex(ATTACK_REASON.DROWNING)))

class FortRushDamageResistanceComponentDescr(object):
    domain = CGF.Domain.All
    resistance = ComponentProperty(type=CGF.PropertyType.Float, editorName='resistance', value=0.0)
