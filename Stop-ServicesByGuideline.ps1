$services_guideline=Import-CSV -Path "service_security_guideline.csv"

$service_list = $services_guideline | Where-Object { $_.Recommendation -notin "Do not disable", "No guidance"}

foreach ($service in $service_list)
{
    $service_name=Get-Service -Name $service.'Service name'
    if ($service_name.Status -ne "Stopped")
    {
        Stop-Service -Name $service.'Service name' -Force
        Write-Host("Service " + $service.'Service name' + " stopped.") -fore red
    }
}
