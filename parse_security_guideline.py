import pandas as pd
import csv

# guideline can be also found on Microsoft Github page
# guideline_github_url="https://github.com/MicrosoftDocs/windowsserverdocs/blob/master/WindowsServerDocs/security/windows-services/security-guidelines-for-disabling-system-services-in-windows-server.md"

guideline_url = "https://docs.microsoft.com/en-us/windows-server/security/windows-services/security-guidelines-for-disabling-system-services-in-windows-server"
csv_headers = ["Service name", "Description", "Installation",
               "Startup type", "Recommendation", "Comments"]
service_descriptions_all = []


def parse_guideline_html(guideline_url):
    tables = pd.read_html(guideline_url)
    services_tables = tables[2:]
    return services_tables


def create_guideline_dictionary(services_tables):
    for service in services_tables:
        service_description = service["Description"]
        iterator = 0
        service_descriptions = {}
        for item_name in csv_headers:
            service_descriptions[item_name] = service_description[iterator]
            iterator += 1
        service_descriptions_all.append(service_descriptions)
    return service_descriptions_all


def save_guideline_csv(service_descriptions_all):
    with open('service_security_guideline.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, csv_headers)
        dict_writer.writeheader()
        dict_writer.writerows(service_descriptions_all)
        print("File service_security_guideline.csv successfully created")


if __name__ == "__main__":
    services_tables = parse_guideline_html(guideline_url)
    if services_tables:
        service_descriptions_all = create_guideline_dictionary(services_tables)
        save_guideline_csv(service_descriptions_all)
