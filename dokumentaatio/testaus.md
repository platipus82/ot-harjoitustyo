
# Testausdokumentti

## Yksikkö- ja integraatiotestaus
## Sovelluslogiikka
Sovelluslogiikasta vastaavat `Play`- ja `App`-luokat testataan [TestPlay](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/tests/flashcards_test.py)- ja [TestApp](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/tests/flashcards_test.py)  testiluokilla.
`TestPlay`-testiluokka luo sovelluksessa käyttämää [`Play`-luokkaa](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/processes/play.py) vastaavan olion. `TestPlay`-testiluokan metodi  `test_update_question_counters` testaa että `Play`-luokan olion `update_question_counters`-metodi toimii ja päivittää luokan attribuutit `questions_n_correct` ja `questions_n_answered` oikein, perustuen luokan sisäisen attribuutin `__ui.last_question_correct` arvoon. `TestPlay` luokka arvioi kahta skenaariota, eli tilantteita jossa viimeiseen kysymykseen vastattiin oikein, tai viimeiseen kysymykseen vastattiin väärin. 
`TestApp`-testiluokka testaa sovelluksen käyttämää [`App`-luokaa](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/processes/app.py) sekä sen vuorovaikutusta ja integraatiota luokkien [`Play`](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/processes/play.py) ja [`Database`](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/repositories/database.py) kanssa. Testiluokka tarkistaa onko syötetiedostohakemisto (`App`-luokan attribuutti `input_dir`) olemassa, metodin `test_that_inputdir_exists`-avulla. Tämä on keskeistä myöhemmille tiedostokäsittelytoiminnoille. Lisäksi `TestApp`-arvioi että syötetiedostoluettelo ei ole tyhjä eli siinä on syötetiedostoja prosessoitavana (metodi `test_that_inputfilelist_not_empty`), syötetideosto on olemassa (metodi `test_that_inputfile_exists`), se ei ole tyhjä (metodi `test_that_inputfile_is_not_empty`) ja että sen formaatti vastaa sovelluksen oletuksia ja on oikean muotoinen  (metodi `test_that_inputfile_is_formatted_correctly`). 

## Repositories-luokat
`TestDatabase`-testiluokka testaa sovelluksen käyttämiä `Database`- ja [`DatabaseInteractions`](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/repositories/database_interactions.py)-luokkia ja niiden yhteistoimintaa. Testataan että toimivasta tietokannasta data voidaan lukea ja tallentaa oikein, sekä tilannetta missä datan lukeminen epäonnistuu tuottaen OSError-virheen. Testiluokka luo `Database`-olion, lukee dataa simuloidusta tietokantatiedostosta ja tarkistaa että data onnistuneesti tallennettin `DatabaseInteractions` luokan attribuutiksi (metodi `test_get_db_data_success`). Testiluokan metodi `test_get_db_data_failure` tuottaa simuloidun tietokantatiedoston lukuvirheen (OSError) ja testaa että  `get_db_data` metodi asettaa luokan data-attribuutiksi tyhjän listan. 

[`TestDatabaseFileHandling`](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/tests/flashcards_tests.py)-testiluokka testaa sovelluksen luokkaa [`DatabaseFileHandling`](https://github.com/platipus82/ot-harjoitustyo/blob/main/src/repositories/database_file_hangling.py). Testiluokan metodi `test_make_new_sql_db_file` testaa sovelluksen `DatabaseFileHandling`-luokan metodia ´make_new_sql_db_file` ja tarkistaa että metodi luo uuden SQL-tietokanta-tiedoston ja siihen tarvittavan taulun ”Records”. Tällä tavalla varmistetaan että SQL-tietokanta on alustettu oikein ja siihen voidaan varastoida käyttöhistoria ja käyttäjätietoja. 

## Yhteenveto 
Näiden testien tarkoituksena on varmistaa että sovelluksen toiminnan kannalta kriittisten `Play`, `App`, `Database`, ja `DatabaseFileHandling`- luokkien toiminta ja vuorovaikutus on odotetun kaltainen ja robusti. Testeillä varmistetaan tärkeimpien metodien ja attribuuttien toiminta erilaisissa käyttö- ja virhe-skenaarioissa. Lisäksi testit toimivat sovelluksen laatudokumentaationa niitä voidaan hyödyntää sovelluksen jatkokehityksessä varmistamaan tulevien päivitysten toimivuutta. 

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
