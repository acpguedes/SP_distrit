import urllib
import geopandas as gpd 

class SpPolygon:
    
    def __init__(self):
        self.dataURL = "http://datageo.ambiente.sp.gov.br/geoserver/datageo/DISTRITO_MUNICIPAL_SP_SMDU/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=DISTRITO_MUNICIPAL_SP_SMDU"
        
    def get_data(self, dest = './spdist.zip'):
        urllib.request.urlretrieve(self.dataURL, dest)
        
    def load_distrites(self, from_file = './spdist.zip'):
        return gpd.read_file(from_file)