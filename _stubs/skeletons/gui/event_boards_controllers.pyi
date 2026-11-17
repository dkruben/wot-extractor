# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/event_boards_controllers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from typing import Any as Any, Callable as Callable, Type as Type
from gui.event_boards.event_boards_items import IPlayerProgression as IPlayerProgression

class IEventBoardController(object):
    def isElenQuestsStatusWrong(self, currentEvent):
        ...
    def getPlayerEventsData(self):
        ...
    def hasEvents(self):
        ...
    def getEventsSettingsData(self):
        ...
    def getMyEventsTopData(self):
        ...
    def getHangarFlagData(self):
        ...
    def updateHangarFlag(self):
        ...
    def cleanEventsData(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def joinEvent(self, eventID, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def leaveEvent(self, eventID, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getHangarFlag(self, callback, onLogin=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getEvents(self, callback, onlySettings=True, isTabVisited=False, onLogin=False, prefetchKeyArtBig=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getMyLeaderboardInfo(self, eventID, leaderboardID, callback, showNotification=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getLeaderboard(self, eventID, leaderboardID, pageNumber, callback, leaderBoardClass=None, showNotification=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getPlayerProgression(self, eventID, leaderboardID, progressionClass, callback=None, showNotification=True):
        ...
