# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/dyn_objects.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/dyn_objects.py
from __future__ import absolute_import
import typing
from future.utils import viewitems
from dyn_objects_cache import DynObjectsBase, createTerrainCircleSettings
from story_mode_common.story_mode_constants import RECON_ABILITY, DISTRACTION_ABILITY, SCC_AIRSTRIKE_ABILITY, SCC_AIRSTRIKE_ABILITY_HARD
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
DEFAULT = 'default'
EQUIPMENT_VISUALS = {SCC_AIRSTRIKE_ABILITY: 'SMSccAirstrikeAimingCircleVisual', 
   SCC_AIRSTRIKE_ABILITY_HARD: 'SMSccAirstrikeAimingCircleVisual', 
   RECON_ABILITY: 'ReconAimingCircleVisual', 
   DISTRACTION_ABILITY: 'DistractionAimingCircleVisual', 
   DEFAULT: 'AimingCircleRestrictionVisual'}

class StoryModeDynObjects(DynObjectsBase):

    def __init__(self):
        super(StoryModeDynObjects, self).__init__()
        self._circleSettings = {}

    def init(self, dataSection):
        if not self._initialized:
            for name, visual in viewitems(EQUIPMENT_VISUALS):
                if dataSection.has_key(visual):
                    self._circleSettings[name] = createTerrainCircleSettings(dataSection[visual])

            super(StoryModeDynObjects, self).init(dataSection)

    def destroy(self):
        self._circleSettings.clear()
        super(StoryModeDynObjects, self).destroy()

    def getAimingCircleRestrictionEffect(self, equipment):
        settings = self._circleSettings.get(equipment.name)
        if settings:
            return settings
        return self._circleSettings.get(DEFAULT)
