# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/cooldown.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import JOIN_FAILURE as JOIN_FAILURE, REQUEST_COOLDOWN as REQUEST_COOLDOWN
from debug_utils import LOG_WARNING as LOG_WARNING
from gui import SystemMessages as SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as I18N_SYSTEM_MESSAGES
from gui.prb_control.formatters import messages as messages
from gui.prb_control.settings import REQUEST_TYPE_NAMES as REQUEST_TYPE_NAMES, REQUEST_TYPE as REQUEST_TYPE
from gui.shared import rq_cooldown as _rqc
from gui.shared.rq_cooldown import RequestCooldownManager as RequestCooldownManager, REQUEST_SCOPE as REQUEST_SCOPE
from helpers import i18n as i18n

class PrbCooldownManager(RequestCooldownManager):
    def __init__(self):
        ...
    def lookupName(self, rqTypeID):
        ...
    def getDefaultCoolDown(self):
        ...

def validatePrbCreationCooldown():
    ...
def setPrbCreationCooldown():
    ...
def getPrbRequestCoolDown(rqTypeID):
    ...
