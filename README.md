# Ohjelmistotekniikka 2023

# Harjoitustyö
## Kuvaus
Flashcards sovelluksen avulla käyttäjät voivat opetella asioita digitaalisten opettelukorttien avulla (eng. *flashcards*). Kortit on ryhmitelty kokoelmiin. 



## Dokumentaatio
[Vaativuusmaarittely](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Muutosloki](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.MD)

[Käyttöohje](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

## Sovelluksen versiot
[viikko5](https://github.com/platipus82/ot-harjoitustyo/releases/tag/viikko5v4)
[viikko6](https://github.com/platipus82/ot-harjoitustyo/releases/tag/viikko6v2)
[viikko8+](https://github.com/platipus82/ot-harjoitustyo/releases/tag/viikko8plus)

## Asennus ja käyttö
1. Ohjelman lataus. Lataa ohjelman viimeisin versio (_release_) [täältä](https://github.com/platipus82/ot-harjoitustyo/releases/tag/viikko8plus) haluamaasi kansioon.
2. Python-versio. Ohjelma on toteutettu ja testattu pythonin 3.8-versiolla. Yhteensopivuutta muiden python-versioiden kanssa ei ole testattu. Tarkista oma python-versio komennolla `python3 --version` tai `python --version` ja tarvittaessa päivitä se.
3. Riippuvuuksien asennus. Asenna riippuvuudet ohjelmahakemistoon komennolla `poetry install`
4. Käynnistä sovellus komennolla `poetry run invoke start`


## Komentorivitoiminnot
**Suoritus**

Ohjelman voi suorittaa komennoilla
- `poetry run invoke start` 
- `python3 flashcards.py` 
- `poetry run python src/flashcards.py` poetryn virtuaaliympäristössä 


**Testaus**

Ohjelman pystyy testaamaan pytestin avulla komennolla `poetry run invoke test` tai `python3 flashcards_test.py`


**Testikattavuus**

Ohjelman testikattavuuden voi kartoittaa komennolla `poetry run invoke coverage`. Html-muotoisen raportin voi tuottaa komennolla `poetry run invoke coverage-report`. Raportti sijoitetaan hakemistoon _htmlcov_.


**Tarkistukset (Pylint)**

Koodin tarkistukset voi suorittaa komennolla `poetry run invoke lint`. Tarkistuksissa käytetään Pylint-moduulia ja se suoritetaan [.pylintrc-tiedostossa](https://github.com/platipus82/ot-harjoitustyo/blob/main/.pylintrc) määriteltyjä sääntöjä noudattaen.
