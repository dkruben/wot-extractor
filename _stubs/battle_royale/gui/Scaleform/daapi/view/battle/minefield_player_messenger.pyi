# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/minefield_player_messenger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener as IProgressionListener
from Event import EventsSubscriber as EventsSubscriber
from gui.battle_control.view_components import IViewComponentsCtrlListener as IViewComponentsCtrlListener
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from items import vehicles as vehicles
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID

class MinefieldPlayerMessenger(IProgressionListener, IViewComponentsCtrlListener):
    MINEFIELD_INSTALLED_ID = 'MINEFIELD_INSTALLED'
    MINEFIELD_DESTROYED_ID = 'MINEFIELD_DESTROYED'
    __sessionProvider: Any
    __eventsSubscriber: Any
    __equipmentCtrl: Any
    def __init__(self):
        ...
    def detachedFromCtrl(self, ctrlID):
        ...
    def __onCombatEquipmentUsed(self, shooterID, eqID):
        ...
    def _onPlayerFeedbackReceived(self, events):
        ...
