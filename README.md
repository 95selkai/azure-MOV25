Novatrix - Driftsättning av kundtjänstsida
Namn: Selma
Kursuppgift: GitHub, Azure VM, Ubuntu, SSH och NginxDokumentation
I uppgiften har jag satt upp ett publikt kursrepo på GitHub, provisionerat en Ubuntu-VM i Microsoft
Azure, anslutit via SSH, installerat Nginx och driftsatt en enkel kundtjänstsida för Novatrix. Nedan
dokumenteras momenten och de kommandon som användes.
Delmoment 1 – Sätt upp kursrepo på GitHub
Jag skapade ett publikt GitHub-repository med namnet azure-MOV25. Repositoryt innehåller
README.md och webbsidans kod i index.html.
Verifiering: Repositoryt är publikt och filerna går att öppna på GitHub.
Delmoment 2 – Provisionera en virtuell server
Jag skapade en virtuell maskin i Azure för Novatrix. Operativsystemet är Ubuntu och servern heter
vm-novatrix-web. Jag valde en mindre VM för att undvika onödiga kostnader.
Verifiering: VM:n visas i Azure Portal och har en publik IP-adress.
Delmoment 3 – Anslut via SSH och installera Nginx
Jag anslöt till Ubuntu-servern via SSH. Därefter uppdaterade jag paketlistan och installerade Nginx. Jag
gick sedan till Nginx webbkatalog för att arbeta med webbsidan.
Kommandon:
ssh azureuser@51.12.241.133
sudo apt update
sudo apt install nginx
cd /var/www/html/
ls
sudo nano index.nginx-debian.html
Verifiering av Nginx
Nginx kan verifieras från servern och genom att öppna VM:ns publika IP-adress i en webbläsare.
sudo systemctl status nginx
curl http://localhost
Delmoment 4 – Driftsätt Novatrix kundtjänstsida
Jag skapade en enkel webbsida för Novatrix med ett ärendeformulär. Formuläret innehåller fälten
namn, e-post och meddelande samt en knapp. I detta moment behöver formuläret endast visas och inte
skicka data.
HTML-kod:

<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Novatrix Kundtjänst</title>
</head>
<body>
<h1>Välkommen till Novatrix</h1>
<p>Kontakta vår kundtjänst genom formuläret nedan.</p>
<form>
<label for="name">Namn:</label><br>
<input type="text" id="name" name="name"><br><br>
<label for="email">E-post:</label><br>
<input type="email" id="email" name="email"><br><br>
<label for="message">Meddelande:</label><br>
<textarea id="message" name="message"></textarea><br><br>
<button type="submit">Skicka</button>
</form>
</body>
</html>
Delmoment 5 – Verifiera och dokumentera
Jag verifierade driftsättningen genom att öppna serverns publika IP-adress i webbläsaren och
kontrollera att Novatrix-sidan och formuläret visas. Koden sparades i det publika GitHub-repositoryt.
Verifiering: Ubuntu-VM:n är skapad, SSH-anslutningen fungerar, Nginx är installerat och webbsidan
kan nås via serverns publika IP.
Sammanfattning
Uppgiftens fem delmoment är dokumenterade med beskrivningar, verifiering och kopierbara
kommandon. När Azure-resurserna inte används bör VM:n deallokeras eller resurserna tas bort för att
minimera kostnaden.
