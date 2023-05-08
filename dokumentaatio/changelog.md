## Viikko 3

- flashcards-projektin ensimmäinen toimiva implementaatio toteutettu
- sovellus lukee .txt-muotoisen tiedoston ja käy läpi sen kysymykset näyttäen ensin kysymyksen ja sitten vastauksen
- tekstikäyttöliittymä
- testattu että toimii Windows- ja Linux ympäristöissä 

## Viikko 4

- flashcards-projektin toinen toimiva implementaatio toteutettu
- käyttäjälle näytetään lista input-kansiossa olevista tekstitiedostoista
- käyttäjä voi valita haluamansa tiedoston
- sovellus lukee .txt-muotoisen tiedoston ja käy läpi sen kysymykset näyttäen ensin kysymyksen ja sitten vastauksen
- sovellukseen lisätty mahdollisuus keskeyttää ohjelman suoritus missä vaiheessa tahansa
- tekstikäyttöliittymä
- testattu että toimii Windows- ja Linux ympäristöissä eli tarkistaa toimiiko tiedostopolku ja jos ei toimi niin käyttää vaihtoehtoista syntaksia
- ohjelman rakenne muutettu luokka-muotoiseksi jatkokehityksen helpottamiseksi
- .coveragerc tiedosto lisätty juurihakemistoon ja testien ulkopuolelle määritelty __init__.py-tiedostot, sekä tests- ja inputs-kansioiden sisällöt


## Viikko 5

- flashcards-sovelluksen kolmas toimiva versio
- sovellukselle luotu GUI
- testattu että toimii Windows- ja Linux ympäristöissä 
- testattu että toimii myös `poetry invoke` syntaksilla

## Viikko 6

- flashcards-sovelluksen neljäs toimiva versio
- GUI päivitetty niin että ikkuna pysyy samankokoisena ja samassa paikassa
- sovelluksen prosessia päivitetty niin että kysymykset näytetään satunnaisessa järjestyksessä
- pakkausta parannettu niin että kukin luokka on omana tiedostonaan, käyttäjävuorovaikutuksesta ja muista prosesseista vastaavat skriptit eriytetty omiin kansioihin 
- testattu että toimii Windows- ja Linux ympäristöissä 
- testattu että toimii myös `poetry invoke` syntaksilla

## Viikko 7
- flashcards-sovelluksen viides toimiva versio
- sovellukseen lisätty tiedon pysyväistallennus _.csv_ formaatissa
- ohjelman päätytyttyä käyttäjälle näytetään yhteenveto päättyneestä käyttökerrasta sekä koko käyttöhistoriasta
- sovellukseen lisätty tiedon tallennus SQL-tietokantaan

