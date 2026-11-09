# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/email/mime/audio.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/mime/audio.py
__all__ = [
 'MIMEAudio']
import sndhdr
from cStringIO import StringIO
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart
_sndhdr_MIMEmap = {'au': 'basic', 'wav': 'x-wav', 
   'aiff': 'x-aiff', 
   'aifc': 'x-aiff'}

def _whatsnd(data):
    hdr = data[:512]
    fakefile = StringIO(hdr)
    for testfn in sndhdr.tests:
        res = testfn(hdr, fakefile)
        if res is not None:
            return _sndhdr_MIMEmap.get(res[0])

    return


class MIMEAudio(MIMENonMultipart):

    def __init__(self, _audiodata, _subtype=None, _encoder=encoders.encode_base64, **_params):
        if _subtype is None:
            _subtype = _whatsnd(_audiodata)
        if _subtype is None:
            raise TypeError('Could not find audio MIME subtype')
        MIMENonMultipart.__init__(self, 'audio', _subtype, **_params)
        self.set_payload(_audiodata)
        _encoder(self)
        return
