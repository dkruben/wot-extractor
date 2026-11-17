# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarFairplayMessageComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from BigWorld import DynamicScriptComponent as DynamicScriptComponent
import SoundGroups as SoundGroups
from gui.shared.utils import showAFKWarningInWindowsBar as showAFKWarningInWindowsBar
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_messages import ClientActionTemplateMessage as ClientActionTemplateMessage, ACTION_MESSAGE_TYPE as ACTION_MESSAGE_TYPE
_logger: Any
AFK_WARNING_MESSAGE_SOUND = 'afk_warning_message'

class AvatarFairplayMessageComponent(DynamicScriptComponent):
    def showWarningMessage(self, templateKey):
        ...
