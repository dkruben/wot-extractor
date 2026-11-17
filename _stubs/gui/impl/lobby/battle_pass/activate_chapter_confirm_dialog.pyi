# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/activate_chapter_confirm_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.battle_pass.sounds import ACTIVATE_CHAPTER_SOUND_SPACE as ACTIVATE_CHAPTER_SOUND_SPACE
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.chapter_confirm_view_model import ChapterConfirmViewModel as ChapterConfirmViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache
_CONFIRM_RES = R.strings.battle_pass.chapterChoice.confirmation
_CHAPTER_RES = R.strings.battle_pass.chapter

class ChapterConfirm(FullScreenDialogBaseView):
    __slots__: tuple
    __itemsCache: Any
    __battlePass: Any
    _COMMON_SOUND_SPACE = ACTIVATE_CHAPTER_SOUND_SPACE
    __chapterID: Any
    def __init__(self, chapterID=None, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onAccept(self):
        ...
    def _onCancel(self):
        ...
    def __onSeasonStateChanged(self):
        ...
