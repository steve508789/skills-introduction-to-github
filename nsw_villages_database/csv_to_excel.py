#!/usr/bin/env python3
"""
CSV to Excel Converter for NSW Small Villages
Converts the small villages CSV data to Excel format without external dependencies.
"""

import csv
import json
from datetime import datetime

def create_excel_like_output():
    """Create Excel-compatible files from CSV data"""
    
    # Read small villages CSV
    villages = []
    with open('nsw_small_villages.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            villages.append(row)
    
    # Create a tab-delimited file that Excel can open
    with open('nsw_small_villages.xlsx.txt', 'w', encoding='utf-8') as file:
        # Write header
        file.write("Village Name\tPopulation\tLocal Government Area\tRegion\tLatitude\tLongitude\tDesignation\n")
        
        # Write data
        for village in villages:
            file.write(f"{village['name']}\t{village['population']}\t{village['lga']}\t{village['region']}\t{village['latitude']}\t{village['longitude']}\t{village['designation']}\n")
    
    # Create HTML table that can be opened in Excel
    with open('nsw_small_villages.html', 'w', encoding='utf-8') as file:
        file.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>NSW Small Villages (500-999 Population)</title>
    <style>
        table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; font-weight: bold; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        .number { text-align: right; }
        .title { color: #333; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1 class="title">NSW Small Villages Database (500-999 Population)</h1>
    <p><strong>Total Villages:</strong> """ + str(len(villages)) + """</p>
    <p><strong>Generated:</strong> """ + datetime.now().strftime("%B %d, %Y") + """</p>
    <table>
        <thead>
            <tr>
                <th>Rank</th>
                <th>Village Name</th>
                <th>Population</th>
                <th>Local Government Area</th>
                <th>Region</th>
                <th>Latitude</th>
                <th>Longitude</th>
                <th>Designation</th>
            </tr>
        </thead>
        <tbody>
""")
        
        # Sort by population (descending) and add rank
        sorted_villages = sorted(villages, key=lambda x: int(x['population']), reverse=True)
        
        for rank, village in enumerate(sorted_villages, 1):
            file.write(f"""            <tr>
                <td class="number">{rank}</td>
                <td><strong>{village['name']}</strong></td>
                <td class="number">{village['population']}</td>
                <td>{village['lga']}</td>
                <td>{village['region']}</td>
                <td class="number">{village['latitude']}</td>
                <td class="number">{village['longitude']}</td>
                <td>{village['designation']}</td>
            </tr>
""")
        
        file.write("""        </tbody>
    </table>
    
    <h2>Summary Statistics</h2>
    <ul>
        <li><strong>Total Villages:</strong> """ + str(len(villages)) + """</li>
        <li><strong>Total Population:</strong> """ + f"{sum(int(v['population']) for v in villages):,}" + """</li>
        <li><strong>Average Population:</strong> """ + f"{sum(int(v['population']) for v in villages) // len(villages):,}" + """</li>
        <li><strong>Largest Village:</strong> """ + sorted_villages[0]['name'] + f" ({sorted_villages[0]['population']} people)" + """</li>
        <li><strong>Smallest Village:</strong> """ + sorted_villages[-1]['name'] + f" ({sorted_villages[-1]['population']} people)" + """</li>
    </ul>
    
    <h2>Regional Distribution</h2>
    <table style="width: 50%;">
        <thead>
            <tr><th>Region</th><th>Villages</th><th>Total Population</th></tr>
        </thead>
        <tbody>
""")
        
        # Calculate regional stats
        regions = {}
        for village in villages:
            region = village['region']
            if region not in regions:
                regions[region] = {'count': 0, 'population': 0}
            regions[region]['count'] += 1
            regions[region]['population'] += int(village['population'])
        
        for region, stats in sorted(regions.items()):
            file.write(f"""            <tr>
                <td>{region}</td>
                <td class="number">{stats['count']}</td>
                <td class="number">{stats['population']:,}</td>
            </tr>
""")
        
        file.write("""        </tbody>
    </table>
    
    <p><em>Source: NSW Geographical Names Register & 2021 Census Data</em></p>
    <p><em>This file can be opened directly in Microsoft Excel</em></p>
</body>
</html>""")
    
    # Create a properly formatted CSV for Excel import
    with open('nsw_small_villages_excel.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Rank', 'Village Name', 'Population', 'Local Government Area', 'Region', 'Latitude', 'Longitude', 'Designation'])
        
        # Write data with ranking
        sorted_villages = sorted(villages, key=lambda x: int(x['population']), reverse=True)
        for rank, village in enumerate(sorted_villages, 1):
            writer.writerow([
                rank,
                village['name'],
                int(village['population']),
                village['lga'],
                village['region'],
                float(village['latitude']),
                float(village['longitude']),
                village['designation']
            ])

def create_xml_spreadsheet():
    """Create XML spreadsheet format that Excel can open"""
    
    # Read small villages CSV
    villages = []
    with open('nsw_small_villages.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            villages.append(row)
    
    sorted_villages = sorted(villages, key=lambda x: int(x['population']), reverse=True)
    
    with open('nsw_small_villages.xml', 'w', encoding='utf-8') as file:
        file.write('''<?xml version="1.0"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:x="urn:schemas-microsoft-com:office:excel"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:html="http://www.w3.org/TR/REC-html40">
 <DocumentProperties xmlns="urn:schemas-microsoft-com:office:office">
  <Title>NSW Small Villages Database</Title>
  <Author>NSW Villages Database</Author>
  <Created>''' + datetime.now().isoformat() + '''</Created>
 </DocumentProperties>
 <Worksheet ss:Name="Small Villages (500-999)">
  <Table>
   <Row>
    <Cell><Data ss:Type="String">Rank</Data></Cell>
    <Cell><Data ss:Type="String">Village Name</Data></Cell>
    <Cell><Data ss:Type="String">Population</Data></Cell>
    <Cell><Data ss:Type="String">Local Government Area</Data></Cell>
    <Cell><Data ss:Type="String">Region</Data></Cell>
    <Cell><Data ss:Type="String">Latitude</Data></Cell>
    <Cell><Data ss:Type="String">Longitude</Data></Cell>
    <Cell><Data ss:Type="String">Designation</Data></Cell>
   </Row>
''')
        
        for rank, village in enumerate(sorted_villages, 1):
            file.write(f'''   <Row>
    <Cell><Data ss:Type="Number">{rank}</Data></Cell>
    <Cell><Data ss:Type="String">{village['name']}</Data></Cell>
    <Cell><Data ss:Type="Number">{village['population']}</Data></Cell>
    <Cell><Data ss:Type="String">{village['lga']}</Data></Cell>
    <Cell><Data ss:Type="String">{village['region']}</Data></Cell>
    <Cell><Data ss:Type="Number">{village['latitude']}</Data></Cell>
    <Cell><Data ss:Type="Number">{village['longitude']}</Data></Cell>
    <Cell><Data ss:Type="String">{village['designation']}</Data></Cell>
   </Row>
''')
        
        file.write('''  </Table>
 </Worksheet>
</Workbook>''')

if __name__ == "__main__":
    print("Converting NSW Small Villages to Excel-compatible formats...")
    print("=" * 60)
    
    create_excel_like_output()
    create_xml_spreadsheet()
    
    print("✅ Excel-compatible files created:")
    print("  1. nsw_small_villages_excel.csv - Enhanced CSV with UTF-8 BOM for Excel")
    print("  2. nsw_small_villages.html - HTML table (opens in Excel)")
    print("  3. nsw_small_villages.xml - XML Spreadsheet format")
    print("  4. nsw_small_villages.xlsx.txt - Tab-delimited for Excel import")
    
    print("\nHow to open in Excel:")
    print("  • Double-click the .html file and Excel will open it")
    print("  • Open Excel and import the _excel.csv file")
    print("  • Use File > Open in Excel to open the .xml file")
    print("  • Import the .txt file using Excel's Text Import Wizard")
    
    # Show preview
    with open('nsw_small_villages.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        villages = list(reader)
    
    print(f"\n📊 Small Villages Summary:")
    print(f"  Total Villages: {len(villages)}")
    print(f"  Population Range: {min(int(v['population']) for v in villages)} - {max(int(v['population']) for v in villages)} people")
    print(f"  Total Population: {sum(int(v['population']) for v in villages):,} people")
    
    print("\nConversion completed successfully! 🎉")