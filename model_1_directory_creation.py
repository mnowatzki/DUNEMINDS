########## Maike Nowatzki, directory creation for model_1, April 2023 ##########


########## IMPORT FUNCTIONS ##########

from model_1_functions import *

########## CREATE FOLDER STRUCTURE ##########

def create_folder_structure(home_dir, study_area):
    
    # home directory
    home_dir = fun_check_create_folder(home_dir)

    # main study area folder
    home_dir_sa = fun_check_create_folder(os.path.join(home_dir, study_area))
    
    
    # shapefiles of study area
    path_shapes_sa = fun_check_create_folder(os.path.join(home_dir_sa, 'shapes'))
    
    
    # downloaded tiles of Sentinel and ALOS
    path_downloads = fun_check_create_folder(os.path.join(home_dir_sa, 'downloads'))
    path_sentinel_downloads = fun_check_create_folder(os.path.join(home_dir_sa, 'downloads/downloads_' + study_area + '_sentinel'))
    path_alos_downloads = fun_check_create_folder(os.path.join(home_dir_sa, 'downloads/downloads_' + study_area + '_alos'))
    path_copdem_downloads = fun_check_create_folder(os.path.join(home_dir_sa, 'downloads/downloads_' + study_area + '_copdem'))
    
    
    # model training files
    path_model_files = fun_check_create_folder(os.path.join(home_dir, 'model_files'))
    
    
    # model weight files
    path_model_weights = fun_check_create_folder(os.path.join(home_dir, 'weights'))
    
    
    # tiles 96 and 9600 (unprocessed)
    #path_tiles96 = fun_check_create_folder(os.path.join(home_dir_sa, 'tiles_96'))
    #path_train_labels_raw = fun_check_create_folder(os.path.join(path_tiles96, 'labels'))
    #path_train_dem_raw = fun_check_create_folder(os.path.join(path_tiles96, 'dem'))
    #path_train_curv_raw = fun_check_create_folder(os.path.join(path_tiles96, 'curv'))
    #path_train_dune_height_raw = fun_check_create_folder(os.path.join(path_tiles96, 'dune_height'))
    #path_train_sentinel_raw = fun_check_create_folder(os.path.join(path_tiles96, 'sentinel'))
    #path_train_curv_smooth_raw = fun_check_create_folder(os.path.join(path_tiles96, 'curv_smooth'))
    
    #path_tiles9600_unlabelled = fun_check_create_folder(os.path.join(home_dir_sa, 'tiles_9600'))
    #path_test_labels_raw_9600 = fun_check_create_folder(os.path.join(path_tiles9600_unlabelled, 'labels'))
    #path_test_dem_raw_9600 = fun_check_create_folder(os.path.join(path_tiles9600_unlabelled, 'dem'))
    #path_test_curv_raw_9600 = fun_check_create_folder(os.path.join(path_tiles9600_unlabelled, 'curv'))
    #path_test_dune_height_raw_9600 = fun_check_create_folder(os.path.join(path_tiles9600_unlabelled, 'dune_height'))
    #path_test_sentinel_raw_9600 = fun_check_create_folder(os.path.join(path_tiles9600_unlabelled, 'sentinel'))
    #path_test_curv_smooth_raw_9600 = fun_check_create_folder(os.path.join(path_tiles9600_unlabelled, 'curv_smooth'))
    
    #path_tiles96_unlabelled = fun_check_create_folder(os.path.join(home_dir_sa, 'tiles_9600'))
    #path_test_labels_raw_96 = fun_check_create_folder(os.path.join(path_tiles96_unlabelled, 'labels'))
    #path_test_dem_raw_96 = fun_check_create_folder(os.path.join(path_tiles96_unlabelled, 'dem'))
    #path_test_curv_raw_96 = fun_check_create_folder(os.path.join(path_tiles96_unlabelled, 'curv'))
    #path_test_dune_height_raw_96 = fun_check_create_folder(os.path.join(path_tiles96_unlabelled, 'dune_height'))
    #path_test_sentinel_raw_96 = fun_check_create_folder(os.path.join(path_tiles96_unlabelled, 'sentinel'))
    #path_test_curv_smooth_raw_96 = fun_check_create_folder(os.path.join(path_tiles96_unlabelled, 'curv_smooth'))
    
    
    # merged images
    path_img_merged = fun_check_create_folder(os.path.join(home_dir_sa, 'img_merged'))
    path_dem_merged = fun_check_create_folder(os.path.join(path_img_merged, 'dem'))
    path_curv_merged = fun_check_create_folder(os.path.join(path_img_merged, 'curv'))
    path_dune_height_merged = fun_check_create_folder(os.path.join(path_img_merged, 'dune_height'))
    path_sentinel_merged = fun_check_create_folder(os.path.join(path_img_merged, 'sentinel'))
    path_curv_smooth_merged = fun_check_create_folder(os.path.join(path_img_merged, 'curv_smooth'))
    
    
    ## pre-processed data training & test
    path_tiles_pp = fun_check_create_folder(os.path.join(home_dir_sa, 'pp_data'))
    
    path_train_pp = fun_check_create_folder(os.path.join(path_tiles_pp, 'train_pp'))
    path_train_labels_pp = fun_check_create_folder(os.path.join(path_train_pp, 'labels'))
    path_train_dem_pp = fun_check_create_folder(os.path.join(path_train_pp, 'dem'))
    path_train_curv_pp = fun_check_create_folder(os.path.join(path_train_pp, 'curv'))
    path_train_dune_height_pp = fun_check_create_folder(os.path.join(path_train_pp, 'dune_height'))
    path_train_sentinel_pp = fun_check_create_folder(os.path.join(path_train_pp, 'sentinel'))
    path_train_curv_smooth_pp = fun_check_create_folder(os.path.join(path_train_pp, 'curv_smooth'))
    
    path_test_pp = fun_check_create_folder(os.path.join(path_tiles_pp, 'test_pp'))
    path_test_tiles96_pp = fun_check_create_folder(os.path.join(path_test_pp, 'tiles_96'))
    path_test_tiles9600_pp = fun_check_create_folder(os.path.join(path_test_pp, 'tiles_9600'))
    path_test_tiles96_labels_pp = fun_check_create_folder(os.path.join(path_test_tiles96_pp, 'labels'))
    path_test_tiles9600_labels_pp = fun_check_create_folder(os.path.join(path_test_tiles9600_pp, 'labels'))
    path_test_tiles96_sentinel_pp = fun_check_create_folder(os.path.join(path_test_tiles96_pp, 'sentinel'))
    path_test_tiles9600_sentinel_pp = fun_check_create_folder(os.path.join(path_test_tiles9600_pp, 'sentinel'))
    path_test_tiles96_dem_pp = fun_check_create_folder(os.path.join(path_test_tiles96_pp, 'dem'))
    path_test_tiles9600_dem_pp = fun_check_create_folder(os.path.join(path_test_tiles9600_pp, 'dem'))
    #path_test_labels_pp = fun_check_create_folder(os.path.join(path_test_pp, 'labels'))
    #path_test_dem_pp = fun_check_create_folder(os.path.join(path_test_pp, 'dem'))
    #path_test_curv_pp = fun_check_create_folder(os.path.join(path_test_pp, 'curv'))
    #path_test_dune_height_pp = fun_check_create_folder(os.path.join(path_test_pp, 'dune_height'))
    #path_test_sentinel_pp = fun_check_create_folder(os.path.join(path_test_pp, 'sentinel'))
    #path_test_curv_smooth_pp = fun_check_create_folder(os.path.join(path_test_pp, 'curv_smooth'))
    
    
    ## model results
    path_results = fun_check_create_folder(os.path.join(home_dir, 'results'))
    
    
    ## diverse csv
    path_csv = fun_check_create_folder(os.path.join(home_dir, 'csv'))
    
    
    ## figures
    path_figures = fun_check_create_folder(os.path.join(home_dir, 'figures'))
    path_figures_sc = fun_check_create_folder(os.path.join(path_figures, 'sanity_check'))
    path_figures_loss = fun_check_create_folder(os.path.join(path_figures, 'loss'))
    path_figues_accuracy = fun_check_create_folder(os.path.join(path_figures, 'accuracy'))
    
    
    ## configs
    path_configs = fun_check_create_folder(os.path.join(home_dir, 'configs'))



