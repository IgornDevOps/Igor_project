import requests
import csv

def get_characters():
    link = "https://rickandmortyapi.com/api/character"
    data = {
        "species": "Human",
        "status": "Alive",
        "origin": "Earth"
    }
    response = requests.get(link, data = data)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def write_csv(characters, filename="rick_and_morty_characters.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Location", "Image"])
        for character in characters:
            writer.writerow([character["name"], character["origin"]["name"], character["image"]])
    print(f"Saved {len(characters)} characters to {filename}")

def main():
    characters = get_characters()
    if characters:
        write_csv(characters)
    else:
        print("No characters matching the data.")

if __name__ == "__main__":
    main()
