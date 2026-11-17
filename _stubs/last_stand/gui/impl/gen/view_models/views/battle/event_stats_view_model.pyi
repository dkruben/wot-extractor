# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/battle/event_stats_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from last_stand.gui.impl.gen.view_models.views.battle.event_stats_team_member_model import EventStatsTeamMemberModel as EventStatsTeamMemberModel
from last_stand.gui.impl.gen.view_models.views.common.stat_column_settings_model import StatColumnSettingsModel as StatColumnSettingsModel

class EventStatsViewModel(ViewModel):
    __slots__: tuple
    onPlayerClick: Any
    onSendFriendRequest: Any
    onSendPlatoonInvitation: Any
    onRemoveFromBlacklist: Any
    def __init__(self, properties=4, commands=4):
        ...
    @property
    def columnSettings(self):
        ...
    @staticmethod
    def getColumnSettingsType():
        ...
    def getTeam(self):
        ...
    def setTeam(self, value):
        ...
    @staticmethod
    def getTeamType():
        ...
    def getContextMenuPlayerId(self):
        ...
    def setContextMenuPlayerId(self, value):
        ...
    def getClientArenaIdx(self):
        ...
    def setClientArenaIdx(self, value):
        ...
    def _initialize(self):
        ...
