# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/ingame_help.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui import GUI_CTRL_MODE_FLAG as GUI_CTRL_MODE_FLAG
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.MapsTrainingIngameHelpWindowMeta import MapsTrainingIngameHelpWindowMeta as MapsTrainingIngameHelpWindowMeta
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl import backport as backport
from gui.impl.gen import R as R
_HTML_TEMPLATE_PATH = 'html_templates:mapsTraining/loadingScreen'

class MapsTrainingIngameHelpWindow(MapsTrainingIngameHelpWindowMeta, BattleGUIKeyHandler):
    def onWindowClose(self):
        ...
    def onWindowMinimize(self):
        ...
    def handleEscKey(self, isDown):
        ...
    def _populate(self):
        ...
    @staticmethod
    def __getPageConfig(pageNum):
        ...
    def _dispose(self):
        ...
