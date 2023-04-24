# Ohjelmistotekniikka 2023

# Harjoitustyö
## Kuvaus
Flashcards sovelluksen avulla käyttäjät voivat opetella asioita digitaalisten opettelukorttien avulla (eng. *flashcards*). Kortit on ryhmitelty kokoelmiin. 



## Dokumentaatio
[Vaativuusmaarittely](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Muutosloki](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.MD)

## Asennus ja käyttö
1. Ohjelman lataus. Lataa ohjelman viimeisin versio (_release_) [täältä](https://github.com/platipus82/ot-harjoitustyo/releases/tag/viikko5) haluamaasi kansioon.
2. Riippuvuuksien asennus. Asenna riippuvuudet ohjelmahakemistoon komennolla `poetry install`
3. Käynnistä sovellus komennolla `poetry run invoke start`


## Komentorivitoiminnot
**Suoritus**
Ohjelman voi suorittaa 
- komennolla `poetry run invoke start` 
- komennoilla `python3 flashcards.py` 
- poetryn virtuaaliympäristössä komennoin `poetry run python src/flashcards.py`



**Testaus**

Ohjelman pystyy testaamaan pytestin avulla komennolla `poetry run invoke test` tai `python3 flashcards_test.py`


**Testikattavuus**

Ohjelman testikattavuuden voi kartoittaa komennolla `poetry run invoke coverage`. Html-muotoisen raportin voi tuottaa komennolla `poetry run invoke coverage-report`. Raportti sijoitetaan hakemistoon _htmlcov_.

**Tarkistukset (Pylint)
Koodin tarkistukset voi suorittaa komennolla `poetry run invoke lint` . Tarkistuksissa käytetään Pylint-moduulia ja se suoritetaan .pylintrc-tiedostossa määriteltyjä sääntöjä noudattaen.
