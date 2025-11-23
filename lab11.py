def a():
    from PIL import Image
    import numpy as np

    img = Image.open(r"C:\Users\aumda\OneDrive\Desktop\clg_stuff\sem-3\python\data_sets_for_lab\MU.jpg")
    img_array = np.array(img)

    print("Image mode:", img.mode)
    print("Dimensions:", img.size)
    print("Shape:", img_array.shape)
    print("Minimum pixel value in Blue channel:", img_array[:, :, 2].min())

def b():
    from PIL import Image, ImageOps

    img = Image.open(r"C:\Users\aumda\OneDrive\Desktop\clg_stuff\sem-3\python\data_sets_for_lab\MU.jpg")
    padded_img = ImageOps.expand(img, border=50, fill='black')
    padded_img.show()


def c():
    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt
    img = Image.open(r"C:\Users\aumda\OneDrive\Desktop\clg_stuff\sem-3\python\data_sets_for_lab\MU.jpg")
    img_array = np.array(img)
    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(R, cmap='Reds')
    plt.title("Red Channel")
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.imshow(G, cmap='Greens')
    plt.title("Green Channel")
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.imshow(B, cmap='Blues')
    plt.title("Blue Channel")
    plt.axis('off')
    plt.show()

c()
