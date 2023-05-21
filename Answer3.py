import requests
# We have to utilize the requests library to download the data and the pandas library to manipulate and export the data in Excel format
import pandas as pd

def download_data_and_convert_to_excel(link):
    # Downloading the data from the link
    response = requests.get(link)
    data = response.text

    # Converting the data into a structured format
    structured_data = data.split('\n')
    
    # Create a DataFrame from the structured data
    df = pd.DataFrame(structured_data, columns=["Data"])

    # Convert the DataFrame to Excel format
    excel_data = df.to_excel("output.xlsx", index=False)
    
    return excel_data

# Testing
link = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"  # Replace with the actual link to download the data
download_data_and_convert_to_excel(link)
