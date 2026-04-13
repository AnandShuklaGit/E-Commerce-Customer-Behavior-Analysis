"""
E-Commerce Geospatial Heatmap Visualization
=============================================
Builds an interactive geospatial heatmap with Folium — color-coded order
markers with revenue popups, exported as a shareable HTML report.

Uses the e-commerce sales dataset to plot customer order locations on a
Delhi NCR map with:
  - Circle markers color-coded by region
  - Revenue popups on click
  - Marker clustering for dense areas
  - Heatmap layer for delivery hotspot visualization

Tech Stack: Python, Pandas, NumPy, Folium
"""

import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap, MarkerCluster

# ─────────────────────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────────────────────
df = pd.read_csv("ecommerce_sales_data.csv")

print(f"Loaded {len(df)} records from ecommerce_sales_data.csv")
print(f"Columns: {list(df.columns)}")

# ─────────────────────────────────────────────────────────────
# 2. GENERATE SYNTHETIC COORDINATES (Delhi NCR Region)
# ─────────────────────────────────────────────────────────────
np.random.seed(42)

# Delhi NCR bounding box (approx.)
lat_center, lon_center = 28.6139, 77.2090
lat_range, lon_range = 0.20, 0.25

df["Latitude"] = np.round(
    lat_center + np.random.uniform(-lat_range, lat_range, len(df)), 6
)
df["Longitude"] = np.round(
    lon_center + np.random.uniform(-lon_range, lon_range, len(df)), 6
)

# ─────────────────────────────────────────────────────────────
# 3. COLOR MAPPING BY REGION
# ─────────────────────────────────────────────────────────────
region_colors = {
    "North": "blue",
    "South": "green",
    "East": "red",
    "West": "purple",
}

# ─────────────────────────────────────────────────────────────
# 4. CREATE FOLIUM MAP
# ─────────────────────────────────────────────────────────────
center_lat = df["Latitude"].mean()
center_lon = df["Longitude"].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=11)

# ─────────────────────────────────────────────────────────────
# 5. ADD MARKER CLUSTER WITH COLOR-CODED MARKERS
# ─────────────────────────────────────────────────────────────
marker_cluster = MarkerCluster().add_to(m)

for _, row in df.iterrows():
    color = region_colors.get(row["Region"], "gray")

    # Scale radius based on revenue (min 3, max 15)
    radius = max(3, min(15, row["Revenue"] / 100))

    # Create popup with order details
    popup_html = (
        f"<b>Order ID:</b> {row['Order_ID']}<br>"
        f"<b>Product:</b> {row['Product_Name']}<br>"
        f"<b>Region:</b> {row['Region']}<br>"
        f"<b>Revenue:</b> ${row['Revenue']:.2f}<br>"
        f"<b>Qty Sold:</b> {row['Quantity_Sold']}"
    )

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=radius,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=folium.Popup(popup_html, max_width=250),
    ).add_to(marker_cluster)

# ─────────────────────────────────────────────────────────────
# 6. ADD HEATMAP LAYER
# ─────────────────────────────────────────────────────────────
heat_data = df[["Latitude", "Longitude", "Revenue"]].values.tolist()
HeatMap(heat_data, radius=15, blur=10, max_zoom=13).add_to(m)

# ─────────────────────────────────────────────────────────────
# 7. ADD LEGEND
# ─────────────────────────────────────────────────────────────
legend_html = """
<div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000;
            background-color: white; padding: 10px; border: 2px solid grey;
            border-radius: 5px; font-size: 14px;">
    <b>Region Legend</b><br>
    <i style="background: blue; width: 12px; height: 12px; display: inline-block;
       border-radius: 50%; margin-right: 5px;"></i> North<br>
    <i style="background: green; width: 12px; height: 12px; display: inline-block;
       border-radius: 50%; margin-right: 5px;"></i> South<br>
    <i style="background: red; width: 12px; height: 12px; display: inline-block;
       border-radius: 50%; margin-right: 5px;"></i> East<br>
    <i style="background: purple; width: 12px; height: 12px; display: inline-block;
       border-radius: 50%; margin-right: 5px;"></i> West<br>
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# ─────────────────────────────────────────────────────────────
# 8. SAVE & EXPORT
# ─────────────────────────────────────────────────────────────
output_file = "customer_distribution_map.html"
m.save(output_file)

print(f"\n✅ Interactive map saved to '{output_file}'")
print(f"   Open in browser to explore delivery hotspots!")
print(f"\n   Map Features:")
print(f"     • {len(df)} order markers with revenue popups")
print(f"     • Color-coded by region (N=Blue, S=Green, E=Red, W=Purple)")
print(f"     • Heatmap overlay showing delivery density")
print(f"     • Marker clustering for zoom-level visualization")
