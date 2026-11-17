# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/crew_members_flag.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.widgets.crew_members_flag_model import CrewMembersFlagModel as CrewMembersFlagModel
from halloween.gui.shared.event_dispatcher import showCrewSelectionWindow as showCrewSelectionWindow
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from helpers import dependency as dependency

# base nao representavel no stub: ViewComponent[...]
class CrewMembersFlag:
    _hwTwitchConCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onClick(self):
        ...
    def __update(self):
        ...
