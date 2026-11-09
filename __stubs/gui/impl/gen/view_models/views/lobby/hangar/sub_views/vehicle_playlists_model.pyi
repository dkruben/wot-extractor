# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_playlists_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Map as Map, ViewModel as ViewModel

class VehiclePlaylistsModel(ViewModel):
    __slots__: tuple
    onSelect: Any
    onCreate: Any
    onModify: Any
    onSetDirtyEdit: Any
    onSave: Any
    onDiscard: Any
    onDelete: Any
    openImportConfirm: Any
    openDeleteConfirm: Any
    onGoToAboutVehicle: Any
    def __init__(self, properties=4, commands=10):
        ...
    def getSelectedID(self):
        ...
    def setSelectedID(self, value):
        ...
    def getEnabled(self):
        ...
    def setEnabled(self, value):
        ...
    def getDirtyEdit(self):
        ...
    def setDirtyEdit(self, value):
        ...
    def getStorage(self):
        ...
    def setStorage(self, value):
        ...
    @staticmethod
    def getStorageType():
        ...
    def _initialize(self):
        ...
