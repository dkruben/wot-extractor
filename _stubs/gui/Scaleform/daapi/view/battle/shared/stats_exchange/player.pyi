# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/stats_exchange/player.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS as INVITATION_DELIVERY_STATUS
from gui.battle_control.arena_info.settings import PLAYER_STATUS as PLAYER_STATUS
from soft_exception import SoftException as SoftException

class PlayerStatusComponent(broker.StatusComponent):
    def __init__(self):
        ...

class InvitationStatusComponent(broker.StatusComponent):
    def __init__(self):
        ...

class InvitationsExchangeBlock(broker.ExchangeBlock):
    def __init__(self):
        ...
    def addSortIDs(self, arenaDP, *flags):
        ...
    def addTotalStats(self, stats):
        ...

class UserTagsItemData(broker.VehicleComponent):
    __slots__: tuple
    _ctx: Any
    _avatarSessionID: Any
    _igrType: Any
    _tags: Any
    _vehicleID: Any
    def __init__(self, ctx):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def get(self, forced=False):
        ...
    def addVehicleInfo(self, vInfoVO):
        ...
    def addUserTags(self, tags):
        ...

class UsersTagsListExchangeData(broker.ExchangeBlock):
    def __init__(self, ctx):
        ...
    def addSortIDs(self, arenaDP, *flags):
        ...
    def addTotalStats(self, stats):
        ...
