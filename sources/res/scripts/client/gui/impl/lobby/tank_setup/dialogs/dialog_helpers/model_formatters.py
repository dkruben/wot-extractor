# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/dialog_helpers/model_formatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/dialogs/dialog_helpers/model_formatters.py


def initItemInfo(viewModel, device, currency):
    with viewModel.transaction() as model:
        model.detailsDevice.setOverlayType(device.getHighlightType())
        model.detailsDevice.setLevel(device.level)
        model.detailsDevice.setDeviceName(device.name)
        model.detailsPriceBlock.setCurrencyName(currency)
        model.detailsPriceBlock.setCountDevice(device.inventoryCount)
        actualPrices = device.sellPrices.itemPrice.price
        model.detailsPriceBlock.setPriceDevice(actualPrices.toSignDict().get(currency, 0))
