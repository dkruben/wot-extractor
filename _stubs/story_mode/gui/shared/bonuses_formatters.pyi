# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/shared/bonuses_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import CurtailingAwardsComposer as CurtailingAwardsComposer
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, PreformattedBonus as PreformattedBonus
from story_mode.gui.story_mode_gui_constants import BONUS_ORDER as BONUS_ORDER
from gui.server_events.awards_formatters import _PreformattedBonus as _PreformattedBonus
_IMG_PATH_PREFIX = 'img://gui'

class StoryModeBonusesAwardsComposer(CurtailingAwardsComposer):
    def _packBonus(self, bonus, size=...):
        ...
    def _packBonuses(self, preformattedBonuses, size):
        ...
    def _packMergedBonuses(self, mergedBonuses, size=...):
        ...
    @staticmethod
    def _bonusesSortFunction(bonus):
        ...

def getImgPath(path):
    ...
