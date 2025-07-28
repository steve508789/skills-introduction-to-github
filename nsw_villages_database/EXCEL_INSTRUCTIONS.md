# How to Open NSW Small Villages Data in Excel

## 📊 Available Excel-Compatible Files

I've created **4 different Excel-compatible formats** for the NSW Small Villages data (500-999 population):

1. **`nsw_small_villages_excel.csv`** - Enhanced CSV with UTF-8 encoding
2. **`nsw_small_villages.html`** - HTML table (opens directly in Excel)
3. **`nsw_small_villages.xml`** - XML Spreadsheet format
4. **`nsw_small_villages.xlsx.txt`** - Tab-delimited text file

## 🚀 Quick Start (Easiest Methods)

### Method 1: HTML File (Recommended - No Import Needed!)
1. **Double-click** `nsw_small_villages.html`
2. Your default browser will open it
3. **Right-click** → **"Open with Microsoft Excel"** OR
4. **Copy the table** from browser and **paste into Excel**

### Method 2: Enhanced CSV
1. **Open Microsoft Excel**
2. **File** → **Open** → Select `nsw_small_villages_excel.csv`
3. Excel will automatically format it correctly!

## 📋 Data Structure

Your Excel sheet will contain **34 small villages** with these columns:

| Rank | Village Name | Population | Local Government Area | Region | Latitude | Longitude | Designation |
|------|-------------|------------|----------------------|---------|----------|-----------|-------------|
| 1 | Crescent Head | 978 | Kempsey | North Coast | -31.1833 | 152.9667 | Locality |
| 2 | Berrigan | 957 | Berrigan | Murray | -35.6667 | 145.8 | Locality |
| 3 | Bowraville | 941 | Nambucca Valley | North Coast | -30.65 | 152.85 | Locality |

## 📈 What You'll Get in Excel

✅ **34 villages** with populations between 500-999 people  
✅ **Ranked by population** (largest first)  
✅ **Geographic coordinates** for mapping  
✅ **Regional classification** for analysis  
✅ **Properly formatted numbers** for calculations  
✅ **Summary statistics** (in HTML version)  

## 🗺️ Top 10 Small Villages (500-999 Population)

1. **Crescent Head** - 978 people (North Coast)
2. **Berrigan** - 957 people (Murray)
3. **Bowraville** - 941 people (North Coast)
4. **Beechwood** - 914 people (North Coast)
5. **East Jindabyne** - 907 people (Snowy Mountains)
6. **Boggabri** - 885 people (New England)
7. **Clarence Town** - 878 people (Hunter)
8. **Darlington Point** - 868 people (Riverina)
9. **Adelong** - 856 people (Riverina)
10. **Brandy Hill** - 852 people (Hunter)

## 🔧 Advanced Import Options

### Method 3: XML Spreadsheet (Full Excel Features)
1. **Open Excel**
2. **File** → **Open** 
3. Select `nsw_small_villages.xml`
4. Excel will recognize it as a native spreadsheet

### Method 4: Text Import Wizard
1. **Open Excel**
2. **Data** → **Get Data** → **From File** → **From Text/CSV**
3. Select `nsw_small_villages.xlsx.txt`
4. Choose **Tab** as delimiter
5. Click **Load**

## 💡 Excel Tips

### For Analysis:
- **Sort by Region**: Select data → Data → Sort → Choose "Region"
- **Filter by Population**: Use AutoFilter to show specific population ranges
- **Create Charts**: Select population data → Insert → Charts
- **Calculate Totals**: Use SUM() function on population column

### For Mapping:
- Use the **Latitude** and **Longitude** columns with Excel's Map charts
- Insert → Charts → Maps → Filled Map

## 📊 Summary Statistics

- **Total Villages**: 34
- **Population Range**: 500 - 978 people  
- **Total Population**: 24,163 people
- **Average Population**: 711 people per village
- **Most Common Region**: North Coast (7 villages)

## 🌟 Features Included

✅ **Ranking system** (1-34)  
✅ **Clean, formatted data** ready for analysis  
✅ **Regional breakdown** for geographic studies  
✅ **Coordinates** for GIS/mapping applications  
✅ **Multiple format options** for compatibility  

## 🔍 Quick Excel Functions You Can Use

```excel
=SUM(C:C)          // Total population
=AVERAGE(C:C)      // Average population  
=MAX(C:C)          // Largest village population
=MIN(C:C)          // Smallest village population
=COUNTIF(E:E,"North Coast")  // Count villages by region
```

## 📞 Need Help?

If you have any issues opening the files:
1. Try the **HTML method** first (most compatible)
2. Ensure you have **Microsoft Excel 2010 or newer**
3. Check that files aren't blocked by your security settings

---
*Generated from NSW Geographical Names Register & 2021 Census Data*