from flask import Flask, jsonify
import requests
import csv

app = Flask(__name__)

def get_characters():
    link = "https://rickandmortyapi.com/api/character"
    data = {
        "species": "Human",
        "status": "Alive",
        "origin": "Earth"
    }
    response = requests.get(link, params=data)
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

# Fetch characters
@app.route('/characters', methods=['GET'])
def fetch_characters():
    characters = get_characters()
    if characters:
        return jsonify(characters), 200
    else:
        return jsonify({"error": "Failed to fetch characters"}), 500

# Health check
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    main()
    app.run(debug=True, host='0.0.0.0')
