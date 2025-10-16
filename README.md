# DUNEMINDS


DUNEMINDS is a notebook-based deep learning model developed to map dune crest lines based on semantic segmentation. It includes all steps of the workflow from data access and pre-processing to model training and inference.
The repository includes an interactive notebook customised to be run through Google Colaboratory as well as helper scripts.

---

## 1. Overview

This repository includes:

- **`duneminds_original.ipynb`** — the main interactive notebook.
- **`model_1_directory_creation.py`** — helper script that creates the standard folder hierarchy.
- **`model_1_datadownload.py`** — helper script for the download of digital elevation models / optical satellite imagery.
- **`model_1_functions.py`** — helper script for various utilities.

- 
The notebook uses **interactive dropdown menus and widgets**, so running it in **Google Colab** is recommended.

---

## 2. Running in Google Colab (recommended set-up)


   - Upload `duneminds_original.ipynb` and the three helper scripts to the same folder in your Google Drive.
   - If the `.py` scripts are located in different folders, the paths in `duneminds_original.ipynb` need to be updated.

