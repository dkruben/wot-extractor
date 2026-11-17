# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/loadout_panel_presenter/loadout_panel_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.pub.view_impl import TViewModel as TViewModel
from gui.impl.gen import R as R
from battle_royale.gui.impl.lobby.views.presenters.loadout_panel_presenter.battle_royale_loadout_presenter import BattleRoyaleLoadoutPresenter as BattleRoyaleLoadoutPresenter
from battle_royale.gui.impl.lobby.views.presenters.loadout_panel_presenter.commander_presenter import CommanderPresenter as CommanderPresenter
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import isIncorrectVehicle as isIncorrectVehicle

# base nao representavel no stub: ViewComponent[...]
class LoadoutContainerPresenter:
    _BATTLE_ROYALE_LOADOUT = R.aliases.battle_royale.loadoutPanelContainer
    _CHILDREN: dict
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onCurrentVehicleChanged(self):
        ...
    def _addChild(self, posId, vehicle):
        ...
