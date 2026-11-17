# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSTeamInfoVoiceChatComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
import VOIP as VOIP
import typing as typing
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN
from gui.battle_control import avatar_getter as avatar_getter
from last_stand.gui.battle_control.arena_info.arena_vos import LSKeys as LSKeys
from VOIP.VOIPManager import VOIPManager as VOIPManager

class LSTeamInfoVoiceChatComponent(DynamicScriptComponent):
    __callbackDelayer: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def set_teamVivoxChannel(self, prev):
        ...
    def __onJoinedVoipChannel(self, *_, **__):
        ...
    def __onLeftVoipChannel(self, *_, **__):
        ...
    def __invalidateTeamVivoxChannel(self):
        ...
    def __updateVoipConnection(self):
        ...
    def __updateVivoxPresence(self):
        ...
