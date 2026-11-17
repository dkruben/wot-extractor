# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/lobby_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from typing import Dict as Dict
SETTINGS_WINDOWS_MAP: dict
DEFAULT_SETTINGS_ALIAS = VIEW_ALIAS.SETTINGS_WINDOW

class USER(object):
    INFO = 'userInfo'
    CLAN_INFO = 'clanInfo'
    SEND_CLAN_INVITE = 'sendClanInvite'
    CREATE_PRIVATE_CHANNEL = 'createPrivateChannel'
    ADD_TO_FRIENDS = 'addToFriends'
    REQUEST_FRIENDSHIP = 'requestFriendship'
    REMOVE_FROM_FRIENDS = 'removeFromFriends'
    ADD_TO_IGNORED = 'addToIgnored'
    REMOVE_FROM_IGNORED = 'removeFromIgnored'
    COPY_TO_CLIPBOARD = 'copyToClipBoard'
    SET_MUTED = 'setMuted'
    UNSET_MUTED = 'unsetMuted'
    CREATE_SQUAD = 'createSquad'
    CREATE_EVENT_SQUAD = 'createEventSquad'
    CREATE_BATTLE_ROYALE_SQUAD = 'createBattleRoyaleSquad'
    INVITE = 'invite'
    VEHICLE_INFO = 'vehicleInfoEx'
    END_REFERRAL_COMPANY = 'endReferralCompany'
    CREATE_MAPBOX_SQUAD = 'createMapboxSquad'

def registerSettingsWindow(arenaBonusType, viewAlias):
    ...
def getSettingsWindowAlias():
    ...
