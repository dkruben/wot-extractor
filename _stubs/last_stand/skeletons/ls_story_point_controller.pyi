# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/skeletons/ls_story_point_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from skeletons.gui.game_control import IGameController as IGameController

class ILSStoryPointController(IGameController):
    FIRST_STORY_POINT_INDEX = None
    onStoryPointStatusUpdated = None
    @property
    def selectedStoryPointID(self):
        ...
    @selectedStoryPointID.setter
    def selectedStoryPointID(self, artefactID):
        ...
    @property
    def storyPoints(self):
        ...
    def getIndex(self, storyPointID):
        ...
    def getStoryPointIDByIndex(self, index):
        ...
    def getStoryPointsCount(self):
        ...
    def isStoryPointReceived(self, storyPointID):
        ...
