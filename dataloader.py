from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define the same transformations as used for the training/validation set
preprocess = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Load the test dataset
test_dataset_dir = "Videos/organized_images/Combined_0_and_1_images/test_dataset"
test_dataset = datasets.ImageFolder(root=test_dataset_dir, transform=preprocess)

# Create a DataLoader for the test set
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
