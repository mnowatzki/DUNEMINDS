# DUNEMINDS


DUNEMINDS is a notebook-based deep learning model developed to map dune crest lines based on semantic segmentation. It includes all steps of the workflow from data access and pre-processing to model training and inference.
The repository includes an interactive notebook customised to be run through Google Colaboratory as well as helper scripts.
Model training and validation are tracked through [*weights & biases*](https://wandb.ai/site).

---

# 1. Overview

This repository includes:

- **`duneminds_original.ipynb`** — the main interactive notebook.
- **`model_1_directory_creation.py`** — helper script that creates the standard folder hierarchy.
- **`model_1_datadownload.py`** — helper script for the download of digital elevation models / optical satellite imagery.
- **`model_1_functions.py`** — helper script for various utilities.


The notebook uses **interactive dropdown menus and widgets**, so running it in **Google Colab** is recommended.

---

# 2. Recommendet Set-up: Google Colab


We recommend the upload of `duneminds_original.ipynb` and the three helper scripts to the same folder in your Google Drive. Google Colab should automatically be available upon opening the script in your browser. 
If the `.py` scripts are located in different folders, the paths in `duneminds_original.ipynb` need to be updated.


## Colab Forms
Google Colab uses so-called *Forms* to enable the creation of drop-down menus, text fields, sliders, and more. We are providing these interactive input options to make running the script more intuitive, particularly for users that have limited programming experience. It contains: 

- *sliders* for entering numeric values within predefined ranges
- *dropdown menus* for selecting from existing variable options
- *checkboxes* for simple yes/no (boolean) inputs
- *text boxes* for direct data entry with defined data types (e.g., string, integer, float)

These controls allow you to easily adjust parameters without modifying the code directly.
If the predefined options don’t match your use case, you can still edit the dropdown lists or enter your own values directly in the script - full flexibility remains available.
More information [here](https://colab.research.google.com/notebooks/forms.ipynb).


# 3. Script structure

**`duneminds_original.ipynb`** contains multiple sections with different functions that can be run in sequence or individually. 

## INTRO
The cells in this section **always have to be run** as they contain:
- installations and package imports
- the mounting of the google drive to access files
- the set-up of wandb for AI experiment tracking
- the definition of common variables and paths
- call to helper functions

### To Do:
In *import packages, define common paths & variables*, enter your `HOME_PATH` (on GoogleDrive). The `FUNCTIONS_SCRIPT_PATH` only needs to be entered if `model_1_functions.py` is not located in the same directory as `duneminds_original.ipynb`.
In *wandb set up* enter your wandb key.


## Directory Creation
This section creates the directory structure required for the following operations.

### To Do: 
Enter your `study_area`. The Kalahari Desert ("kalahari") and Simpson Desert ("simpson") are available through the drop-down menu. The naming of the study area is important for the directory structure in case of multiple study areas.

<img width="1394" height="172" alt="image" src="https://github.com/user-attachments/assets/426c2711-152b-4313-9cd5-8b596a42aed0" />



## Data Download
This section can be used to download Earth Engine datasets. It is customised for Copernicus DEM, ALOS DEM, and Sentinel-2 but can be easily extended to other Earth Engine data sets.
An Earth Engine project key is required. 
The dropdown menus and text boxes can be used to define the search parameters for the imagery (e.g. date, max cloudy pixels,...). 

## Data pre-processing
Contains a function to check if the target images are already pre-processed, pre-processing functions, and an execution cell for the pre-processing functions.
Pre-processing functions are only executed if the pre-processing check yields they are not yet pre-processed.
Pre-processing consists of a variety of checks (e.g. required tile size and band number) as well as normalisation.

## Training & Validation
Contains functions for:
- custom validation metrics
- functions for different U-Net model architectures
- functions for a tiered IoU metric
- functions for dataset preparation and augmentation

Two execution cells are (1) preparing the dataset and (2) executing model training.


## Visualising validation data


## Testing / Prediction





# 4. Data

Pre-processed training data can be obtained [here](https://drive.google.com/drive/folders/1-TrPQzy8tLkgg-vgebODLxou5t6dp9dN?usp=sharing).

## Folder structure:

```text
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


