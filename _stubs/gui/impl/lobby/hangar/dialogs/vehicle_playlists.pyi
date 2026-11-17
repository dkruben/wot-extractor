# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/dialogs/vehicle_playlists.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from BWUtil import AsyncReturn as AsyncReturn
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.dialogs import showTypeParamConfirmDialog as showTypeParamConfirmDialog
from wg_async import wg_async as wg_async, wg_await as wg_await
EMPTY_DIALOG_PARAMS = '{}'

class VehPlaylistsDialogType(object):
    IMPORT = 'import'
    DELETE = 'delete'
    SAVE_BEFORE_LEAVE = 'save'

# decorador original: @wg_async
def showTypeParamPlaylistDialog(dialogType, dialogParams):
    ...
# decorador original: @wg_async
def showSaveBeforeLeavePlaylistDialog(dialogParams=None):
    ...
