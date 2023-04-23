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
Sovellus ei vaadi erillistä asennusta vaan sitä pystyy käyttämään suoraan - Pythonilla. 

Viimeisin versio (_release_) löytyy [täältä](https://github.com/platipus82/ot-harjoitustyo/releases/tag/viikko5)

## Komentorivitoiminnot
**Suoritus**
- Tällä hetkellä ohjelman voi suorittaa komennoilla `python3 flashcards.py` tai Poetryn virtuaaliympäristössä komennoin `poetry run python src/flashcards.py`
- Tulevaisuudessa ohjelman pystyy suorittamaan komennolla `poetry run invoke start`. Tällä hetkellä se ei vielä ole mahdollista: kehitysympäristönä on Windows eikä siinä toimi pty=True vaihtoehto. Ja virtuaaliympäristössä Poetrya ei voi myöskään käyttää [virheen](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/poetry_virhekuvaus.MD) takia. 


**Testaus**

Ohjelman pystyy testaamaan pytestin avulla komennolla `poetry run invoke test` tai `python3 flashcards_test.py`


**Testikattavuus**

Ohjelman testikattavuuden voi kartoittaa komennolla `poetry run invoke coverage`. Html-muotoisen raportin voi tuottaa komennolla `poetry run invoke coverage-report`. Raportti sijoitetaan hakemistoon _htmlcov_.


