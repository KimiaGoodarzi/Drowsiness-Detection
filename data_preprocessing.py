# data_preprocessing.py
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

#  transformations for preprocessing and data augmentation
preprocess = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    # Normalizing
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


def get_data_loaders(image_directory, batch_size=32, train_split=0.8):

    dataset = datasets.ImageFolder(root=image_directory, transform=preprocess)

    # Splitting the dataset (train and validation)
    train_size = int(train_split * len(dataset))
    validation_size = len(dataset) - train_size
    train_dataset, validation_dataset = torch.utils.data.random_split(dataset, [train_size, validation_size])

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    validation_loader = DataLoader(validation_dataset, batch_size=batch_size)

    return train_loader, validation_loader
