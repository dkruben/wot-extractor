# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/comp7_light_modifiers_domain_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/comp7_light_modifiers_domain_tooltip_view.py
from __future__ import absolute_import
from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider
from battle_modifiers_ext.constants_ext import GameplayImpact
from battle_modifiers.gui.impl.lobby.tooltips.modifiers_domain_tooltip_view import ModifiersDomainTooltipView
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController
COMP7_LIGHT_SEASON_MODIFIERS_DOMAIN = 'comp7LightSeasonModifiers'

class Comp7LightModifiersDomainTooltipView(ModifiersDomainTooltipView):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    def getModifiersDataProvider(self):
        return Comp7LightModifiersDataProvider(self.__comp7LightController.battleModifiers)


class Comp7LightModifiersDataProvider(ModifiersDataProvider):

    @classmethod
    def isHiddenModifier(cls, mod):
        return mod.gameplayImpact == GameplayImpact.HIDDEN

    def _readClientDomain(self, modifier):
        return COMP7_LIGHT_SEASON_MODIFIERS_DOMAIN
