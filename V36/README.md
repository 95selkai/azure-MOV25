# Vecka 36 - Azure nätverk för Novatrix

## Delmoment 1 - Repo
Jag har uppdaterat repot med dokumentation för vecka 36.

## Delmoment 2 - Virtuellt nätverk
Jag använder VNet `Vnet-novatrix` med adressutrymmet `10.0.0.0/16`.

Subnät:
- `Snet-web` - `10.0.1.0/24`
- `Snet-db` - `10.0.2.0/24`
- `default` - `10.0.0.0/24`

Webbservern `vm-novatrix-web2` ligger i `Snet-web`.
Privat IP: `10.0.1.6`
Publik IP: `135.116.199.8`

## Delmoment 3 - Säkerhet
NSG: `NSG-web`

Regler:
- HTTP/HTTPS: port 80 och 443 från Internet
- SSH: port 22 endast från administratörens IP
- Övrig inkommande trafik blockeras

## Delmoment 4 - Placering
Webbservern ligger i det publika subnätet `Snet-web`.
`Snet-db` är förberett som privat subnät för backend och lagring.

## Delmoment 5 - Verifiering
HTTP testades med:

```bash
curl -I http://135.116.199.8
