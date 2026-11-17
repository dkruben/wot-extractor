# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/game_control/award_controller_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from gui.game_control.AwardController import ServiceChannelHandler as ServiceChannelHandler
from resource_well.gui.shared.event_dispatcher import showResourceWellAwardWindow as showResourceWellAwardWindow
_logger: Any

class ResourceWellRewardHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
