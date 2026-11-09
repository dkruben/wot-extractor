# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/prb_control/__init__.py
from __future__ import absolute_import

def registerComp7LightOthersPrbParams():
    from comp7_light.gui.prb_control.storages.comp7_light_storage import Comp7LightStorage
    from constants import QUEUE_TYPE
    from gui.prb_control.storages import makeQueueName
    from gui.shared.system_factory import registerPrbStorage
    from gui.impl.lobby.mode_selector.items import _arenaBonusTypeByModeName
    from gui.prb_control.prb_getters import _PRB_TO_QUEUE
    from comp7_light.gui.comp7_light_constants import PREBATTLE_ACTION_NAME
    from constants import ARENA_BONUS_TYPE
    from gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants
    from gui.shared.system_factory import registerModeSelectorTooltips
    from comp7_light_constants import PREBATTLE_TYPE
    registerModeSelectorTooltips([
     ModeSelectorTooltipsConstants.COMP7_LIGHT_CALENDAR_DAY_EXTENDED_INFO], {})
    registerPrbStorage(makeQueueName(QUEUE_TYPE.COMP7_LIGHT), Comp7LightStorage())
    _PRB_TO_QUEUE.update({(PREBATTLE_TYPE.COMP7_LIGHT): (QUEUE_TYPE.COMP7_LIGHT)})
    _arenaBonusTypeByModeName.update({(PREBATTLE_ACTION_NAME.COMP7_LIGHT): (ARENA_BONUS_TYPE.COMP7_LIGHT)})
