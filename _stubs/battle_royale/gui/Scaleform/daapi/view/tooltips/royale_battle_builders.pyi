# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/tooltips/royale_battle_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.app_loader import sf_battle as sf_battle
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from battle_royale.gui.shared.tooltips.battle_royale_modules import BattleRoyaleModulesTooltip as BattleRoyaleModulesTooltip
from gui.shared.tooltips.builders import DataBuilder as DataBuilder
from helpers import dependency as dependency
from items import parseIntCompactDescr as parseIntCompactDescr
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
__all__: tuple

class _BattleRoyaleBattleVehInfoContext(object):
    # decorador original: @sf_battle
    def app(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getVehicle(self):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def __getProgressionCtrl(self, sessionProvider=None):
        ...
    def getComponent(self):
        ...

def getTooltipBuilders():
    ...
