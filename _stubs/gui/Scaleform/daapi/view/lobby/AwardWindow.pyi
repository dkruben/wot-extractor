# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/AwardWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.meta.MissionAwardWindowMeta import MissionAwardWindowMeta as MissionAwardWindowMeta
from gui.Scaleform.daapi.view.meta.AwardWindowMeta import AwardWindowMeta as AwardWindowMeta
from gui.server_events.pm_constants import PERSONAL_MISSIONS_SILENT_SOUND_SPACE as PERSONAL_MISSIONS_SILENT_SOUND_SPACE

class AwardWindow(AwardWindowMeta):
    def onOKClick(self):
        ...
    def onCloseClick(self):
        ...
    def onTakeNextClick(self):
        ...
    def _getTypeSpecificFields(self):
        ...

class MissionAwardWindow(MissionAwardWindowMeta):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SILENT_SOUND_SPACE
    def onCurrentQuestClick(self):
        ...
    def onNextQuestClick(self):
        ...
    def _getTypeSpecificFields(self):
        ...
