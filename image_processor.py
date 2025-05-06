from PIL import Image
import os
import matplotlib.pyplot as plt

# --- Implementação Manual (Pixel a Pixel) ---
def to_grayscale_manual(image_path):
    try:
        img_color = Image.open(image_path).convert("RGB")
        width, height = img_color.size
        img_gray = Image.new("L", (width, height))
        for x in range(width):
            for y in range(height):
                r, g, b = img_color.getpixel((x, y))
                gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
                img_gray.putpixel((x, y), gray_value)
        return img_gray
    except FileNotFoundError:
        print(f"Erro: Arquivo de imagem não encontrado em '{image_path}'")
        return None
    except Exception as e:
        print(f"Erro ao converter para grayscale manualmente: {e}")
        return None

def to_binary_manual(img_gray, threshold=127):
    if img_gray is None: return None
    try:
        width, height = img_gray.size
        img_binary = Image.new("L", (width, height))
        for x in range(width):
            for y in range(height):
                pixel_value = img_gray.getpixel((x, y))
                if pixel_value < threshold:
                    img_binary.putpixel((x, y), 0)
                else:
                    img_binary.putpixel((x, y), 255)
        return img_binary
    except Exception as e:
        print(f"Erro ao converter para binário manualmente: {e}")
        return None

# --- Implementação com Funções da Biblioteca Pillow ---
def to_grayscale_pillow(image_path):
    try:
        img_color = Image.open(image_path)
        img_gray = img_color.convert("L")
        return img_gray
    except FileNotFoundError:
        print(f"Erro: Arquivo de imagem não encontrado em '{image_path}'")
        return None
    except Exception as e:
        print(f"Erro ao converter para grayscale com Pillow: {e}")
        return None

def to_binary_pillow(img_gray, threshold=127):
    if img_gray is None: return None
    try:
        img_binary = img_gray.point(lambda p: 255 if p >= threshold else 0)
        if img_binary.mode != 'L':
             img_binary = img_binary.convert('L')
        return img_binary
    except Exception as e:
        print(f"Erro ao converter para binário com Pillow: {e}")
        return None

if __name__ == "__main__":
    input_dir = "images"
    output_dir = "output_images"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Pasta '{input_dir}' criada. Por favor, coloque sua imagem de entrada nela.")

    input_filename = "minha_imagem.jpg" # Esta imagem deve estar na pasta 'images/'
    input_image_path = os.path.join(input_dir, input_filename)

    binarization_threshold = 128
    print(f"Tentando carregar a imagem de: {input_image_path}")

    print("--- Processando com Implementação Manual ---")
    img_gray_manual = to_grayscale_manual(input_image_path)
    if img_gray_manual:
        save_path = os.path.join(output_dir, "grayscale_manual.png")
        img_gray_manual.save(save_path)
        print(f"Imagem em tons de cinza (manual) salva em: {save_path}")
        img_binary_manual = to_binary_manual(img_gray_manual, threshold=binarization_threshold)
        if img_binary_manual:
            save_path = os.path.join(output_dir, "binary_manual.png")
            img_binary_manual.save(save_path)
            print(f"Imagem binarizada (manual) salva em: {save_path}")
    print("-" * 30)

    print("--- Processando com Funções da Biblioteca Pillow ---")
    img_gray_pillow = to_grayscale_pillow(input_image_path)
    if img_gray_pillow:
        save_path = os.path.join(output_dir, "grayscale_pillow.png")
        img_gray_pillow.save(save_path)
        print(f"Imagem em tons de cinza (Pillow) salva em: {save_path}")
        img_binary_pillow = to_binary_pillow(img_gray_pillow, threshold=binarization_threshold)
        if img_binary_pillow:
            save_path = os.path.join(output_dir, "binary_pillow.png")
            img_binary_pillow.save(save_path)
            print(f"Imagem binarizada (Pillow) salva em: {save_path}")
    print("-" * 30)

    try:
        original_img_for_plot = Image.open(input_image_path)
        if img_gray_pillow and img_binary_pillow:
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            axes[0].imshow(original_img_for_plot)
            axes[0].set_title("Original Colorida"); axes[0].axis('off')
            axes[1].imshow(img_gray_pillow, cmap='gray')
            axes[1].set_title("Tons de Cinza (Pillow)"); axes[1].axis('off')
            axes[2].imshow(img_binary_pillow, cmap='gray', vmin=0, vmax=255)
            axes[2].set_title(f"Binarizada (Pillow, Thr={binarization_threshold})"); axes[2].axis('off')
            plt.tight_layout(); plt.show()
        elif os.path.exists(input_image_path):
            print("Imagens processadas não geradas. Exibindo apenas original.")
            plt.imshow(Image.open(input_image_path)); plt.title("Imagem Original Apenas"); plt.axis('off'); plt.show()
        else:
            print("Não foi possível carregar imagens para exibição.")
    except FileNotFoundError:
        print(f"Erro ao carregar '{input_image_path}' para plot. Certifique-se que está na pasta '{input_dir}'.")
    except ImportError:
        print("Matplotlib não instalado. Instale com 'pip install matplotlib'.")
    except Exception as e:
        print(f"Erro ao exibir com Matplotlib: {e}")