import pathlib
import PIL
import PIL.Image
import numpy


# data_dir = pathlib.Path("/content/animal-data/animal_data/").with_suffix('') # Example on Google Colab
data_dir = pathlib.Path("<path_to_dataset>").with_suffix('')

# h x w of the dataset 224 as example
height = 224 
width = 224


def load_dataset(dataset_dir, target_size=(height, width)):
    dataset_dir = Path(data_dir)
    classes = [directory for directory in dataset_dir.iterdir() if directory.is_dir()]
    images = []
    labels = []

    for i, class_dir in enumerate(classes):
        for image_path in class_dir.glob('*'):
            img = Image.open(image_path)
            img = img.resize(target_size)  # Resize images if necessary
            img_array = np.array(img)
            images.append(img_array)
            labels.append(i)  # Label for this image is the index of the class

    return np.array(images), np.array(labels)


dataset_directory = data_dir
images, labels = load_dataset(dataset_directory)
print("Shape of images array:", images.shape)
print("Number of labels:", len(labels))
