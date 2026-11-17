# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/shared/event_dispatcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from BWUtil import AsyncReturn as AsyncReturn
from advent_calendar.gui.shared.advent_system_factory import collectPurchaseDialogView as collectPurchaseDialogView, collectRewardWindow as collectRewardWindow, collectCalendarWindow as collectCalendarWindow
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from frameworks.wulf import WindowLayer as WindowLayer
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper as FullScreenDialogWindowWrapper
from gui.impl.dialogs import dialogs as dialogs
from helpers import dependency as dependency
from wg_async import wg_async as wg_async, wg_await as wg_await
_logger: Any

def getCalendarWindowType():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showAdventCalendarMainWindow(controller=None):
    ...
def showAdventCalendarIntroWindow(**kwargs):
    ...
def showRewardWindow(**kwargs):
    ...
# decorador original: @wg_async
def showPurchaseDialogWindow(dayId, price, currencyProvider, parent=None):
    ...
