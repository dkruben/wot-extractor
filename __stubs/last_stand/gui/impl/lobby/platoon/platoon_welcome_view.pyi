# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/platoon/platoon_welcome_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.platoon.view.platoon_welcome_view import WelcomeView as WelcomeView
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from last_stand.gui.impl.gen.view_models.views.lobby.ext_platoon_dropdown_model import ExtPlatoonDropdownModel as ExtPlatoonDropdownModel
from last_stand.gui.ls_gui_constants import QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from last_stand.gui.impl.lobby.platoon.platoon_search_view import LSSearchView as LSSearchView

class LSWelcomeView(WelcomeView):
    __platoonCtrl: Any
    _layoutID: Any
    @property
    def _viewModelClass(self):
        ...
    def _setBattleTypeRelatedProps(self):
        ...
    def _onFind(self):
        ...
