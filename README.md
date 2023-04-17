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
Ohjelma ei vaadi erillistä asennusta vaan sitä pystyy käyttämään suoraan - Pythonilla. 

## Komentorivitoiminnot
**Suoritus**
- Tällä hetkellä ohjelman voi suorittaa komennoilla `python3 flashcards.py` tai Poetryn virtuaaliympäristössä komennoin `poetry run python src/flashcards.py`
- Tulevaisuudessa ohjelman pystyy suorittamaan komennolla `poetry run invoke start`. Tällä hetkellä se ei vielä ole mahdollista: kehitysympäristönä on Windows eikä siinä toimi pty=True vaihtoehto. Ja virtuaaliympäristössä Poetrya ei voi myöskään käyttää virheen takia. 

Ohjelman pystyy **testaamaan** pytestin avulla komennolla `poetry run invoke test` tai `python3 flashcards_test.py`

Ohjelman pystyy **suorittamaan** komennolla `poetry run invoke coverage-report` tai `python3 flashcards.py`

