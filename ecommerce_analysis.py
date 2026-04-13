"""
E-Commerce Customer Behavior Analysis
======================================
Data analytics pipeline to segment customers and analyze behavior trends.
Synthesizes a 200-sample dataset using NumPy; applies Pandas filtering to
identify cart abandonment, device-wise traffic, and referral source distribution.

Tech Stack: Python, Pandas, NumPy, Matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────
# 1. SYNTHETIC DATA GENERATION (200 Samples)
# ─────────────────────────────────────────────────────────────
np.random.seed(42)
n = 200

data = {
    "Customer_Id": np.arange(1001, 1001 + n),
    "Session_Duration": np.random.randint(30, 1800, n),          # seconds
    "Pages_Visited": np.random.randint(1, 20, n),
    "Cart_Additions": np.random.randint(0, 10, n),
    "Purchase_Made": np.random.choice(["Yes", "No"], n, p=[0.4, 0.6]),
    "Device_Type": np.random.choice(["Mobile", "Desktop", "Tablet"], n),
    "Referral_Source": np.random.choice(
        ["Google", "Facebook", "Direct", "Email"], n
    ),
}

df = pd.DataFrame(data)

print("=" * 70)
print("  E-COMMERCE CUSTOMER BEHAVIOR ANALYSIS")
print("=" * 70)
print(f"\nDataset Shape: {df.shape}")
print(f"\nFirst 10 Records:\n{df.head(10)}")
print(f"\nDataset Info:")
print(df.describe())

# ─────────────────────────────────────────────────────────────
# 2. CUSTOMERS WHO MADE A PURCHASE
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 70)
print("  TASK 1: Customers Who Made a Purchase")
print("─" * 70)

purchased = df[df["Purchase_Made"] == "Yes"]
print(f"\nTotal customers who purchased: {len(purchased)}")
print(purchased.to_string(index=False))

# ─────────────────────────────────────────────────────────────
# 3. CUSTOMERS WHO DID NOT MAKE A PURCHASE
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 70)
print("  TASK 2: Customers Who Did NOT Make a Purchase")
print("─" * 70)

not_purchased = df[df["Purchase_Made"] == "No"]
print(f"\nTotal customers who did not purchase: {len(not_purchased)}")
print(not_purchased.to_string(index=False))

# ─────────────────────────────────────────────────────────────
# 4. CART ABANDONMENT — Added to Cart but Did Not Purchase
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 70)
print("  TASK 3: Cart Abandonment (Added to Cart but Did Not Purchase)")
print("─" * 70)

cart_abandoned = df[(df["Cart_Additions"] > 0) & (df["Purchase_Made"] == "No")]
print(f"\nTotal cart abandoners: {len(cart_abandoned)}")
print(f"Cart Abandonment Rate: {len(cart_abandoned) / len(df) * 100:.2f}%")
print(cart_abandoned.to_string(index=False))

# ─────────────────────────────────────────────────────────────
# 5. DEVICE TYPE DISTRIBUTION (Percentage)
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 70)
print("  TASK 4: Percentage of Device Type Used for Visiting Pages")
print("─" * 70)

device_counts = df["Device_Type"].value_counts()
device_percentage = (device_counts / len(df) * 100).round(2)

print("\nDevice Type Distribution:")
for device, pct in device_percentage.items():
    print(f"  {device:>10}: {pct}%")

# ─────────────────────────────────────────────────────────────
# 6. REFERRAL SOURCE DISTRIBUTION
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 70)
print("  TASK 5: Referral Source Distribution")
print("─" * 70)

referral_counts = df["Referral_Source"].value_counts()
referral_percentage = (referral_counts / len(df) * 100).round(2)

print("\nReferral Source Distribution:")
for source, pct in referral_percentage.items():
    print(f"  {source:>10}: {pct}%")

# ─────────────────────────────────────────────────────────────
# 7. ADDITIONAL INSIGHTS
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 70)
print("  ADDITIONAL INSIGHTS")
print("─" * 70)

# Average session duration for purchasers vs non-purchasers
avg_session = df.groupby("Purchase_Made")["Session_Duration"].mean()
print(f"\nAverage Session Duration:")
print(f"  Purchasers:     {avg_session.get('Yes', 0):.0f} seconds")
print(f"  Non-Purchasers: {avg_session.get('No', 0):.0f} seconds")

# Average pages visited
avg_pages = df.groupby("Purchase_Made")["Pages_Visited"].mean()
print(f"\nAverage Pages Visited:")
print(f"  Purchasers:     {avg_pages.get('Yes', 0):.1f} pages")
print(f"  Non-Purchasers: {avg_pages.get('No', 0):.1f} pages")

# Device-wise conversion rate
print("\nDevice-wise Conversion Rate:")
device_purchase = df.groupby("Device_Type")["Purchase_Made"].apply(
    lambda x: (x == "Yes").sum() / len(x) * 100
)
for device, rate in device_purchase.items():
    print(f"  {device:>10}: {rate:.1f}%")

# ─────────────────────────────────────────────────────────────
# 8. VISUALIZATION — Matplotlib Charts
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("E-Commerce Customer Behavior Analysis", fontsize=16, fontweight="bold")

# (a) Device Type Distribution — Pie Chart
colors_pie = ["#4e79a7", "#f28e2b", "#76b7b2"]
axes[0, 0].pie(
    device_counts.values,
    labels=device_counts.index,
    autopct="%1.1f%%",
    colors=colors_pie,
    startangle=140,
    explode=[0.05] * len(device_counts),
)
axes[0, 0].set_title("Device Type Distribution")

# (b) Referral Source Distribution — Bar Chart
colors_bar = ["#e15759", "#59a14f", "#edc948", "#b07aa1"]
axes[0, 1].bar(referral_counts.index, referral_counts.values, color=colors_bar)
axes[0, 1].set_title("Referral Source Distribution")
axes[0, 1].set_ylabel("Number of Customers")

# (c) Purchase vs Non-Purchase — Bar Chart
purchase_counts = df["Purchase_Made"].value_counts()
axes[1, 0].bar(
    purchase_counts.index,
    purchase_counts.values,
    color=["#59a14f", "#e15759"],
)
axes[1, 0].set_title("Purchase vs Non-Purchase")
axes[1, 0].set_ylabel("Count")

# (d) Average Session Duration by Device — Bar Chart
avg_session_device = df.groupby("Device_Type")["Session_Duration"].mean()
axes[1, 1].barh(
    avg_session_device.index,
    avg_session_device.values,
    color=colors_pie,
)
axes[1, 1].set_title("Avg Session Duration by Device")
axes[1, 1].set_xlabel("Duration (seconds)")

plt.tight_layout()
plt.savefig("customer_behavior_analysis.png", dpi=150, bbox_inches="tight")
print("\n✅ Charts saved to 'customer_behavior_analysis.png'")
plt.show()

print("\n" + "=" * 70)
print("  ANALYSIS COMPLETE")
print("=" * 70)
