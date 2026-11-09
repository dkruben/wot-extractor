# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/game_control/award_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.comp7_light_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from comp7_light.gui.shared.event_dispatcher import showBattleQuestAwardsWindow as showBattleQuestAwardsWindow
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from gui.game_control.AwardController import PunishWindowHandler as PunishWindowHandler, ServiceChannelHandler as ServiceChannelHandler
from helpers import dependency as dependency
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages

class Comp7LightProgressionStageHandler(ServiceChannelHandler):
    __systemMessages: Any
    _CLIENT_MSG_TYPE = SCH_CLIENT_MSG_TYPE.COMP7_LIGHT_PROGRESSION_NOTIFICATIONS
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    def _showMessages(self, ctx):
        ...
    @staticmethod
    def _getMessage(ctx):
        ...

class Comp7LightPunishWindowHandler(PunishWindowHandler):
    @property
    def channelType(self):
        ...
