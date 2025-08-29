#v 1.1.1.2
from mp_api.client import MPRester
from pathlib import Path
import os

download_path = Path.home() / "Downloads" / "CIF-Downloader" / "Downloaded CIF"
#SAVE_DIR = r"C:\Users\<USER>\Downloads\project\Downloaded CIF"
download_path.mkdir(parents=True, exist_ok=True)

def bulk_download(api_key, formulas_file, log_file):
    with MPRester(api_key) as mpr:
        # Read formulas
        with open(formulas_file, "r") as f:
            formulas = [line.strip() for line in f if line.strip()]

        # Prepare log
        with open(log_file, "w") as log:
            log.write("Download Log\n")
            log.write("=====================\n")

            counter = 1
            for formula in formulas:
                try:
                    # Search for the formula
                    docs = mpr.summary.search(formula=formula)

                    if not docs:
                        print(f"No materials found for {formula}")
                        continue

                    # Take first match
                    doc = docs[0]
                    
                    ''' #
                    if doc.band_gap == 0:
                        print(f"Skipping {formula} (band gap = 0)")
                        continue
                    '''

                    mp_id = doc.material_id              # full ID with "mp-"
                    structure = mpr.get_structure_by_material_id(mp_id)

                   # Use only the number for filename
                    numeric_id = mp_id.replace("mp-", "")  
                    cif_filename = f"{numeric_id}.cif"
                    cif_path = os.path.join(download_path, cif_filename)

                    with open(cif_path, "w") as f:
                     f.write(structure.to(fmt="cif"))

                    log.write(f"{counter}. Formula: {formula}, MP ID: {mp_id}, Formation Energy: {doc.formation_energy_per_atom}\n")
                    print(f"Downloaded {cif_filename}")

                    counter += 1

                except Exception as e:
                    print(f"Error processing {formula}: {e}")



# ===== RUN =====
if __name__ == "__main__":
    API_KEY = "you_api_key"  # Replace with your MP API key
    FORMULAS_FILE = "formulas.txt"
    LOG_FILE = "download_log.txt"

    bulk_download(API_KEY, FORMULAS_FILE, LOG_FILE)




