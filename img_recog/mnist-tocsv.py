import struct
from os import path


def to_csv(name, maxdata):
    current_path = path.dirname(__file__)
    lbl_f = open(current_path + "/mnist/"+name+"-labels-idx1-ubyte", "rb")
    img_f = open(current_path + "/mnist/"+name+"-images-idx3-ubyte", "rb")
    csv_f = open(current_path + "/mnist/"+name+".csv", "w", encoding="utf-8")
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols
    for idx in range(lbl_count):
        if idx > maxdata:
            break
        label = struct.unpack("B", lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")
        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            pgm_path = current_path + "/mnist/{0}-{1}-{2}.pgm"
            iname = pgm_path.format(name, idx, label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()


to_csv("train", 5000)
to_csv("t10k", 500)
