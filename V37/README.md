## Vecka 37 - Managed Identity och Blob Storage
Denna vecka konfigurerade jag Managed Identity för vm-novatrix-web2 och gav identiteten rollen
Storage Blob Data Contributor på novatrixstorage. Jag installerade Azure CLI på VM:n och
verifierade inloggningen med az login --identity. Därefter testade jag åtkomsten till containern
arenden och kunde lista blob-filer utan att använda lagringsnycklar.
