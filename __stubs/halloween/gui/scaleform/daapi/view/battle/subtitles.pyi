# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/subtitles.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from Avatar import PlayerAvatar as PlayerAvatar
from gui import makeHtmlString as makeHtmlString
from halloween.gui.scaleform.daapi.view.meta.HWSubtitlesMeta import HWSubtitlesMeta as HWSubtitlesMeta
from halloween.gui.sounds.sound_constants import VO as VO
from helpers import i18n as i18n, dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class BattleSubtitles(HWSubtitlesMeta):
    sessionProvider: Any
    _currentMessage: Any
    _isPostMortem: Any
    _isSubtitleVisible: Any
    _soundNotifications: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
    def _onSubtitleShow(self, msgKey):
        ...
    def _onSubtitleHide(self):
        ...
    def _show(self):
        ...
    def _hide(self):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def _onRespawnBaseMoving(self):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
