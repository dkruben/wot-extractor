# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/award_window_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.AwardWindowsBaseMeta import AwardWindowsBaseMeta as AwardWindowsBaseMeta
from gui.server_events.awards import AwardAbstract as AwardAbstract

class AwardWindowBase(AwardWindowsBaseMeta):
    _award: Any
    def __init__(self, ctx):
        ...
    def onWindowClose(self):
        ...
    def _populate(self):
        ...
    def _getTypeSpecificFields(self):
        ...
    def _dispose(self):
        ...
    def __playSound(self):
        ...
