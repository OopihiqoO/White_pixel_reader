# Alex B

from PIL import Image
import numpy as np
import csv
import matplotlib.pyplot as plt
import os


def calculate_read_percentage(image_path, threshold=(200, 200, 200)):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    height, width, channels = img_array.shape
    read_pixels = np.all(img_array > threshold, axis=-1)
    
    read_pixel_count = np.sum(read_pixels)
    total_pixel = height * width
    
    read_percentage = (read_pixel_count / total_pixel) * 100
    return read_percentage

def process_images_to_csv(image_paths, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image', 'Read Pixel Percentage'])
        
        for image_path in image_paths:
            read_percentage = calculate_read_percentage(image_path)
            image_name = os.path.basename(image_path)
            writer.writerow([image_name, read_percentage])

def read_csv_data(csv_filename):
    images = []
    read_percentages = []
    
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            image = row[0]
            percentage = float(row[1])
            images.append(image)
            read_percentages.append(percentage)
    
    return images, read_percentages

def plot_read_data(images, read_percentages):
    plt.bar(images, read_percentages, color='cyan')
    plt.xlabel('Images')
    plt.ylabel('Read Pixel Percentage (%)')
    plt.title('Read White Pixels Tracker')
    plt.tight_layout()
    plt.show()

def main():
    image_paths = ['/Users/Lesdrova/Desktop/VS_python/Capstone_401_ab/Ca.png',
                   '/Users/Lesdrova/Desktop/VS_python/Capstone_401_ab/Ca2.png']
    
    csv_filename = 'read_pixels_data.csv'
    process_images_to_csv(image_paths, csv_filename)
    images, read_percentages = read_csv_data(csv_filename)
    print("Images and Read Pixel Percentages from CSV:")
    for image, percentage in zip(images, read_percentages):
        print(f"{image}: {percentage:.2f}%")
    plot_read_data(images, read_percentages)

if __name__ == "__main__":
    main()
