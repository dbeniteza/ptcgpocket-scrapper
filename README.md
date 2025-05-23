# Pokémon TCG Pocket Web Scraper

Python script scrapes the Limitless TCG Pocket website to extract card information such as name, type, HP, attacks, weaknesses, and more. It then converts this data into JSON.

## ✨ Features
- Scrapes card information from the Pokémon TCG Pocket website.
- Extracts data like name, type, HP, attacks, weaknesses, and image URLs.
- Saves the extracted data in JSON format.
- It can be used as an API by Pokémon Cards API

## 📦 Installation Guide
To get started with the Pokémon TCG Pocket Web Scraper:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dbeniteza/ptcgpocket-scrapper.git
   cd ptcgpocket-scrapper
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool**:
   ```bash
   python pokemontcgp_scrapper.py
   ```

## 🧪 Environment Setup
Make sure you have Python 3.x installed. This project uses:

- requests – for making HTTP requests
- beautifulsoup4 – for parsing HTML content

## 📊 Data Origins
The card data is sourced from the Limitless TCG Pocket website. This data includes card names, types, HP, attacks, weaknesses, and image URLs, and is used to build a structured dataset in JSON format.

## 🖼️ Sample Card Preview
Here’s an example of a Pokémon card image scraped from the site:

![Sample Pokémon Card](https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1/A1_036_EN.webp)

## Card info - Charizard ex

**ID**: 36

**Name**: Charizard ex

**HP**: 180

**Type**: Fire

**Card Type**: Pokémon - Stage 2 - Evolves from Charmeleon

**Evolution Type**: Stage 2

## Attacks
- **Name**: Slash
  - **Cost**: Fire, Colorless, Colorless
  - **Damage**: 60
  - **Effect**: 

- **Name**: Crimson Storm
  - **Cost**: Fire, Fire, Colorless, Colorless
  - **Damage**: 200
  - **Effect**: Discard 2 [R] Energy from this Pokémon.

## Ability
- **Name**: No ability
- **Effect**: N/A

**Weakness**: Water

**Retreat**: 2

**Rarity**: ◊◊◊◊

**Full Art**: No

**EX**: Yes

**Set Details**: Genetic Apex  (A1)

**Pack**: Charizard pack

## Alternate Versions
- **Version**: Genetic Apex #36
  - **Rarity**: ◊◊◊◊

- **Version**: Genetic Apex #253
  - **Rarity**: ☆☆

- **Version**: Genetic Apex #280
  - **Rarity**: ☆☆☆

- **Version**: Genetic Apex #284
  - **Rarity**: ♛

**Artist**: PLANETA Mochizuki

## Probability
- **1-3 card**: 0.000%
- **4 card**: 1.666%
- **5 card**: 6.664%

**Crafting Cost**: 500
