# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/email/mime/image.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/mime/image.py
__all__ = [
 'MIMEImage']
import imghdr
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart

class MIMEImage(MIMENonMultipart):

    def __init__(self, _imagedata, _subtype=None, _encoder=encoders.encode_base64, **_params):
        if _subtype is None:
            _subtype = imghdr.what(None, _imagedata)
        if _subtype is None:
            raise TypeError('Could not guess image MIME subtype')
        MIMENonMultipart.__init__(self, 'image', _subtype, **_params)
        self.set_payload(_imagedata)
        _encoder(self)
        return
