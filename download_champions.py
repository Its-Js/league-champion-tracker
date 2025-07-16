import os
import requests

# 1. Get the latest version
versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
latest = versions[0]
print(f"✅ Latest Data Dragon version: {latest}")

# 2. Fetch champion data
url = f"https://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion.json"
resp = requests.get(url).json()
champ_data = resp["data"]

# 3. Prepare output folder
os.makedirs("champions", exist_ok=True)

# 4. Build list of champion names and download square images
for champ_key, info in champ_data.items():
    name = info["name"]
    image_filename = info["image"]["full"]  # e.g. "Aatrox.png"
    img_url = f"https://ddragon.leagueoflegends.com/cdn/{latest}/img/champion/{image_filename}"

    # Save image
    img_data = requests.get(img_url).content
    path = os.path.join("champions", image_filename)
    with open(path, "wb") as f:
        f.write(img_data)

    print(f"📥 Downloaded {name} → {image_filename}")

# 5. Save names to a text file
with open("champion_names.txt", "w", encoding="utf-8") as f:
    for info in champ_data.values():
        f.write(info["name"] + "\n")
