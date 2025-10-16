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




# Data

Pre-processed training data can be obtained [here](https://drive.google.com/drive/folders/1-TrPQzy8tLkgg-vgebODLxou5t6dp9dN?usp=sharing).

## Folder structure:

pp_data/                        # preprocessed tiles for training & testing
├── train_pp/                   # preprocessed training data
│   ├── labels/                 # label rasters (dune crest lines)
│   ├── dem/                    # digital elevation model tiles
│   ├── curv/                   # curvature rasters derived from DEM
│   ├── curv_smooth/            # smoothed curvature rasters
│   ├── dune_height/            # dune height rasters
│   └── sentinel/               # Sentinel satellite imagery tiles
│
└── test_pp/                    # preprocessed test data
    ├── tiles_96/               # small test tiles (96×96 px)
    │   ├── sentinel/           # Sentinel image tiles
    │   └── dem/                # DEM test tiles
    │
    └── tiles_9600/             # large-area test tiles (9600×9600 px)
        ├── sentinel/           # large Sentinel image tiles
        └── dem/                # DEM tiles for large test areas

