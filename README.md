# Win-ServicesGuidelineChecker

Powershell scripts to check your corporate environment services on Windows Server 2016 whether they match Security Guideline.
Those script are used for Security Hardening Windows systems.

Best practices were prepared by Microsoft:
https://docs.microsoft.com/en-us/windows-server/security/windows-services/security-guidelines-for-disabling-system-services-in-windows-server.

* If you're using printer on your Windows Server, modify service_security_guideline.csv file to not disable it.

Many thanks to Microsoft team for providing such a great guideline=)

Guideline file: _service_security_guideline.csv_. You may change, modify it or create your own guideline.

Note, if file _service_security_guideline.csv_ doesn't exist in current folder, powershell script will download it from this github project.

## Usage

### Check-ServicesByGuideline
To check which services can be disabled on your corporate system (Windows Server 2016) environment, run:
```powershell
PS C:\Users\Leo\Downloads> .\Check-ServicesByGuideline.ps1
```
Example of output:
```
Service NcbService is enabled. Due to security guideline this service recommended to be disabled.
Service Spooler is enabled. Due to security guideline this service recommended to be disabled.
Service PcaSvc is enabled. Due to security guideline this service recommended to be disabled.
Service RmSvc is enabled. Due to security guideline this service recommended to be disabled.
Service ShellHWDetection is enabled. Due to security guideline this service recommended to be disabled.
Service SSDPSRV is enabled. Due to security guideline this service recommended to be disabled.
Service TabletInputService is enabled. Due to security guideline this service recommended to be disabled.
Service Audiosrv is enabled. Due to security guideline this service recommended to be disabled.
Service AudioEndpointBuilder is enabled. Due to security guideline this service recommended to be disabled.
Service WpnService is enabled. Due to security guideline this service recommended to be disabled.
Service WSearch is enabled. Due to security guideline this service recommended to be disabled.
```

### Stop-ServicesByGuideline
To stop services that can be disabled due to Microsoft Security Guideline run

```powershell
PS C:\Users\Leo\Downloads> .\Stop-ServicesByGuideline.ps1
```

Example of output:
```
Service NcbService stopped.
Service Spooler stopped.
Service PcaSvc stopped.
```

### parse_security_guideline.py

To update service_security_guideline.csv from official microsoft guideline run
```powershell
PS C:\Users\Leo\Downloads> python3 .\parse_security_guideline.py
```
