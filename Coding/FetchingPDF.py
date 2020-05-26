import tabula

file = "https://apps.health.tn.gov/AEM_embed/TDH-2019-Novel-Coronavirus-Epi-and-Surveillance.pdf"
# tables = tabula.read_pdf(file, pages = "all", multiple_tables = True)

# output all the tables in the PDF to a CSV
# tabula.convert_into(file, "Testing.csv", all = True)
tabula.convert_into_by_batch("Data/Test", output_format = "csv", pages = "all")