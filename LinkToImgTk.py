import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Function to load image from URL
def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        img_data = response.content
        pil_image = Image.open(BytesIO(img_data))
        return pil_image
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from URL: {e}")
    except PIL.UnidentifiedImageError as e:
        print(f"Error loading image: {e}")

    return None


# Main application
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Image Display from URL")

    # URL of the image
    image_url = "https://image-cdn-ak.spotifycdn.com/image/ab67706c0000da84f068049300d1aa8e8a2eb739"  # Replace with your image URL

    # Load the image from the URL
    pil_image = load_image_from_url(image_url)

    # Convert the image to a format Tkinter can use
    tk_image = ImageTk.PhotoImage(pil_image)

    # Create a label widget to display the image
    label = tk.Label(root, image=tk_image)
    label.pack()

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
