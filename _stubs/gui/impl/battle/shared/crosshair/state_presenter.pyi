# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/crosshair/state_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_control.battle_constants import CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from gui.impl.gen.view_models.views.battle.shared.crosshair_state_model import CrosshairStateModel as CrosshairStateModel, CrosshairType as CrosshairType
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.crosshair_proxy import CrosshairDataProxy as CrosshairDataProxy
_CROSSHAIR_TYPE_BY_ID: dict

class CrosshairStatePresenter(ViewComponent):
    __sessionProvider: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __onCrosshairZoomFactorChanged(self, zoomFactor):
        ...
    @staticmethod
    def __getTypeByID(viewID):
        ...
