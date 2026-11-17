# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/referral_program_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.page.footer.referral_program_model import ReferralProgramModel as ReferralProgramModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import ReferralProgramEvent as ReferralProgramEvent
from helpers import dependency as dependency
from skeletons.gui.game_control import IReferralProgramController as IReferralProgramController

# base nao representavel no stub: ViewComponent[...]
class ReferralProgramPresenter:
    __referralCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onReferralStateChanged(self):
        ...
    def __onClick(self):
        ...
    def __updateModel(self, *_):
        ...
