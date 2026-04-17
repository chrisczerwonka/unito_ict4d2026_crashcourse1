import openpyxl
import json
from datetime import datetime

def convert_excel_to_geojson(excel_file, geojson_file):
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active
    
    # Get headers
    headers = [cell.value for cell in sheet[1]]
    
    features = []
    
    # Iterate through rows starting from the second one
    for row in sheet.iter_rows(min_row=2, values_only=True):
        properties = {}
        lon = None
        lat = None
        
        for i, value in enumerate(row):
            header = headers[i]
            
            # Handle dates
            if isinstance(value, datetime):
                value = value.strftime('%Y-%m-%d')
            
            if header == 'long':
                lon = value
            elif header == 'lat':
                lat = value
            else:
                properties[header] = value
        
        # Only add features that have coordinates
        if lon is not None and lat is not None:
            try:
                lon = float(lon)
                lat = float(lat)
                
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat]
                    },
                    "properties": properties
                }
                features.append(feature)
            except (ValueError, TypeError):
                # Skip rows with invalid coordinates
                continue
                
    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }
    
    with open(geojson_file, 'w') as f:
        json.dump(geojson_data, f, indent=2)

if __name__ == "__main__":
    convert_excel_to_geojson('../data/flood_data.xlsx', '../data/flood_data.geojson')
