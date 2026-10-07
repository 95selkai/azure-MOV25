# Vecka 39 – Power Automate och integration

## Delmoment 1 – Repo
Jag har skapat dokumentation för vecka 39 i mitt GitHub-repo.

## Delmoment 2 – Power Automate
Jag skapade ett Power Automate-flöde för Novatrix kundtjänst.

Flödet kan triggas när ett nytt ärende kommer in.

## Delmoment 3 – Microsoft 365
Power Automate är kopplat till Microsoft 365.

Jag har testat Outlook och verifierat att ett e-postmeddelande kan skickas automatiskt till kundtjänst.


## Delmoment 4 – Azure
Novatrix kundtjänstsida körs på en Debian-server med Nginx i Azure.

Formuläret innehåller:
- Namn
- Ärende
- Bifoga fil

Kedjan ska vara:

Novatrix formulär → Power Automate → SharePoint → Outlook

## Delmoment 5 – Verifiering
Power Automate och Outlook har testats och körningen lyckades.

Den slutliga kedjan verifieras genom att skicka ett ärende från Novatrix-formuläret och kontrollera att:
1. Power Automate startar.
2. Kundtjänst får en notifiering i Outlook.

## Konfiguration

Form-ID: arendeForm
Trigger: När en HTTP-begäran tas emot
Microsoft 365: Outlook
Server: Azure VM / Debian / Nginx
