# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_exchange_rewards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from functools import partial as partial
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_exchange_rewards_model import BattleMattersExchangeRewardsModel as BattleMattersExchangeRewardsModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons

class BattleMattersExchangeRewards(FullScreenDialogBaseView):
    __slots__: tuple
    def __init__(self, vehicleName, vehicleUserName):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, vehicleName, vehicleUserName):
        ...
    def _getEvents(self):
        ...
