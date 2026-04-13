# 🛒 E-Commerce Customer Behavior Analysis

A data analytics pipeline that segments customers and visualizes delivery hotspots using Python, Pandas, NumPy, Folium, and Matplotlib.

## 📋 Project Overview

An online retail company seeks to understand customer behavior trends to optimize their marketing and website experience. This project analyzes customer interactions to improve conversions and reduce cart abandonment rates.

## 🎯 Objective

To identify key patterns in customer behavior that influence purchase decisions and recommend strategies for enhancing the online shopping experience.

## 📊 Data Overview

A synthetic dataset of **200 samples** was generated to simulate customer activity on the e-commerce platform. The key variables include:

| Variable | Description |
|----------|-------------|
| `Customer_Id` | Unique customer identifier |
| `Session_Duration` | Time spent on the website (in seconds) |
| `Pages_Visited` | Number of pages viewed per session |
| `Cart_Additions` | Number of products added to the shopping cart |
| `Purchase_Made` | Whether a customer completed a purchase (Yes/No) |
| `Device_Type` | Mobile, Desktop, or Tablet |
| `Referral_Source` | Platform through which customers arrived (Google, Facebook, Direct, Email) |

## 🔍 Analysis Performed

1. **Purchase Segmentation** — Identify customers who made vs. did not make a purchase
2. **Cart Abandonment Detection** — List customers who added items to cart but did not purchase
3. **Device-wise Traffic Analysis** — Percentage breakdown of device types used
4. **Referral Source Distribution** — Analyze how customers arrive at the platform
5. **Geospatial Heatmap** — Interactive Folium map with color-coded order markers and revenue popups

## 🗺️ Interactive Map

The project generates an interactive HTML-based geospatial heatmap (`customer_distribution_map.html`) featuring:
- Color-coded circle markers by region (North → Blue, South → Green, East → Red, West → Purple)
- Revenue popups on click
- Marker clustering for dense areas
- Heatmap layer for delivery hotspot visualization

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Pandas** — Data manipulation and filtering
- **NumPy** — Synthetic data generation
- **Folium** — Interactive geospatial mapping
- **Matplotlib** — Data visualization

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Ecommerce-Customer-Behavior-Analysis.git
   cd Ecommerce-Customer-Behavior-Analysis
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy folium matplotlib
   ```

3. Run the analysis script:
   ```bash
   python ecommerce_analysis.py
   ```

4. Run the geospatial mapping script:
   ```bash
   python geospatial_heatmap.py
   ```

5. Open `customer_distribution_map.html` in your browser to view the interactive map.

## 📁 Project Structure

```
Ecommerce-Customer-Behavior-Analysis/
├── README.md
├── ecommerce_analysis.py        # Customer behavior analysis pipeline
├── geospatial_heatmap.py        # Folium-based geospatial visualization
├── ecommerce_sales_data.csv     # E-commerce sales dataset (for mapping)
└── customer_distribution_map.html  # Generated interactive map (output)
```

## 📈 Sample Output

### Device Type Distribution
```
Device Type    Percentage
Mobile         38.5%
Desktop        33.0%
Tablet         28.5%
```

### Cart Abandonment Rate
Customers who added items to cart but didn't purchase are flagged for targeted remarketing campaigns.
