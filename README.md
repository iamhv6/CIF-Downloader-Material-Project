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
## 📝 Available Metadata
 Input Molecule  `Na2VAgF6`
- Metadata

```py
elements=[Element Ag, Element F, Element Na, Element V],
nelements=4,
composition=Composition('Na2 V1 Ag1 F6'),
composition_reduced=Composition('Na2 V1 Ag1 F6'),
formula_pretty='Na2VAgF6',
formula_anonymous='ABC2D6',
chemsys='Ag-F-Na-V',
volume=159.65800192520845,
density=3.315499811878073,
density_atomic=15.965800192520845,
symmetry=SymmetryData(crystal_system=<CrystalSystem.cubic: 'Cubic'>, symbol='Fm-3m', number=225, point_group='m-3m', symprec=0.1, angle_tolerance=5.0, version='2.5.0'),
property_name='summary',
material_id=MPID(mp-1111313),
deprecated=False,
deprecation_reasons=None,
last_updated=datetime.datetime(2025, 6, 3, 23, 12, 42, 675000, tzinfo=datetime.timezone.utc),
origins=[PropertyOrigin(name='structure', task_id=MPID(mp-1921789), last_updated=datetime.datetime(2021, 2, 10, 4, 29, 15, 625000, tzinfo=datetime.timezone.utc)), PropertyOrigin(name='energy', task_id=MPID(mp-1921789), last_updated=datetime.datetime(2025, 4, 7, 17, 4, 28, 26000, tzinfo=datetime.timezone.utc)), PropertyOrigin(name='electronic_structure', task_id=MPID(mp-1921789), last_updated=datetime.datetime(2021, 2, 10, 4, 29, 15, 625000, tzinfo=datetime.timezone.utc)), PropertyOrigin(name='magnetism', task_id=MPID(mp-1921789), last_updated=datetime.datetime(2021, 2, 10, 4, 29, 15, 625000, tzinfo=datetime.timezone.utc))],
warnings=[],
structure=Structure Summary
Lattice
    abc : 6.089317 6.089317064933472 6.089316716239433
 angles : 59.99999785570633 59.999993026071536 59.999994920324866
 volume : 159.65800192520845
      A : np.float64(6.089317) np.float64(0.0) np.float64(0.0)
      B : np.float64(3.044659) np.float64(5.273503) np.float64(0.0)
      C : np.float64(3.044659) np.float64(1.757834) np.float64(4.971906)
    pbc : True True True
PeriodicSite: Na (3.045, 1.758, 1.243) [0.25, 0.25, 0.25]
PeriodicSite: Na (9.134, 5.274, 3.729) [0.75, 0.75, 0.75]
PeriodicSite: V (0.0, 0.0, 0.0) [0.0, 0.0, 0.0]
PeriodicSite: Ag (6.089, 3.516, 2.486) [0.5, 0.5, 0.5]
PeriodicSite: F (4.42, 4.479, 1.123) [0.2259, 0.7741, 0.2259]
PeriodicSite: F (7.759, 4.479, 1.123) [0.7741, 0.7741, 0.2259]
PeriodicSite: F (7.759, 2.552, 3.849) [0.7741, 0.2259, 0.7741]
PeriodicSite: F (6.089, 1.588, 1.123) [0.7741, 0.2259, 0.2259]
PeriodicSite: F (6.089, 5.443, 3.849) [0.2259, 0.7741, 0.7741]
PeriodicSite: F (4.42, 2.552, 3.849) [0.2259, 0.2259, 0.7741],
task_ids=[MPID(mp-1921789), MPID(mp-1111522), MPID(mp-1111313)],
uncorrected_energy_per_atom=-4.681280642,
energy_per_atom=-8.666359119499997,
formation_energy_per_atom=-2.533360947999998,
energy_above_hull=0.23844848950000103,
is_stable=False,
equilibrium_reaction_energy_per_atom=None,
decomposes_to=[DecompositionProduct(material_id=MPID(mp-1120790), formula='Na8 V4 F20', amount=0.4), DecompositionProduct(material_id=MPID(mp-3240155), formula='Na1 V1 F5', amount=0.34999999999999903), DecompositionProduct(material_id=MPID(mp-1391), formula='Ag2 F1', amount=0.15000000000000002), DecompositionProduct(material_id=MPID(mp-682), formula='Na1 F1', amount=0.099999999999999)],
xas=None,
grain_boundaries=None,
band_gap=0.0,
cbm=None,
vbm=None,
efermi=0.9346998,
is_gap_direct=False,
is_metal=True,
es_source_calc_id=None,
bandstructure=None,
dos=None,
dos_energy_up=None,
dos_energy_down=None,
is_magnetic=True,
ordering='FM',
total_magnetization=2.0002905,
total_magnetization_normalized_vol=0.012528595346802,
total_magnetization_normalized_formula_units=2.0002905,
num_magnetic_sites=1,
num_unique_magnetic_sites=1,
types_of_magnetic_species=[Element V],
bulk_modulus=None,
shear_modulus=None,
universal_anisotropy=None,
homogeneous_poisson=None,
e_total=None,
e_ionic=None,
e_electronic=None,
n=None,
e_ij_max=None,
weighted_surface_energy_EV_PER_ANG2=None,
weighted_surface_energy=None,
weighted_work_function=None,
surface_anisotropy=None,
shape_factor=None,
has_reconstructed=None,
possible_species=['Na+', 'Ag+', 'V3+', 'F-'],
has_props={'materials': True, 'thermo': True, 'xas': False, 'grain_boundaries': False, 'chemenv': True, 'electronic_structure': True, 'absorption': False, 'bandstructure': False, 'dos': False, 'magnetism': True, 'elasticity': False, 'dielectric': False, 'piezoelectric': False, 'surface_properties': False, 'oxi_states': True, 'provenance': True, 'charge_density': True, 'eos': False, 'phonon': False, 'insertion_electrodes': False, 'substrates': False},
theoretical=True
```

## Important Note

- If the repository is downloaded locally, It has to be present in the `Downloads` directory as accordance with the code.































