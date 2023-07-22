
# Testausdokumentti

## Yksikkö- ja integraatiotestaus

### Testikattavuus
Käyttöliittymäkerrosta ei ole testattu. Muuilta osin sovelluksen testauksen haarautumakattavuus on 71%
![](./kuvat/coverage_report.JPG)

## Järjestelmätestaus
### Asennus 
Viimeisin sovellusversio on haettu ja sitä on testattu [käyttöohjeen](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md) kuvaamalla tavalla Windows- ja Linux-ympäristössä.
Sovellusta on testattu tilanteissa joissa
- käyttäjä on uusi tai entuudestaan tuttu
- syötetiedostostot ovat olemassa tai puuttuvat
- tietokantatiedostot ovat olemassa tai puuttuvat
- kaikilla käyttömoodeilla, mukaan lukien ajastettu läpikäynti
- oikeilla, virheellisillä ja puuttuvilla vastauksilla ja syötteillä

Käyttäjäyhteenvedon oikeellisuudet on myös tarkistettu. 


### Toiminnallisuudet
Kaikki [vaatimusmäärittelydokumentin](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md) mukaiset toiminnallisuudet on testattu ja ne toimii.

## Sovelluksen laatuongelmat
Sovellusta on pyritty testaamaan monipuolisesti erilaisissa tilanteissa - myös puuttuvilla tai virheellisillä syötteillä ja tiedostoilla. 
Mahdolliset virhetilanteet on käsitelty siten että sovellus ei kaadu virheellisillä syötteillä vaan kysyy tietoja uudelleen kunnes validi syöte on annettu tai oikea tiedosto on löytynyt. Sovellus ei siten kaadu testatuissa tilanteissa - eikä myöskään anna virheilmoituksia koska niille ei ole tarvetta. Toisaalta, ei myöskään voida täysin poissulkea sellaista mahdollisuutta että jotain virhetilannetta ei testattu tai huomioitu. Siten emme voi myöskään taata sovelluksen tarkoituksenmukaista käyttäytymistä sellaisessa tilanteessa - tai järkevää virheiden käsittelyä. 
