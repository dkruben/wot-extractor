# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/base_crew_dialog_template_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.lobby.crew.crew_sounds import CREW_SOUND_OVERLAY_SPACE as CREW_SOUND_OVERLAY_SPACE

class BaseCrewDialogTemplateView(DialogTemplateView):
    __slots__: tuple
    _COMMON_SOUND_SPACE = CREW_SOUND_OVERLAY_SPACE
    _isClosed: Any
    def __init__(self, layoutID=None, uniqueID=None, *args, **kwargs):
        ...
    def _closeClickHandler(self, args=None):
        ...
