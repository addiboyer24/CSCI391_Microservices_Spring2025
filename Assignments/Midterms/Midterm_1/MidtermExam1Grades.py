import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample list of exam scores out of 77
exam_scores = [37.5, 69, 67, 66.5, 71, 63, 74, 60, 69.5, 49.5, 62.5, 61, 54, 51.5]

# Convert exam scores to percentages (out of 77)
exam_percentages = [(score / 77) * 100 for score in exam_scores]

# Calculate the average (mean) percentage
average_percentage = np.mean(exam_percentages)

# Set the style for better visuals using seaborn
sns.set(style="whitegrid")

# Create the histogram with KDE (Kernel Density Estimate) for smooth curve
plt.figure(figsize=(10, 6))
sns.histplot(exam_percentages, bins=10, kde=True, color='skyblue', edgecolor='black', linewidth=1.5)

# Customize the appearance
plt.title('Grade Distribution (Percentages)', fontsize=18, fontweight='bold', color='darkblue')
plt.xlabel('Percentage Scores (%)', fontsize=14, fontweight='bold', color='darkgreen')
plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='darkgreen')

# Add vertical lines for grade boundaries
plt.axvline(x=60, color='orange', linestyle='--', label='D/F Boundary (60%)')
plt.axvline(x=70, color='yellow', linestyle='--', label='C/D Boundary (70%)')
plt.axvline(x=80, color='green', linestyle='--', label='B/C Boundary (80%)')
plt.axvline(x=90, color='blue', linestyle='--', label='A/B Boundary (90%)')

# Add a vertical line for the average percentage
plt.axvline(x=average_percentage, color='red', linestyle='-', label=f'Average ({average_percentage:.2f}%)')

# Add a legend for the vertical lines
plt.legend(title='Grade Boundaries', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()

