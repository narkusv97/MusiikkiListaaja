# MusiikkiListaaja

Update Välipalautus 2:

Yritin siirtää sovellusta herokuun mutten olen saanut sitä vielä toimimaan...

Siirsin sovelluksen tänne hetkellisesti listaten myös missä vaiheessa työ on:


Coded the main structure

-Main page (index) done visually.

-Adding Albums working as intended

-Listing Albums as intended


Need to do:

Search (not working)

Register (not working)

Log in/off (not working)

Modify album (haven't started)

Remove Album (changing viewable to False, haven't done)

own list (haven't started)

Security (haven't started)

Structure...

------------------------------------------------------------------------

Tarkoituksena on luoda musiikkilistaaja, jonne voi lisätä CD-levyjä.

Sovelluksella on käyttäjiä, jotka voivat lisätä uusia CD-levyjä sivulle.


Käyttö:

Käyttäjä voi luoda CD-levyn täyttämällä kenttiin tarvitut tiedot.

Käyttäjä voi muokata jo olemassa olevan CD-levyn tietoja muokkauspainikkeesta.

Käyttäjä voi hakea CD-levyn hakukentällä. (Voisi etsiä vuodella, nimellä, artistilla jne. tai ehkä niiden kombinaatiolla)

Käyttäjä voi luoda tunnuksen sivustolle, joka muistaa käyttäjän. (Käyttäjätunnus ja salasana)

Käyttäjä voi sisäänkirjauduttuaan lisätä/poistaa omaan kirjastoonsa CD-levyä, jotka näkyvät hänelle omassa listassa.



Sommittelu:

Alussa pääaukeama jossa näkyy osa CD-levyistä, CD hakukenttä, CD lisäysmahdollisuus ja rekisteröitymis-, kirjautumismahdollisuus.

Yksittäinen CD sivusto tulee sisältämään CD-levyn nimen, artistin, valmistusvuoden, genren/genret, ehkä kuvan cd-levystä ja lisäksi muokkausmahdollisuus.

Lisäysmahdollisuus tulee sisältämään tekstilaatikkoja CD:n tiedoille, jotka kaikki tulee täyttää CD:n sivustolle lisäämiseksi.
Jos kaikki ei täytetty, niin sivusto ilmoittaa ei täytetyistä tiedoista. Muuten lisäys onnistuu.

Muokkausmahdollisuus on periaatteessa sama kuin cd-lisäys. Tarkoituksena poistaa muistissa oleva CD-levy ja luoda uusi uusilla tiedoilla.

Rekisteröitymismahdollisuus ohjaa tunnuksen ja salasanan kyselyyn ja salasanan varmistamiseen, joka onnistuessa luo tunnuksen ja kirjaa sisään ja epäonnistuessa virheilmoitukseen.

Kirjautumismahdollisuus ohjaa tunnuksen ja salasanan kyselyyn joka onnistuessa kirjaa sisään ja epäonnistuessa virheilmoitukseen.

Kun on kirjautunut sisään niin näkyy mahdollisuudet kirjaudu ulos ja oma lista. Lisäksi näkyy uusi ominaisuus "lisää"  yksittäisellä CD sivustolla, joka lisää omaan listaan CD-levyn. 

Uloskirjautuminen kirjaa ulos ja näyttää pääaukeaman.

Oma lista näyttää lisätyt CD-levyt.
