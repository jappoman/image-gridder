from PIL import Image, ImageDraw

def draw_grid(image_path):
    # Apri l'immagine originale
    original_image = Image.open(image_path)

    # Crea una nuova immagine con dimensioni 16cm x 16cm
    new_image = Image.new('RGB', (590, 590), 'white')

    # Ridimensiona l'immagine originale alla dimensione desiderata
    resized_image = original_image.resize((590, 590))

    # Copia l'immagine ridimensionata nella nuova immagine
    new_image.paste(resized_image, (0, 0))

    # Crea un oggetto ImageDraw per disegnare sulla nuova immagine
    draw = ImageDraw.Draw(new_image)

    # Calcola la dimensione di ciascun quadratino
    square_size = 590 // 16

    # Disegna la griglia con numerazione
    for i in range(17):
        x = i * square_size
        y = 590 - (i * square_size)
        draw.line([(x, 0), (x, 590)], fill='black')
        draw.line([(0, y), (590, y)], fill='black')
        draw.text((x + 2, y + 2), f'{i},{16-i}', fill='black')

    # Salva l'immagine risultante
    new_image.save('immagine_con_griglia.png')

# Richiedi il percorso dell'immagine da tastiera
input_image_path = input("Inserisci il percorso dell'immagine: ")
draw_grid(input_image_path)
