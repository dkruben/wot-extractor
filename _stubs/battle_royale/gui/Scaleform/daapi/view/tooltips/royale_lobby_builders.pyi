# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/tooltips/royale_lobby_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowLayer as WindowLayer
from battle_royale.gui.Scaleform.daapi.view.lobby.tooltips import BattleProgressionTooltipData as BattleProgressionTooltipData, BattleRoyaleCalendarExtendedTooltip as BattleRoyaleCalendarExtendedTooltip
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.genConsts.BATTLEROYALE_ALIASES import BATTLEROYALE_ALIASES as BATTLEROYALE_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.app_loader import sf_lobby as sf_lobby
from gui.shared.tooltips import contexts as contexts
from battle_royale.gui.shared.tooltips.battle_royale_modules import BattleRoyaleModulesTooltip as BattleRoyaleModulesTooltip
from gui.shared.tooltips.builders import DataBuilder as DataBuilder
from battle_royale.gui.Scaleform.daapi.view.lobby.tooltips.battle_royale_completed_quest_tooltip import BattleRoyaleQuestsTooltip as BattleRoyaleQuestsTooltip
__all__: tuple

class _BattleRoyaleHangarVehInfoContext(contexts.HangarContext):
    _vehicle: Any
    # decorador original: @sf_lobby
    def app(self):
        ...
    def getVehicle(self):
        ...
    def buildItem(self, intCD, slotIdx=0, historicalBattleID=-1, vehicle=None):
        ...

def getTooltipBuilders():
    ...
