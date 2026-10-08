using namespace System.Net

param($Request, $TriggerMetadata)

$namn = $Request.Body.namn
$epost = $Request.Body.epost
$meddelande = $Request.Body.meddelande

$body = @{
status = "Tack!"
message = "Vi har mottagit ditt ärende."
namn = $namn
epost = $epost
} | ConvertTo-Json

Push-OutputBinding -Name Response -Value (
[HttpResponseContext]@{
StatusCode = [HttpStatusCode]::OK
Headers = @{
"Content-Type" = "application/json; charset=utf-8"
}
Body = $body
}
)
