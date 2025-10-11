# Script to download R, G, B, NIR Sentinel-2 data or DEM (ALOS & COPDEM)

########## IMPORT FUNCTIONS ##########

from model_1_functions import *

########## DATA DOWNLOAD FUNCTION ##########

def download_data_ee(path_shapes_sa,
                    study_area,
                    start_date,
                    end_date,
                    cloudy_pixels,
                    R_band,
                    G_band,
                    B_band,
                    NIR_band,
                    export_file_prefix,
                    export_scale,
                    export_folder,
                    export_crs,
                    download_data):

    ### import shapefile of study area and turn into EE geometry data type 
    
    # check for study area polygon folder / file 
    stop_var = fun_check_folder_file(path_shapes_sa, study_area + '_shape.shp')
    
    ## check if shapefile is in right projection and transform to Earth Engine geometry file
    if stop_var == 1:
    
        shapefile_sa =  gpd.read_file(path_shapes_sa + "/" + study_area + "_shape.shp") # shapefile_sa = study area shapefile
        #print(shapefile_sa)
    
        # check projection - is study area shapefile in geographic coordinate system ESPG 4326
        print("old projection: " , shapefile_sa.crs)
        
        if shapefile_sa.crs == "*4326": 
            print("Already is in the right projection.")
            
        else:
            
            # reproject to WGS 84 geographic coordinate system
            shapefile_sa = shapefile_sa.to_crs("EPSG:4326")     
            print("new projection: " , shapefile_sa.crs)
    
        # read coordinates of points in shapefile polygon as list
        g = [i for i in shapefile_sa.geometry]
        x,y = g[0].exterior.coords.xy
        coords_sa = np.dstack((x,y)).tolist() # coords_sa = coordinates of study area polygon points
    
        print(coords_sa)
    
        geometry_sa = ee.Geometry.Polygon(coords_sa)    
        
    elif stop_var == 0:
        sys.exit("STOP. No study area file existing.")
        
    else:
        sys.exit("STOP. More than one study area shapefile existing.")
    
    
    if download_data == 'Sentinel-2': 
    
        ### Get Sentinel-2 images of study area
        # Sentinel-2
        # sensing date range
        # how many cloudy pixels are allowed?
        # sorting done by cloudy pixel percentage, false = descending
    
        s2_img = ee.ImageCollection('COPERNICUS/S2_SR')\
        .filterBounds(geometry_sa)\
        .filterDate(start_date, end_date)\
        .filterMetadata('CLOUDY_PIXEL_PERCENTAGE', 'less_than', cloudy_pixels)\
        .sort('CLOUDY_PIXEL_PERCENTAGE', False)\
    
        # merging images in image collection - if overlapping, the topmost is used (cf. .sort for sorting)
        s2_img = s2_img.mosaic()
    
        # select bands to use
        s2_img_RGBNIR = s2_img.select(R_band, G_band, B_band, NIR_band)
    
    
        ### Download final Sentinel-2 imagery to google Drive
    
        task = ee.batch.Export.image.toDrive(
            image=s2_img_RGBNIR,
            description=export_file_prefix,
            fileFormat='GeoTiff',
            region=geometry_sa,
            scale = export_scale, # one pixel = 10mx10m
            folder = export_folder,
            crs = export_crs, #change to Mercator based coordinate system 
            maxPixels=100000000000 # max number of pixels that can be downloaded - increase if Earth Engine is throwing error
        )
    
        task.start()
    
    
    
    if download_data == 'ALOS': 
    
        dem_img = ee.ImageCollection("JAXA/ALOS/AW3D30/V3_2")\
        .filterBounds(geometry_sa)\
        
        # merging images in image collection - if overlapping, the topmost is used (cf. .sort for sorting)
        dem_img = dem_img.mosaic()
    
        # select bands to use
        dem_img = dem_img.select('DSM')
    
    
        ### Download final ALOS imagery to google Drive 
    
        task = ee.batch.Export.image.toDrive(
            image=dem_img,
            description=export_file_prefix,
            fileFormat='GeoTiff',
            region=geometry_sa,
            scale = 10, # one pixel = 10mx10m
            folder = export_folder,
            crs = 'EPSG:3857', #change to Mercator based coordinate system 
            maxPixels=100000000000 # max number of pixels that can be downloaded - increase if Earth Engine is throwing error
        )
    
        task.start()
    
    
    
    
    
    if download_data == 'COPDEM': 
    
        dem_img = ee.ImageCollection("COPERNICUS/DEM/GLO30")\
        .filterBounds(geometry_sa)\
        
        # merging images in image collection - if overlapping, the topmost is used (cf. .sort for sorting)
        dem_img = dem_img.mosaic()
    
        # select bands to use
        dem_img = dem_img.select('DEM')
    
    
        ### Download final COPDEM imagery to google Drive
    
        task = ee.batch.Export.image.toDrive(
            image=dem_img,
            description=export_file_prefix,
            fileFormat='GeoTiff',
            region=geometry_sa,
            scale = 10, # one pixel = 10mx10m
            folder = export_folder,
            crs = 'EPSG:3857', #change to Mercator based coordinate system 
            maxPixels=100000000000 # max number of pixels that can be downloaded - increase if Earth Engine is throwing error
        )
    
        task.start()



