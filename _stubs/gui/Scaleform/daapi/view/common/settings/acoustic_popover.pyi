# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/settings/acoustic_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.common.settings import acoustic_presets as acoustic_presets
from gui.Scaleform.daapi.view.meta.AcousticPopoverMeta import AcousticPopoverMeta as AcousticPopoverMeta
from gui.Scaleform.genConsts.ACOUSTICS import ACOUSTICS as ACOUSTICS
from gui.Scaleform.locale.SETTINGS import SETTINGS as SETTINGS
from helpers.i18n import makeString as makeString

class AcousticPopover(AcousticPopoverMeta):
    __acousticType: Any
    __player: Any
    def __init__(self, ctx=None):
        ...
    def setEnabled(self, isEnabled):
        ...
    def setItemsSelected(self, speakerIDs):
        ...
    def setItemsPlay(self, speakerIDs):
        ...
    def setPauseEnabled(self, isEnabled):
        ...
    def setPlayEnabled(self, isEnabled):
        ...
    def onActionStart(self, actionID):
        ...
    def onSpeakerClick(self, speakerID):
        ...
    def _populate(self):
        ...
    def as_disposeS(self):
        ...
