# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/formatters/servers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import icons as icons
from gui.shared.formatters import text_styles as text_styles
from predefined_hosts import HOST_AVAILABILITY as HOST_AVAILABILITY, PING_STATUSES as PING_STATUSES
_UNAVAILABLE_DATA_PLACEHOLDER = '--'

def formatPingStatus(csisStatus, isColorBlind, isSelected, pingStatus, pingValue, useBigSize=False):
    ...
def makePingStatusIcon(pingStatus, colorBlindName=''):
    ...
