
# Nordvik Fastigheter AB – Hyresgästportal i Azure

## Syfte
Syftet med projektet är att planera, implementera och dokumentera en säker hyresgästportal i Microsoft Azure. Portalen gör det möjligt för hyresgäster att skicka in felanmälningar med rubrik, beskrivning och en bifogad bild.

---

## Projektets arkitektur och resurser

### 1. Compute
* **Virtuell Maskin (VM):** `vm-nordvik-web` (Ubuntu 24.04 LTS, Standard B2ts v2) placerad i resursgruppen `RG-NORDVIK2` (region *Sweden Central*).
* **Serverless:** Azure Functions som hanterar händelsestyrd logik vid inskickade ärenden.
* **Offentlig IP-adress:** `135.225.114.161`.

### 2. IAM och Least Privilege
* **Rollbaserad Åtkomstkontroll (RBAC):**
  * **Hyresgäst:** Skapar nya felanmälningar samt ser sina egna ärenden.
  * **Förvaltare:** Full behörighet att hantera, tilldela och ändra status på alla felanmälningar.
  * **Ekonomi:** Tilldelas rollen *Läsare (Reader)* för uppföljning och kostnadskontroll.
* **Hanterad Identitet (Managed Identity):** `vm-nordvik-web` och Azure Functions har tilldelats en **System-assigned Managed Identity** med rollen **Storage Blob Data Contributor** på lagringskontot. Det gör att portalen säkert kan skriva till lagringen utan hårdkodade nycklar.

### 3. Nätverk och Säkerhet (Defense in Depth)
* **Virtuellt Nätverk:** `vnet-swedencentral-1` / `snet-swedencentral-1`.
* **Perimetersäkerhet:** Inkommande HTTPS-trafik filtreras via Network Security Group (NSG).
* **Lagringsskydd:** Anonym publik åtkomst är inaktiverad på alla blob-containrar
* . Åtkomst kräver Microsoft Entra ID-autentisering eller intern nätverkskoppling.

### 4. Storage
* **Storage Account:** `stnordvikselma01` (StorageV2) placerat i `RG-NORDVIK2`.
* **Blob Containrar:**
  * `felanmalningar`: Privat container för säker lagring av uppladdade bildfiler och underlag.
  * `app-package-func-nordvik-felanmla...`: Används för automatisering och applikationspaket.

### 5. Automation och M365-integration
Arbetsflöde i **Power Automate** kopplat mot Nordviks tenant (`novatrix736.onmicrosoft.com`):
1. När formuläret skickas in aktiveras flödet via ett HTTP-anrop.
2. En ny post skapas i förvaltarens **SharePoint Online**-lista med alla ärendedetaljer och bildlänk från `stnordvikselma01`.
3. Ett **Adaptive Card** skickas som notis till förvaltaren via Microsoft Teams / Outlook för snabb hantering.

---

## Repostruktur

```text
V41 Nordvik Fastigheter AB 
├── README.md                  # Dokumentation
├── azuredeploy.json           # ARM-template för infrastrukturen
├── azuredeploy.parameters.json # Parametrar för ARM-deployment
└── index.html                 # Källkod för portalens formulär
