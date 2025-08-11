# Bulk CIF Downloader – Materials Project API

A Python script that automatically **bulk downloads** `.cif` (Crystallographic Information Files) from the [Materials Project](https://materialsproject.org/) using their API.  

---

## ✨ Features
- 🔹 Download `.cif` files for thousands of materials automatically
- 🔹 Works with **chemical formulas** instead of outdated material IDs
- 🔹 Keeps a **log file** (`log.txt`) containing
- 🔹 Overwrites log file each run to keep things clean

---

## 📦 Requirements
- Materials Project API Key ([materialsproject.org](https://materialsproject.org/))
- Python packages:
  ```bash
  pip install mp-api
  
---

## 🔨 Usage
- Get The api key from [Material Project](https://next-gen.materialsproject.org/api)
   <img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/36628cf0-e584-414e-93bc-36b2f8d90d34" />
- Add your API key in `runit.py` file, save and exit it
- Next open the `formulas.txt` file and manually add the name of the elements that you want to bulk download
- Open your terminal, cd into Downloads\CIF-Downloader folder 
- Execute the `runit.py` file
- A log file and a folder for the downloaded cif files should be created with the data within them

---

## Important Note

- If the repository is downloaded locally, It has to be present in the `Downloads` directory as accordance with the code.































