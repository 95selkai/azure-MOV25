# Vecka 38 – ARM Templates

## Novatrix – Infrastructure as Code

Under vecka 38 arbetar jag med ARM-templates för att provisionera och återskapa delar av Novatrix miljö i Microsoft Azure.

### Delmoment
- Skapa ARM-template
- Provisionera Azure-resurser från kod
- Verifiera deployment
- Versionshantera ändringar med GitHub
- Dokumentera hur miljön kan återskapas från repot
## Deployment

ARM-templaten skapar följande resurser i Azure:

- Storage Account för Novatrix
- Virtual Network: novatrix-vnet
- Subnet för kundtjänsten

Resurserna skapades i resursgruppen `rg-novatrix-v38` i regionen `swedencentral`.

Deploymenten verifierades i Azure och resurserna fick status `Succeeded`.

## Återskapa miljön

Miljön kan återskapas från GitHub-repot genom Azure Cloud Shell.

Skapa först resursgruppen:

```bash
az group create --name rg-novatrix-v38 --location swedencentral
```

Deploya sedan ARM-templaten från GitHub:

```bash
az deployment group create --resource-group rg-novatrix-v38 --template-uri "https://raw.githubusercontent.com/95selkai/azure-MOV25/refs/heads/main/V38/azuredeploy.json"
```

Verifiera resurserna:

```bash
az resource list --resource-group rg-novatrix-v38 -o table
```

## Versionshantering

ARM-templaten versionshanteras med Git och GitHub. Jag gjorde en ändring av subnetet från `kundtjanst-subnet` till `kundtjanst-subnet-v2` och skapade en ny commit.

Versionshantering gör det möjligt att se vilka ändringar som har gjorts, jämföra olika versioner och gå tillbaka till en tidigare version vid behov. Det underlättar även samarbete eftersom ändringar dokumenteras i Git-historiken.
