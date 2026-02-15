#!/usr/bin/env python3
"""
Demo script showcasing basic AIGC functionality
"""

import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def generate_sample_image():
    """Generate a simple sample image using PyTorch"""
    # Create a gradient image
    x = torch.linspace(0, 1, 256)
    y = torch.linspace(0, 1, 256)
    xx, yy = torch.meshgrid(x, y, indexing='ij')
    
    # Create RGB channels
    r = xx
    g = yy
    b = (xx + yy) / 2
    
    # Combine channels
    img_tensor = torch.stack([r, g, b], dim=-1)
    img_array = (img_tensor.numpy() * 255).astype(np.uint8)
    
    return Image.fromarray(img_array)

def main():
    print("AIGC Examples Demo Script")
    print("========================")
    
    # Generate sample image
    print("Generating sample image...")
    sample_img = generate_sample_image()
    
    # Display image
    plt.figure(figsize=(8, 8))
    plt.imshow(sample_img)
    plt.title("Generated Gradient Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('output/sample_image.png', dpi=150, bbox_inches='tight')
    print("Image saved as 'output/sample_image.png'")
    
    # Print system info
    print(f"\nSystem Information:")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA device count: {torch.cuda.device_count()}")
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()