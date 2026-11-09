# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/dialogs/abilities_incomplete_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from PlayerEvents import g_playerEvents as g_playerEvents
from constants import LoadoutParams as LoadoutParams
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from last_stand.gui.impl.gen.view_models.views.lobby.dialogs.abilities_inclomplete_dialog_model import AbilitiesInclompleteDialogModel as AbilitiesInclompleteDialogModel
from last_stand.gui.impl.lobby.states import LastStandConsumableLoadoutState as LastStandConsumableLoadoutState
from last_stand.gui.impl.lobby.tank_setup import LSTankSetupConstants as LSTankSetupConstants
from last_stand.gui.impl.lobby.widgets.ls_loadout import getCurrentPreset as getCurrentPreset

class AbilitiesIncompleteDialog(FullScreenDialogBaseView):
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onSubmitClick(self):
        ...
    def _onCancelClick(self):
        ...
    def _onCloseClick(self):
        ...

def getConsumablesLoadoutParams():
    ...
