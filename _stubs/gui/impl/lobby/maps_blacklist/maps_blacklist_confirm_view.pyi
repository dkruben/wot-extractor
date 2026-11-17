# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_blacklist/maps_blacklist_confirm_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.content.select_option_content import SelectOptionContent as SelectOptionContent, MapOption as MapOption
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.shared.formatters import time_formatters as time_formatters
from typing import List as List, Optional as Optional
_logger: Any

class MapsBlacklistDialog(DialogTemplateView):
    newMap: Any
    mapsToReplace: Any
    cooldown: Any
    _selector: Any
    _confirmButton: Any
    def __init__(self, newMap, mapsToReplace, cooldown):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _setTitle(self, mapAmount, mapName):
        ...
    def _setContentMessage(self, mapAmount, mapName):
        ...
    def _fillOptions(self):
        ...
    def _onSelectionChanged(self):
        ...
    def _getAdditionalData(self):
        ...
