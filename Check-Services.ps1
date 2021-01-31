$service_guidelines=Import-CSV -Path "service_security_guideline.csv"

$service_list = $service_guidelines | Where-Object { $_.Recommendation -notin "Do not disable", "No guidance"}

foreach ($service in $service_list)
{
    $service_name=Get-Service -Name $service.'Service name'
    if ($service_name.Status -ne "Stopped")
    {
        Write-Host("Service " + $service_name.Name + "is enabled. Due to security guideline this service recommended to be disabled") -fore red
    }
}
