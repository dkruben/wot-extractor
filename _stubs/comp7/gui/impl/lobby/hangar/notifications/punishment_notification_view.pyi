# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/notifications/punishment_notification_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.impl.lobby.hangar.notifications.punishment_notification_view import PunishmentView as PunishmentView, AfkLeaverNotification as AfkLeaverNotification
from gui.shared.utils.functions import getArenaShortName as getArenaShortName
from helpers import i18n as i18n

class Comp7BanView(PunishmentView):
    def __init__(self, arenaTypeID, time, duration, penalty, isQualification, layoutID=None):
        ...

class Comp7BanNotificationWindow(AfkLeaverNotification):
    __slots__: tuple
    arenaTypeID: Any
    time: Any
    duration: Any
    penalty: Any
    isQualification: Any
    def __init__(self, arenaTypeID, time, duration, penalty, isQualification, parent=None):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
