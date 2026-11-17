# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/rally_dialog_meta.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.daapi.view.dialogs import I18nDialogMeta as I18nDialogMeta, I18nInfoDialogMeta as I18nInfoDialogMeta, I18nConfirmDialogMeta as I18nConfirmDialogMeta, I18nConfirmDialogButtons as I18nConfirmDialogButtons, I18nInfoDialogButtons as I18nInfoDialogButtons, DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES as CYBER_SPORT_ALIASES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.prb_control.formatters.messages import makeEntityI18nKey as makeEntityI18nKey
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE
from gui.shared.events import ShowDialogEvent as ShowDialogEvent
from gui.Scaleform.framework.ScopeTemplates import VIEW_SCOPE as VIEW_SCOPE, WINDOW_SCOPE as WINDOW_SCOPE, SimpleScope as SimpleScope
_P_TYPE = PREBATTLE_TYPE
_Q_TYPE = QUEUE_TYPE
_C_TYPE = CTRL_ENTITY_TYPE
_VIEW_SCOPES: dict
_ENTITY_TO_ANOTHER_PREFIX: dict
_DEFAULT_CONFIRM = 'leave'
_INTRO_TO_ANOTHER_PREFIX: dict

class _RallyInfoDialogMeta(I18nInfoDialogMeta):
    def __init__(self, ctrlType, entityType, prefix):
        ...

class _RallyConfirmDialogMeta(I18nConfirmDialogMeta):
    def __init__(self, ctrlType, entityType, prefix, titleCtx=None, messageCtx=None, focusedID=None):
        ...

class UnitConfirmDialogMeta(I18nConfirmDialogMeta):
    def __init__(self, prbType, prefix, titleCtx=None, messageCtx=None, focusedID=None):
        ...

class StrongholdConfirmDialogMeta(I18nDialogMeta):
    def __init__(self, key, subKey='', titleCtx=None, messageCtx=None, focusedID=None):
        ...

class _RallyScopeDialogMeta(I18nDialogMeta):
    __key: Any
    def __init__(self, ctrlType, entityType, meta):
        ...
    def getEventType(self):
        ...
    def getViewScopeType(self):
        ...

class RallyScopeInfoDialogMeta(_RallyScopeDialogMeta):
    def __init__(self, ctrlType, entityType, prefix):
        ...

class RallyLeaveDisabledDialogMeta(RallyScopeInfoDialogMeta):
    def __init__(self, ctrlType, entityType):
        ...

class RallyScopeConfirmDialogMeta(_RallyScopeDialogMeta):
    def __init__(self, ctrlType, entityType, prefix):
        ...

def _createLeaveRallyMeta(unlockCtx, leftCtrlType, leftEntityType, isSwitching=False):
    ...
def _createLeaveIntroMeta(unlockCtx, leftCtrlType, leftEntityType, isSwitching=False):
    ...
def createPrbIntroLeaveMeta(unlockCtx, leftPrbType, isSwitching=False):
    ...
def createPrbLeaveMeta(unlockCtx, leftPrbType, isSwitching=False):
    ...
def createUnitIntroLeaveMeta(unlockCtx, leftPrbType, isSwitching=False):
    ...
def createUnitLeaveMeta(unlockCtx, leftPrbType, isSwitching=False):
    ...
def createLeavePreQueueMeta(unlockCtx, leftQueueType, isSwitching=False):
    ...
def createLeaveInfoMeta(unlockCtx, prefix):
    ...
