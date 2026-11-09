# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/items_parameters/params_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/items_parameters/params_constants.py
from __future__ import absolute_import
from gui.shared.gui_items import KPI
from items import ITEM_TYPES
ONE_HUNDRED_PERCENTS = 100
AUTOCANNON_SHOT_DISTANCE = 400
MAX_VISION_RADIUS = 500
MIN_VISION_RADIUS = 150
PIERCING_DISTANCES = (50, 500)
MIN_RELATIVE_VALUE = 1
EXTRAS_CAMOUFLAGE = 'camouflageExtras'
MAX_DAMAGED_MODULES_DETECTION_PERK_VAL = -4
MAX_ART_NOTIFICATION_DELAY_PERK_VAL = -2
METERS_PER_SECOND_TO_KILOMETERS_PER_HOUR = 3.6
EPSILON = 0.0001
MODULES = {(ITEM_TYPES.vehicleRadio): (lambda vehicleDescr: vehicleDescr.radio), 
   (ITEM_TYPES.vehicleEngine): (lambda vehicleDescr: vehicleDescr.engine), 
   (ITEM_TYPES.vehicleChassis): (lambda vehicleDescr: vehicleDescr.chassis), 
   (ITEM_TYPES.vehicleTurret): (lambda vehicleDescr: vehicleDescr.turret), 
   (ITEM_TYPES.vehicleGun): (lambda vehicleDescr: vehicleDescr.gun)}
HIDDEN_PARAM_DEFAULTS = {(KPI.Name.ART_NOTIFICATION_DELAY_FACTOR): 2.1, 
   (KPI.Name.DAMAGED_MODULES_DETECTION_TIME): 4.5}
