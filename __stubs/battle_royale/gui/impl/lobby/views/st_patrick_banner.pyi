# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/st_patrick_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_royale.gui.impl.lobby.views.event_banner import BattleRoyaleEventBanner as BattleRoyaleEventBanner
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class StPatrickEventBanner(BattleRoyaleEventBanner):
    NAME = 'StPatrickEntryPoint'
    @property
    def borderColor(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    def _onUpdate(self, *_):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isStPatrickEntryPointAvailable(battleRoyaleController=None):
    ...
