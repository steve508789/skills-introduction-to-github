# NSW Villages Database

A comprehensive database of villages in New South Wales, Australia, classified by population order.

## Overview

This database contains detailed information about **153 villages** across NSW, compiled from official NSW Geographical Names Register and Census data. Villages are classified into four population categories and include geographic coordinates, local government areas (LGA), and regional classifications.

## Database Summary

- **Total Villages**: 153
- **Total Population**: 262,952
- **Average Population**: 1,718 people per village
- **Data Source**: NSW Geographical Names Register & 2021 Census Data
- **Last Updated**: July 28, 2025

## Population Classification

### Large Villages (5000+ population) - 11 villages
Villages with significant population centers that serve as regional hubs.

**Top 5 Largest Villages:**
1. **Armidale** - 21,312 (New England)
2. **Ballina** - 18,532 (Northern Rivers)
3. **Batemans Bay** - 12,263 (South Coast)
4. **Byron Bay** - 10,538 (Northern Rivers)
5. **Casino** - 9,968 (Northern Rivers)

### Medium Villages (1000-4999 population) - 53 villages
Established communities with good local services and amenities.

### Small Villages (500-999 population) - 34 villages
Smaller communities often with basic services and strong local character.

### Very Small Villages (<500 population) - 55 villages
Rural communities and hamlets, often with historic significance.

## Regional Distribution

| Region | Number of Villages |
|--------|-------------------|
| Northern Rivers | 23 |
| North Coast | 21 |
| South Coast | 19 |
| New England | 14 |
| Central West | 11 |
| Riverina | 11 |
| Hunter | 10 |
| Capital Country | 8 |
| Snowy Mountains | 8 |
| Southern Highlands | 6 |
| Macarthur | 5 |
| Murray | 5 |
| Living Outback | 5 |
| Sydney | 4 |
| Blue Mountains | 2 |
| Central Coast | 1 |

## Files Description

### CSV Files
- **`nsw_villages_all.csv`** - Complete database with all 153 villages sorted by population (largest first)
- **`nsw_large_villages.csv`** - 11 villages with 5000+ population
- **`nsw_medium_villages.csv`** - 53 villages with 1000-4999 population
- **`nsw_small_villages.csv`** - 34 villages with 500-999 population
- **`nsw_very_small_villages.csv`** - 55 villages with <500 population

### Database Files
- **`nsw_villages.db`** - SQLite database for programmatic access
- **`nsw_villages_database.json`** - Complete JSON database with metadata

### Data Fields

Each village record includes:
- **name** - Official village name
- **population** - 2021 Census population figure
- **lga** - Local Government Area
- **region** - NSW geographic region
- **latitude** - Geographic coordinate (GDA94)
- **longitude** - Geographic coordinate (GDA94)
- **designation** - Official classification (Urban Center/Locality)
- **population_category** - Size classification

## Usage Examples

### Python SQLite Query
```python
import sqlite3

conn = sqlite3.connect('nsw_villages.db')
cursor = conn.cursor()

# Get all large villages
cursor.execute("SELECT name, population, region FROM villages WHERE population >= 5000 ORDER BY population DESC")
large_villages = cursor.fetchall()

for village in large_villages:
    print(f"{village[0]}: {village[1]} people ({village[2]})")
```

### CSV Analysis
```python
import pandas as pd

# Load all villages
df = pd.read_csv('nsw_villages_all.csv')

# Regional analysis
regional_stats = df.groupby('region').agg({
    'population': ['count', 'sum', 'mean'],
    'name': 'count'
}).round(0)

print(regional_stats)
```

### JSON Processing
```python
import json

with open('nsw_villages_database.json', 'r') as f:
    data = json.load(f)

# Get metadata
print(f"Database contains {data['metadata']['total_villages']} villages")
print(f"Source: {data['metadata']['source']}")

# Access villages by category
large_villages = [v for v in data['villages'] if v['population'] >= 5000]
```

## Geographic Coverage

The database covers villages across all major NSW regions:

- **Coastal**: From the Queensland border (Tweed) to the Victorian border (Eden)
- **Inland**: From the western slopes to the far west outback communities
- **Mountains**: Blue Mountains, Snowy Mountains, and New England tablelands
- **Valleys**: Hunter Valley, Riverina, and various river valleys

## Data Quality

- Population figures from 2021 Australian Census
- Coordinates verified against NSW Geographical Names Register
- LGA boundaries current as of 2025
- Excludes suburbs of major cities (Sydney, Newcastle, Wollongong)
- Focuses on standalone village communities

## License

This database is released under **Creative Commons Attribution 4.0 International License**.

Original data sources:
- NSW Geographical Names Board © State of New South Wales
- Australian Bureau of Statistics Census 2021

## Applications

This database is useful for:
- Regional planning and development
- Tourism and travel applications
- Demographic research
- Geographic information systems (GIS)
- Educational projects
- Population studies
- Infrastructure planning

## Updates

The database will be updated as new Census data becomes available and as village boundaries or classifications change through the NSW Geographical Names Board.

## Contact

For questions about this database or to report errors, please refer to the official NSW Geographical Names Board: https://www.gnb.nsw.gov.au/

---

*Generated on July 28, 2025*