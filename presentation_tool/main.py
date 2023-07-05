from PIL import Image, ImageTk
import tkinter as tk
import os

# PROJECT_ROOT = os.path.expanduser("~/PycharmProjects/GFS-NeuralNetworks/")
PROJECT_ROOT = "D:\Projects\PycharmProjects\GFS-NeuralNetworks"
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
    with open(notes_file, "r", encoding="utf-8") as f:
        note = f.read().split("#---")
        notes.append(note)

print(notes)

root = tk.Tk()
root.title("Presentation Tool")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

small_slides = []
very_small_slides = []
# resize the images to fit the screen
for i in range(len(slides)):
    small_slides.append([])
    very_small_slides.append([])
    for j in range(len(slides[i])):
        slides[i][j] = slides[i][j].resize((w, h), Image.LANCZOS)
        small_slides[i].append(slides[i][j].copy().resize((1920 // 2, 1080 // 2), Image.LANCZOS))
        very_small_slides[i].append(ImageTk.PhotoImage(slides[i][j].copy().resize((1920 // 3, 1080 // 3), Image.LANCZOS)))

root.attributes('-fullscreen', True)
root.configure(background='black')

canvas = tk.Canvas(root, width=w, height=h, bg="black")
canvas.pack()

slides_pos = (0, 0)

img = ImageTk.PhotoImage(slides[0][0])
img_label = tk.Label(canvas, image=img, bg="black")
img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

next_slide_notes_window = tk.Toplevel(root)
next_slide_notes_window.geometry("1600x1050+2560+500")

next_slide_notes_window.configure(background='black')
canvas2 = tk.Canvas(next_slide_notes_window, width=1600, height=1050, bg="black")
canvas2.pack()

img2 = ImageTk.PhotoImage(small_slides[1][0])
img_label2 = tk.Label(canvas2, image=img2, bg="black")
img_label2.place(relx=0.0, rely=0.0, anchor=tk.NW)

notes_label = tk.Label(canvas2, text="Notes", bg="black", fg="white", font=("Helvetica", 20), justify=tk.LEFT,
                       wraplength=500)
notes_label.place(relx=0.9, rely=0.5, anchor=tk.E)

img_label3 = tk.Label(canvas2, image=very_small_slides[0][0], bg="black")
img_label3.place(relx=0.3, rely=0.75, anchor=tk.CENTER)


def jump_to_slide(x, y):
    global slides_pos
    slides_pos = (y, x)
    i = ImageTk.PhotoImage(slides[y][x])
    img_label.configure(image=i)
    img_label.image = i
    update_next_slide_notes()


grid_2D_overview = []
for i in range(len(slides)):
    grid_2D_overview.append([])
    for j in range(len(slides[i])):
        # grid_2D_overview[i].append(tk.Button(canvas2, text=f"{j + 1}", image=very_small_slides[i][j], bg="black", fg="white", font=("Helvetica", 30),
        #                                    command=lambda x=j, y=i: jump_to_slide(x, y)))
        # grid_2D_overview[i][j].grid(row=i, column=j)
        pass


def get_location_string(x, y):
    return f"{x + 1}/{len(slides[y])} | {y + 1}/{len(slides)}"


location_counter = tk.Label(canvas2, text=get_location_string(0, 0), bg="black", fg="white", font=("Helvetica", 30))
location_counter.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def update_next_slide_notes():
    global slides_pos
    next_slide_pos = (slides_pos[0], slides_pos[1] + 1)
    if next_slide_pos[1] >= len(slides[next_slide_pos[0]]):
        next_slide_pos = (next_slide_pos[0] + 1, 0)
    if next_slide_pos[0] >= len(slides):
        next_slide_pos = (0, 0)

    i = ImageTk.PhotoImage(small_slides[slides_pos[0]][slides_pos[1]])
    img_label2.configure(image=i)
    img_label2.image = i

    i3 = very_small_slides[next_slide_pos[0]][next_slide_pos[1]]
    img_label3.configure(image=i3)
    img_label3.image = i3

    location_counter.configure(text=get_location_string(next_slide_pos[1], next_slide_pos[0]))

    if notes[next_slide_pos[0]] is None:
        notes_label.configure(text="No notes")
        return

    if len(notes[next_slide_pos[0]]) <= next_slide_pos[1]:
        notes_label.configure(text="No notes")
        return

    notes_label.configure(text=notes[slides_pos[0]][slides_pos[1]])


def next_slide(event):
    global slides_pos
    slides_pos = (slides_pos[0], slides_pos[1] + 1)
    if slides_pos[1] >= len(slides[slides_pos[0]]):
        slides_pos = (slides_pos[0] + 1, 0)
    if slides_pos[0] >= len(slides):
        slides_pos = (0, 0)
    img = ImageTk.PhotoImage(slides[slides_pos[0]][slides_pos[1]])
    img_label.configure(image=img)
    img_label.image = img
    update_next_slide_notes()


def prev_slide(event):
    global slides_pos
    slides_pos = (slides_pos[0], slides_pos[1] - 1)
    if slides_pos[1] < 0:
        slides_pos = (slides_pos[0] - 1, len(slides[slides_pos[0] - 1]) - 1)
    img = ImageTk.PhotoImage(slides[slides_pos[0]][slides_pos[1]])
    img_label.configure(image=img)
    img_label.image = img
    update_next_slide_notes()


saved_2D_locations = [0 for _ in range(len(slides))]


def skip_right(event):
    global slides_pos
    global saved_2D_locations
    saved_2D_locations[slides_pos[0]] = slides_pos[1]
    slides_pos = (slides_pos[0] + 1, saved_2D_locations[slides_pos[0] + 1])
    if slides_pos[0] >= len(slides):
        slides_pos = (0, saved_2D_locations[0])
    img = ImageTk.PhotoImage(slides[slides_pos[0]][slides_pos[1]])
    img_label.configure(image=img)
    img_label.image = img
    update_next_slide_notes()


def skip_left(event):
    global slides_pos
    global saved_2D_locations
    saved_2D_locations[slides_pos[0]] = slides_pos[1]
    slides_pos = (slides_pos[0] - 1, saved_2D_locations[slides_pos[0] - 1])
    if slides_pos[0] < 0:
        slides_pos = (len(slides) - 1, saved_2D_locations[len(slides) - 1])
    img = ImageTk.PhotoImage(slides[slides_pos[0]][slides_pos[1]])
    img_label.configure(image=img)
    img_label.image = img
    update_next_slide_notes()


# when space is pressed, go to next slide
root.bind("<space>", next_slide)

# when enter is pressed, go to previous slide
root.bind("<Return>", prev_slide)

# when right arrow is pressed, skip to next slide
root.bind("<Right>", next_slide)

# when left arrow is pressed, skip to previous slide
root.bind("<Left>", prev_slide)

root.mainloop()
