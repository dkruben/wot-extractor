import struct
import unittest
import xml.etree.ElementTree as ET

from wot_extractor.extract.validate import validate_xml
from wot_extractor.formats.bwxml import PackedXmlError, decode_packed_xml, format_float32, is_packed

from .helpers import SAMPLE_PACKED, N, S, I, F, pack_xml


def _parse(text: str) -> ET.Element:
    return ET.fromstring(text.replace("xmlns:xmlref", "xmlns__xmlref"))


class DecodeTests(unittest.TestCase):
    def test_all_types(self):
        r = decode_packed_xml(SAMPLE_PACKED)
        self.assertEqual(r.status, "success")
        self.assertEqual(r.version, 0)
        text = r.to_text()
        root = _parse(text)
        self.assertEqual(root.tag, "root")
        self.assertEqual(root.find("xmlns__xmlref").text, " http://bwt/xmlref ")
        v = root.find("vehicle")
        self.assertEqual((v.find("id").text, v.find("price").text, v.find("tags").text), ("7", "373000", "mediumTank secret"))
        self.assertEqual(root.find("speed").text, "20")
        self.assertEqual(root.find("color").text, "1 0.725 0.45")
        rows = [root.find(f"transform/row{i}").text for i in range(4)]
        self.assertEqual(rows, ["1 0 0", "0 1 0", "0 0 1", "5 6 7"])
        self.assertEqual((root.find("enabled").text, root.find("hidden").text), ("true", "false"))
        self.assertEqual(root.find("blob").text, "AAEC")
        self.assertEqual(root.find("big").text, str(-2**40))
        self.assertEqual(root.find("zero").text, "0")
        self.assertEqual(r.trailing_bytes, 0)
        self.assertEqual(validate_xml(text.encode()), "valid_bigworld")  # prefixo xmlns: mantido

    def test_nested_with_own_text_and_renamed_tag(self):
        data = pack_xml(N("root", S(""), [N("a", S("texto"), [N("b", I(1, 2))]), N("1bad", S("x"))]))
        r = decode_packed_xml(data)
        root = ET.fromstring(r.to_text())
        self.assertEqual(root.find("a").text.strip(), "texto")
        self.assertEqual(root.find("a/b").text, "1")
        self.assertEqual(root.find("_1bad").text, "x")
        self.assertEqual(r.renamed_tags, 1)
        self.assertTrue(any("1bad" in w for w in r.warnings))

    def test_trailing_bytes_is_partial(self):
        r = decode_packed_xml(SAMPLE_PACKED + b"\x00\x00")
        self.assertEqual((r.status, r.trailing_bytes), ("partial", 2))

    def test_invalid_inputs(self):
        bad = [
            b"<root/>",                                   # nao e binario
            SAMPLE_PACKED[:-3],                           # truncado
            SAMPLE_PACKED[:5] + b"semterminador",         # dicionario sem fim
        ]
        for data in bad:
            with self.subTest(data=data[:12]):
                with self.assertRaises(PackedXmlError):
                    decode_packed_xml(data)

    def test_corrupt_structures(self):
        head = b"\x45\x4e\xa1\x62\x00a\x00\x00"
        cases = {
            "tipo desconhecido": head + struct.pack("<HI", 0, (7 << 28) | 0),
            "fora do dicionario": head + struct.pack("<HI", 1, (1 << 28) | 0) + struct.pack("<HI", 5, (1 << 28) | 0),
            "inteiro": head + struct.pack("<HI", 0, (2 << 28) | 3) + b"abc",
            "booleano": head + struct.pack("<HI", 0, (4 << 28) | 2) + b"\x01\x01",
            "floats": head + struct.pack("<HI", 0, (3 << 28) | 5) + b"12345",
            # elemento aninhado declarado com 20 B, mas ocupa 6
            "ocupa": head + struct.pack("<HI", 1, (1 << 28) | 0) + struct.pack("<HI", 0, (0 << 28) | 20)
                     + struct.pack("<HI", 0, (1 << 28) | 0) + b"\x00" * 14,
        }
        for label, data in cases.items():
            with self.subTest(label=label):
                with self.assertRaises(PackedXmlError) as cm:
                    decode_packed_xml(data)
                self.assertIn(label.split()[0], str(cm.exception))

    def test_invalid_xml_chars_escaped(self):
        r = decode_packed_xml(pack_xml(N("root", S(""), [N("a", S("x\x01y"))])))
        self.assertEqual(r.escaped_strings, 1)
        self.assertEqual(ET.fromstring(r.to_text()).find("a").text, "x\\x01y")

    def test_is_packed(self):
        self.assertTrue(is_packed(SAMPLE_PACKED))
        self.assertFalse(is_packed(b"<root/>"))


class FloatFormatTests(unittest.TestCase):
    def test_round_trip_and_positional(self):
        for v, expected in ((20.0, "20"), (0.725, "0.725"), (1e-7, "0.0000001"), (-3.5, "-3.5"), (0.0, "0")):
            raw = struct.pack("<f", v)
            s = format_float32(raw)
            self.assertEqual(s, expected)
            self.assertEqual(struct.pack("<f", float(s)), raw)
        self.assertEqual(format_float32(struct.pack("<f", -0.0)), "-0")
        self.assertEqual(format_float32(struct.pack("<f", float("inf"))), "inf")
        s = format_float32(struct.pack("<f", 1 / 3))
        self.assertEqual(struct.pack("<f", float(s)), struct.pack("<f", 1 / 3))


if __name__ == "__main__":
    unittest.main()
