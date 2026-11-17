# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/messenger/formatters/invites.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.formatters.invites import PrbInviteHtmlTextFormatter as PrbInviteHtmlTextFormatter
from last_stand.skeletons.ls_controller import ILSController as ILSController
from helpers import dependency as dependency

class LSPrbInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter):
    lsCtrl: Any
    def canAcceptInvite(self, invite):
        ...
