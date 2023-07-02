from PIL import Image, ImageTk
import tkinter as tk
import os

PROJECT_ROOT = os.path.expanduser("~/PycharmProjects/GFS-NeuralNetworks/")
SLIDES_DIR = os.path.join(PROJECT_ROOT, "slides")
IMAGES_DIR = os.path.join(SLIDES_DIR, "images")
NOTES_DIR = os.path.join(SLIDES_DIR, "notes")

if not os.path.isfile(os.path.join(SLIDES_DIR, "topics")):
    print("No topics file found in slides dir")
    exit(1)

with open(os.path.join(SLIDES_DIR, "topics"), "r") as f:
    topics = f.readlines()

topics = [topic.strip() for topic in topics]
slide_paths = [(os.path.join(IMAGES_DIR, topic), os.path.join(NOTES_DIR, topic + ".txt")) for topic in topics]

i = 0
for slides, notes in slide_paths:
    if not os.path.isdir(slides):
        print(f"Slides file {slides} not found")
        exit(1)
    if not os.path.isfile(notes):
        print(f"Warning: no notes for {slides}")
        slide_paths[i] = (slides, None)
    i += 1

slides = []
notes = []
for slides_dir, notes_file in slide_paths:
    imgs = os.listdir(slides_dir)
    slides.append([])
    for i in range(len(imgs)):
        imgs[i] = os.path.join(slides_dir, imgs[i])
        img = Image.open(imgs[i])
        slides[-1].append(img)

    if notes_file is None:
        notes.append(None)
        continue
    with open(notes_file, "r") as f:
        note = f.read().split("#---")
        notes.append(note)

print(notes)

root = tk.Tk()
root.title("Presentation Tool")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.attributes('-fullscreen', True)
root.configure(background='black')

canvas = tk.Canvas(root, width=w, height=h, bg="black")
canvas.pack()

img = ImageTk.PhotoImage(slides[0][0])
img_label = tk.Label(canvas, image=img, bg="black")
img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

notes_label = tk.Label(canvas, text="", bg="black", fg="white", font=("Helvetica", 20))
notes_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

slide_index = 0
img_index = 0
notes_index = 0

root.update()