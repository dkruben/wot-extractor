# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/boss_indicator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.settings_core import settings_constants as settings_constants
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.scaleform.daapi.view.meta.HWBossIndicatorProgressMeta import HWBossIndicatorProgressMeta as HWBossIndicatorProgressMeta
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class HWBossIndicator(HWBossIndicatorProgressMeta):
    guiSessionProvider: Any
    settingsCore: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __handleChangeDistance(self, ctx):
        ...
    def __onSettingsChange(self, diff):
        ...
    def __updateAlpha(self):
        ...
