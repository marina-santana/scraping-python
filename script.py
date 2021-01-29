import json
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    executable_path='C:/Users/{user}/Downloads/chromedriver_win32/chromedriver.exe')

array_elements = []

id = 1

while (id <= 118):
    url = "https://pubchem.ncbi.nlm.nih.gov/periodic-table/#popup={}".format(
        id)

    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content)

    def find_span(data_label, symbol):
        formatted_string = data_label.format(symbol)
        href = soup.find(
            "a", {"data-label": formated_string})

        if href:
            span = href.find("span", {"class": "capitalized"})
            if span:
                return span.text
            else:
                return "N/A"
        else:
            return "N/A"

    def find_div(class_name):
        div = soup.find(
            "div", {"class": class_name})

        if div:
            return div.text
        else:
            return "N/A"

    symbol = find_div("f-3")
    name = find_div("f-125 f-lh-15")
    type_element = find_div("f-0875 capitalized f-lh-15")
    standard_state = find_span(
        'Content Link (List View): {}; Standard State Property Value', symbol)
    atomic_mass = find_span(
        "Content Link (List View): {}; Atomic Mass Property Value", symbol)
    electron_configuration = find_span(
        "Content Link (List View): {}; Electron Configuration Property Value", symbol)
    oxidation_states = find_span(
        "Content Link (List View): {}; Oxidation States Property Value", symbol)
    electronegativity = find_span(
        "Content Link (List View): {}; Electronegativity (Pauling Scale) Property Value", symbol)
    atomic_radius = find_span(
        "Content Link (List View): {}; Atomic Radius (van der Waals) Property Value", symbol)
    ionization_energy = find_span(
        "Content Link (List View): {}; Ionization Energy Property Value", symbol)
    electron_affinity = find_span(
        "Content Link (List View): {}; Electron Affinity Property Value", symbol)
    melting_point = find_span(
        "Content Link (List View): {}; Melting Point Property Value", symbol)
    boiling_point = find_span(
        "Content Link (List View): {}; Boiling Point Property Value", symbol)
    density = find_span(
        "Content Link (List View): {}; Density Property Value", symbol)
    year_discovered = find_span(
        "Content Link (List View): {}; Year Discovered Property Value", symbol)

    data = {"id": id, "symbol": symbol,
            "name": name,
            "type": type_element,
            "standardState": standard_state,
            "atomicMass": atomic_mass,
            "electronConfiguration": electron_configuration,
            "oxidationStates":	oxidation_states,
            "electronegativity": electronegativity,
            "atomicRadius":	atomic_radius,
            "ionizationEnergy":	ionization_energy,
            "electronAffinity":	electron_affinity,
            "meltingPoint":	melting_point,
            "boilingPoint":	boiling_point,
            "density": density,
            "yearDiscovered": year_discovered}

    array_elements.append(data)
    id = id + 1

driver.close()
with open('data.json', 'w') as f:
    json.dump(array_elements, f)
