# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/br_vo_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import WWISE as WWISE
import nations as nations
from constants import CURRENT_REALM as CURRENT_REALM, IS_CHINA as IS_CHINA
from gui.battle_control import avatar_getter as avatar_getter
from items import vehicles as vehicles
from helpers import isPlayerAvatar as isPlayerAvatar
_RU_REALMS: tuple
_SWITCH_RU = 'SWITCH_ext_BR_vo_language'
_SWITCH_RU_ON = 'SWITCH_ext_BR_vo_language_RU'
_SWITCH_RU_OFF = 'SWITCH_ext_BR_vo_language_nonRU'
_SWITCH_CN = 'SWITCH_ext_BR_vo_language_CN'
_SWITCH_CHAR = 'SWITCH_ext_BR_vo_char'
_SWITCH_CHAR_FOR_NATIONS: dict

class BRVoiceOverController(object):
    __isActive: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def __onVehicleEnterWorld(self, vehicle):
        ...
    def __updateBattleSwitches(self, vehicle):
        ...
    def __compactDescrToSwitchValue(self, descr):
        ...
    @property
    def __isRuRealm(self):
        ...
    @property
    def __switchRuValue(self):
        ...
