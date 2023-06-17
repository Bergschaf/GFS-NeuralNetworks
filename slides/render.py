import os

SLIDES_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPTS_DIR = os.path.join(SLIDES_ROOT_DIR, 'scripts')
CACHE_DIR = os.path.join(SLIDES_ROOT_DIR, 'cache')
IMAGES_DIR = os.path.join(SLIDES_ROOT_DIR, 'images')

USE_CACHE = True

if not os.path.exists(CACHE_DIR):
    os.mkdir(CACHE_DIR)

if not os.path.exists(IMAGES_DIR):
    os.mkdir(IMAGES_DIR)

scripts = [s for s in os.listdir(SCRIPTS_DIR) if not s.startswith('_') and not s.startswith('media')]
scripts_name = [os.path.splitext(s)[0] for s in scripts]

if USE_CACHE:
    cached = []
    for s in scripts_name:
        if os.path.exists(os.path.join(CACHE_DIR, s)):
            f = open(os.path.join(CACHE_DIR, s), 'r')
            cache = f.read()
            f.close()
            f2 = open(os.path.join(SCRIPTS_DIR, s + '.py'), 'r')
            script = f2.read()
            f2.close()
            if cache == script:
                cached.append(s)
            else:
                f = open(os.path.join(CACHE_DIR, s), 'w')
                f.write(script)
                f.close()
        else:
            f = open(os.path.join(CACHE_DIR, s), 'w')
            f2 = open(os.path.join(SCRIPTS_DIR, s + '.py'), 'r')
            script = f2.read()
            f.write(script)
            f2.close()
            f.close()

    # remove the cached scripts from the list
    for s in cached:
        scripts_name.remove(s)

for name in scripts_name:
    if not os.path.exists(os.path.join(IMAGES_DIR, name)):
        os.mkdir(os.path.join(IMAGES_DIR, name))
    os.system(
        f"manim render {os.path.join(SCRIPTS_DIR, name)}.py --format png -o {os.path.join(IMAGES_DIR, name)}/Slide_ --fps 1 -q l")

#if os.path.exists(os.path.join(SLIDES_ROOT_DIR, "media")):
#    os.system(f"rm -rf {os.path.join(SLIDES_ROOT_DIR, 'media')}")
