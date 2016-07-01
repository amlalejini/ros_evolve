import sys, os, Image

"""
Given an image, generate a 2d binary grid.
 0: empty
 1: occupied
"""

def main():
    """
    main script functionality
    """
    # Command line argument specified?
    if len(sys.argv) < 2:
        print "No image specified."
        exit(-1)
    iname = sys.argv[1]
    # Can I open it as an image?
    print "Opening: " + str(iname)
    img = None
    try:
        img = Image.open(iname).convert("L")
    except:
        print "Failed to open " + str(iname)
        exit(-1)
    img_size = img.size
    pix = img.load()
    gfile_content = ""
    for h in range(0, img_size[1]):
        for w in range(0, img_size[0]):
            gfile_content += str(int(pix[w, h] == 0))
        gfile_content += "\n"
    with open("grid.dat", "w") as fp:
        fp.write(gfile_content)
    img.show()

if __name__ == "__main__":
    main()
