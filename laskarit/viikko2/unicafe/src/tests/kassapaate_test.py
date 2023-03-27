import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()


    def test_alkusaldo_oikein(self):
        # alustetaan maksukortti, jossa on 1000 euroa (100000 senttiä)
        kassa = Kassapaate()

        #	Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea 
            #  (rahaa 1000 euroa, lounaita myyty 0)
            #	Huomaa, että luokka tallentaa rahamäärän sentteinä

        self.assertEqual(str(kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kassa.edulliset), "0")
        self.assertEqual(str(kassa.maukkaat), "0")


    def test_syo_edullisesti_kateisella(self):
        #   Käteisosto toimii edullisten  lounaiden osalta
        
        #   1. maksu riittävä: 
        #       kassassa oleva rahamäärä kasvaa lounaan hinnalla ja 
        #       vaihtorahan suuruus on oikea
        #       myytyjen lounaiden määrä kasvaa
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(str(kassa.kassassa_rahaa), "100240")
        self.assertEqual(str(kassa.edulliset), "1")
        self.assertEqual(str(kassa.maukkaat), "0")
        self.assertEqual(str(vaihtoraha), "10")

        #   2. Jos maksu on riittävä: 
            # kassassa oleva rahamäärä ei muutu, 
            # kaikki rahat palautetaan vaihtorahana 
            # ja myytyjen lounaiden määrässä ei muutosta
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(str(kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kassa.edulliset), "0")
        self.assertEqual(str(kassa.maukkaat), "0")
        self.assertEqual(str(vaihtoraha), "200")

    def test_syo_maukkaasti_kateisella(self):
        #   Käteisosto toimii maukkaiden lounaiden osalta
        #	1. Jos maksu riittävä: 
        #       kassassa oleva rahamäärä kasvaa lounaan hinnalla 
        #       ja vaihtorahan suuruus on oikea
        #	    myytyjen lounaiden määrä kasvaa
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(str(kassa.kassassa_rahaa), "100400")
        self.assertEqual(str(kassa.edulliset), "0")
        self.assertEqual(str(kassa.maukkaat), "1")
        self.assertEqual(str(vaihtoraha), "10")


        #	2. Jos maksu ei ole riittävä: 
                # kassassa oleva rahamäärä ei muutu, 
                # kaikki rahat palautetaan vaihtorahana 
                # ja myytyjen lounaiden määrässä ei muutosta
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(str(kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kassa.edulliset), "0")
        self.assertEqual(str(kassa.maukkaat), "0")
        self.assertEqual(str(vaihtoraha), "200")

    #	seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein

    def test_syo_edullisesti_kortilla(self):
        #	Korttiosto toimii edullisten lounaiden osalta
        #	1. JoS kortilla on tarpeeksi rahaa, 
        #       veloitetaan summa kortilta ja palautetaan True
        #   	myytyjen lounaiden määrä kasvaa
        kassa = Kassapaate()
        kortti = Maksukortti(250)
        tulos = kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tulos, True)
        self.assertEqual(str(kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kassa.edulliset), "1")
        self.assertEqual(str(kassa.maukkaat), "0")
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.10 euroa")

        #	2. Jos kortilla ei ole tarpeeksi rahaa:
        #       kortin rahamäärä ei muutu, 
        #       myytyjen lounaiden määrä muuttumaton ja palautetaan False
        
        kassa = Kassapaate()
        kortti = Maksukortti(230)
        tulos = kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kassa.edulliset), "0")
        self.assertEqual(str(kassa.maukkaat), "0")
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.30 euroa")
        self.assertEqual(tulos, False)

        #	Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
  
    def test_syo_maukkaasti_kortilla(self):
        #	Korttiosto toimii maukkaiden lounaiden osalta
        #   1. Jos kortilla on tarpeeksi rahaa, 
        #       veloitetaan summa kortilta
        #       palautetaan True
        #	    myytyjen lounaiden määrä kasvaa
        kassa = Kassapaate()
        kortti = Maksukortti(410)
        tulos = kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tulos, True)
        self.assertEqual(str(kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kassa.edulliset), "0")
        self.assertEqual(str(kassa.maukkaat), "1")
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.10 euroa")

        #	2. Jos kortilla ei ole tarpeeksi rahaa, 
        #       kortin rahamäärä ei muutu, 
        #       myytyjen lounaiden määrä muuttumaton 
        #       palautetaan False
        kassa = Kassapaate()
        kortti = Maksukortti(390)
        tulos = kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kassa.edulliset), "0")
        self.assertEqual(str(kassa.maukkaat), "0")
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.90 euroa")
        self.assertEqual(tulos, False)
        #	Kassassa oleva rahamäärä ei muutu kortilla ostettaessa

    def test_lataa_rahaa(self):
        #	Kortille rahaa ladattaessa 
        #       kortin saldo muuttuu 
        #        kassassa oleva rahamäärä kasvaa ladatulla summalla
        kassa = Kassapaate()
        kortti = Maksukortti(100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(str(kassa.kassassa_rahaa), "100100")

        kassa.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(str(kassa.kassassa_rahaa), "100100")