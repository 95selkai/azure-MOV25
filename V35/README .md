# V35 – IAM och identitet

## Delmoment 1 – Repo
Jag har skapat ett avsnitt för V35 i mitt kursrepo och uppdaterat README.

## Delmoment 2 – Identiteter
Jag skapade användare och grupper i Microsoft Entra ID för Novatrix.

## Delmoment 3 – RBAC
Jag tilldelade roller på resursgruppen enligt principen least privilege.

Azure drift = Contributor
Novatrix utveckling = Reader

## Delmoment 4 – Managed Identity
Jag skapade en User Assigned Managed Identity för applikationen.
Identiteten har ingen behörighet ännu. Den kopplas till lagringen i V37.

## Delmoment 5 – Verifiering
Jag kontrollerade rolltilldelningarna under Access Control (IAM) → Role assignments.
Rollerna är begränsade efter användarnas behov.
