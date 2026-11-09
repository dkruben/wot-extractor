# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/missions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from gui.marathon.marathon_event_controller import getMarathons as getMarathons
from gui.server_events import events_dispatcher as server_events
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from skeletons.gui.game_control import ILiveOpsWebEventsController as ILiveOpsWebEventsController, IMarathonEventsController as IMarathonEventsController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, w2c as w2c

class _MissionsSchema(W2CSchema):
    tab: Any
    missionID: Any
    groupID: Any
    marathonPrefix: Any
    anchor: Any
    showDetails: Any
    subTab: Any

class _PersonalMissionsSchema(W2CSchema):
    branch: Any
    operation_id: Any

class _MarathonMissionsSchema(W2CSchema):
    prefix: Any

class _MissionsCategoriesSchema(W2CSchema):
    group_id: Any

class MissionsWebApiMixin(object):
    # decorador original: @w2c(...)
    def openMissionsTab(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openMissionsEvents(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openVehicleMissions(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openMissionCategories(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openMissionsElenEvents(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openMissionMarathon(self, cmd):
        ...

class PersonalMissionsWebApiMixin(object):
    # decorador original: @w2c(...)
    def openPersonalMissions(self, cmd):
        ...
