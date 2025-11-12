# DUNEMINDS


DUNEMINDS is a notebook-based framework centered around a deep learning model that was developed to map dune crest lines using semantic segmentation. It includes all steps of the workflow from data access and pre-processing to model training and inference.
The repository includes an interactive notebook customised to be run through Google Colaboratory as well as helper `.py`scripts.
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
Note: Opening the Colab file through the **Open in Colab** button at the top of the **`duneminds_original.ipynb`** script in Github won't work as the script requires the helper scripts (see **1. Overview**).




## Colab Forms
Google Colab uses so-called *Forms* to enable the creation of drop-down menus, text fields, sliders, and more. We are providing these interactive input options to show what variables can be changed flexibly and make running the script more intuitive, particularly for users that have limited programming experience. It contains: 

- *sliders* for entering numeric values within predefined ranges
- *dropdown menus* for selecting from existing variable options
- *checkboxes* for simple yes/no (boolean) inputs
- *text boxes* for direct data entry with defined data types (e.g., string, integer, float)

These controls allow you to easily adjust parameters without modifying the code directly.
If the predefined options don’t match your use case, you can still edit the dropdown options, slider range, etc or enter your own values directly in the script - full flexibility remains available.
More information [here](https://colab.research.google.com/notebooks/forms.ipynb).

---

# 3. Script structure

**`duneminds_original.ipynb`** contains multiple sections with different functions that can be run in sequence or individually. 



## INTRO
The cells in this section **always have to be run** as they contain:
- installations and package imports
- the mounting of the google drive to access files
- the set-up of wandb for AI experiment tracking
- the definition of common variables and paths
- call to helper functions

### Note:
The Colab runtime has to be restarted once the first cell (**installations**) has been run. This is due to a workaround to make dependencies work that were used when the model was first developed. To restart the runtime, click the **Runtime** tab and choose **restart runtime**. 

### To Do:
In *set seed, mount GDrive, common paths, import modules from other scripts*, enter your `HOME_PATH` (on GoogleDrive). Enter your `SCRIPT_PATH` to the directory where `model_1_functions.py` and the other helper scripts are located.
In *wandb set up* enter your wandb key.



## Directory Creation
This section creates the directory structure required for the following operations.

### To Do: 
Enter your `study_area`. The Kalahari Desert ("kalahari") and Simpson Desert ("simpson") are available through the drop-down menu. The naming of the study area is important for the directory structure in case of multiple study areas.

<img width="1394" height="172" alt="image" src="https://github.com/user-attachments/assets/426c2711-152b-4313-9cd5-8b596a42aed0" />



## Data Download
This section can be used to download Google Earth Engine datasets. It is customised for Copernicus DEM, ALOS DEM, and Sentinel-2 but can be easily extended to other Earth Engine data sets.

### To Do - before running:
For data download via Google Earth Engine, your Earth Engine will need to be set up. Information on getting started and signing up for a non-commercial account [here](https://earthengine.google.com/noncommercial/). In the [Google Cloud Console](https://console.cloud.google.com/), you can create a new project or find the project key of your current one by clicking on **My Project**. You will need to enter your project key (e.g. `my-project-1111111111111`) into the first text box (`ee_project_key`).
Set `study_area` to match that of a directory you have created.
Further dropdown menus and text boxes can be used to define the search parameters for the imagery you would like to download: 
- `start_date` and `end_date` (temporal range of sensing date) - only needed for optical imagery!
- `cloudy_pixels` (maximum cloud coverage, in percent) - only needed for optical imagery!
- `R_band`, `G_band`, `B_band`, `NIR_band` (names of the red, green, blue, and NIR band - by default set to Sentinel-2, needs to be changed only if using other optical imagery such as Landsat) - only needed for optical imagery!
- `export_scale`(resolution of imagery, by default set to 10m)
- `export_folder_suffix` (makes sense to use a suffix that matches the dataset to download)
- `export_crs` (by default EPSG:3857)
- 'download_data' (data set to download - COP-DEM, ALOS, or Sentinel-2 are pre-set to choose from) - MOST IMPORTANT to set!

### To Do - after running:

You can check the state of the download on the [Earth Engine platform](https://code.earthengine.google.com/). The data will be automatically downloaded to your GoogleDrive at the path set up and specified during directory creation and in this cell's DOWNLOADS_FOLDER_PATH.

<img width="573" height="318" alt="image" src="https://github.com/user-attachments/assets/5f99588c-5b4a-441c-a855-608f5308c215" />



## Merging & clipping base images: Sentinel & DEM

This section enables the merging of multiple downloaded tiles - which will be relevant for large study areas such as the Kalahari. Afterwards, the mosaic of tiles is clipped to the study area's extent.

### To Do:
Ensure that `study_area` is set to the right location.
This section requires a shapefile called `{study_area}_shape.shp` in the directory specified during the creation of the directory structure (by default, it is `STUDY_AREA_SHAPES_FOLDER_PATH = os.path.join(HOME_PATH, study_area, "shapes")`
Set `merged_dataset` and `data_set` to the data set that you will be merging and clipping (e.g. dem - copdem. 
`src_nodata` is set to the no data value of the respective data set.



## Sense Check

This section is optional and can be run to visualise an extract of the merged and clipped dataset for a low-key sense check. This can either be done with a static sense check (i.e., displaying an image, first cell) or through an interactive folium map (second cell).



## Curvature, height, merge

This section can be used for the creation of secondary DEM data - a dune height data set (extracting local heights from the underlying topography), a curvature data set, and a smoothed curvature data set. Due to a limitation of the `richdem` library that is used in the calculation, curvature is processed in two chunks (northern and southern portion of the study area separately) and then merged and clipped.
The first cell provides one function containing the calculations for all three DEM derivatives; variables need to be set in the second cell along with the execution of the function. Merging and clipping will only be executed if there are no merged/clipped files existing in the specified folder.

### To Do:
Set `study_area` to the right variable.
Choose the base data set (`data_set`) for your DEM derivatives - this can either be COP-DEM or ALOS, depending on what you've downloaded before.
Choose the `derivative` that you'd like to produce: **curvature**, **smoothed curvature**, or **dune height**.
For smoothed curvature and dune height, you can select further parameters.
For smoothed curvature: `sigma_value_curv_smooth`.
For dune height: `sigma_value_dune_height`, `kernel_size_dune_height`, and most importantly the `height_approach` (recommended: top hat).



## Tiling

Both training and prediction (testing) of the model uses tiles extracted from the extensive raster data covering the entire study area. For training, it is advisable to use small tiles to keep the labelling effort low (or use the provided 96x96 pixel labelled tiles); for prediction/testing, it can make sense to split extensive study areas such as the Kalahari into multiple tiles for processing.
The section consists of three cells: 
- *create csv function* contains a function to produce a CSV file saving the placing of labels so the matching image tiles can be created;
- the *main tiling function*;
- a cell to determine variables and execute the functions

### To Do:
Set `study_area` to the right variable. 
Determine the base `data_set` you want to tile (note: for curvature, dune height, and smoothed curvature this is copdem!) and the `tile_type` (this is where you choose from curv, curv_smooth, sentinel, etc).
Choose whether you're tiling for training or testing (`train_test`) and what size you want your tiles to have (`tile_size`). Recommended is a tile size of 96 for training tiles, larger for test tiles.
Choose the `pixe_size` - recommended default is 10m to make use of the high Sentinel-2 resolution.
You can now select whether you'd like to create **specific tiles**, **random tiles**, or **all tiles**.
Specific tiles will create tiles in the same locations as tiles you've previously created and saved. Just set `img_to_csv_folder` to the folder from which you'd like to copy the tile locations; e.g. `train_pp/labels`. Make sure that `suffix` is set to the suffix of the files you'd like to copy from in case there are not only .tif files in the folder (e.g., .tif.aux.xml files that are created when opening .tif files in a GIS).
Random tiles will create the number of randomly distributed tiles across the study area that you've chosen through `tile_nr`.
All tiles will break the entire study area into tiles of the size you've selected.
You can choose a `prefix`for the tile images you're creating.


### Important:
If you've decided to not use the provided labels, you will have to manually create labels for your training tiles at this point.


## Data pre-processing
This section contains a function to check if the target images are already pre-processed, pre-processing functions, and an execution cell.
Pre-processing is only executed if the pre-processing check yields that the tiles are not yet pre-processed.
Pre-processing consists of a variety of checks (e.g. required tile size and band number) as well as normalisation.

### To Do:
Set `study_area` to the right variable. 
Determine what `tile_type` you'd like to check or pre-process - sentinel, dem, curv, curv_smooth, dune_height, or labels.
Specify the `tile_size` and `pixel_size` as well as the `band_number` you'd like to check. E.g. for the provided sentinel training tiles, this would be 96, 10, and 4.
It is important to choose the `nodata_value` that was determined previously - either manually or through libraries used for calculations. We used -99 for dem and curv; -9999 for curv_smooth, and 0 for all others.


## Training & Validation

This section contains cells with the following content:
- *custom metrics*: Functions to calculate custom model validation metrics
- *model functions*: Functions defining model architectures
- *tiered IoU functions*: Functions to calculate a validation metric developed during model development, the tiered IoU (t-IoU)
- *dataset preparation / augmentation functions*: Functions needed for the preparation of the training data set - e.g. matching and stacking training labels and images, train / vali split, etc. - and for data augmentation. Includes visual sense checks.
- *main training function*: Functions for model training, including the option for fine-tuning existing model weights or newly training a model
- *evaluation functions*: Functions for model evaluation/validation, including loss and accuracy curves and the calculation of a variety of metrics (iou, t-iou, false positives, true positives, false negatives, true negatives,...)

Two further cells are execution cells for (1) preparing the dataset and (2) running the model training.


## Visualising validation data


## Testing / Prediction



---

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


