# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/role_skill_slot_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/role_skill_slot_presenter.py
from __future__ import absolute_import
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7_core.gui.impl.lobby.role_skill_slot_presenter import RoleSkillSlotPresenter
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7RoleSkillSlotPresenter(RoleSkillSlotPresenter):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @property
    def _modeController(self):
        return self.__comp7Controller

    @property
    def _roleSkillTooltipId(self):
        return COMP7_TOOLTIPS.COMP7_ROLE_SKILL_LOBBY_TOOLTIP
