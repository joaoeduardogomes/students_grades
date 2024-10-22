import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
import os
from dataframes import get_students_status

def plot_pie_chart():
    df = get_students_status()

    status_counts = df["status"].value_counts()

    # Check if there's any data to plot
    if status_counts.empty:
        print("No data to plot.")
        return None


    plt.figure(figsize=(4, 4), facecolor='lightgray')
    plt.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%", colors=["lightgreen", "red"])
    plt.title("Students Status")

    img_path = os.path.join("static", "img", "pie_chart.png")

    plt.savefig(img_path)
    plt.close()

    return img_path

def plot_histogram():
    df = get_students_status()

    plt.figure(figsize=(4, 4), facecolor='lightgray')
    plt.hist(df['grade'], bins=20, color="blue", alpha=0.7)
    plt.xlabel('Grade')
    plt.ylabel("Frequency")
    plt.title("Distribution of Grades")

    img_path = os.path.join("static", "img", "histogram.png")

    plt.savefig(img_path)
    plt.close()

    return img_path