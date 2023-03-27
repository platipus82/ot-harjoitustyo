import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_oikein(self):
        # testaa että krtin saldo alussa oikein
        kortti = Maksukortti(400)
        self.assertEqual(str(kortti), "Kortilla on rahaa 4.00 euroa")

    def test_lataa_saldo(self):
        # Rahan lataaminen kasvattaa saldoa oikein
        kortti = Maksukortti(1000)
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")
        
    def test_ota_rahaa(self):
        # rahan ottaminen toimii:
        kortti = Maksukortti(1000)
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_saldo_vahenee(self):
        # Saldo vähenee oikein, jos rahaa on tarpeeksi
        kortti = Maksukortti(1000)
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_saldo_ei_muutu(self):
        # Saldo ei muutu, jos rahaa ei ole tarpeeksi
        kortti = Maksukortti(1000)
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahat_riittavat(self):
        # Metodi palauttaa True, jos rahat riittivät ja muuten False
        kortti = Maksukortti(1000)
        x = self.maksukortti.ota_rahaa(1200)
        y = self.maksukortti.ota_rahaa(800)
        return((x and y))
