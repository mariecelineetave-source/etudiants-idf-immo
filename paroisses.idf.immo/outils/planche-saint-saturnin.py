# -*- coding: utf-8 -*-
"""Saint-Saturnin d'Antony — la photographie, traitée en planche.

JC Allin, Wikimedia Commons, CC BY-SA 3.0. Recadrée et retraitée :
l'œuvre dérivée reste sous la même licence.

Le tirage : ombres à l'encre froide, hautes lumières sur papier chaud.
Le noir et blanc est pondéré vers le bleu, ce qui éclaircit le ciel très
saturé de l'original au lieu de le laisser plomber la page.
"""
from PIL import Image, ImageChops

SRC = Image.open("saturnin.jpg").convert("RGB")

OMBRE  = (34, 45, 62)      # encre, légèrement bleue
MEDIAN = (150, 148, 143)   # pierre
PAPIER = (248, 245, 238)   # papier chaud

def gris_bleu(img, wr=0.24, wg=0.30, wb=0.46):
    r, v, b = img.split()
    return ImageChops.add(
        ImageChops.add(r.point(lambda p: int(p * wr)), v.point(lambda p: int(p * wg))),
        b.point(lambda p: int(p * wb)))

def courbe(g, noir=26, blanc=214, gamma=0.72):
    ec = max(1, blanc - noir)
    t = []
    for i in range(256):
        u = (i - noir) / ec
        u = 0.0 if u < 0 else (1.0 if u > 1 else u)
        t.append(int(round(255 * (u ** gamma))))
    return g.point(t)

def duo(g):
    canaux = []
    for k in range(3):
        t = []
        for i in range(256):
            u = i / 255.0
            if u < 0.5:
                a, z, w = OMBRE[k], MEDIAN[k], u / 0.5
            else:
                a, z, w = MEDIAN[k], PAPIER[k], (u - 0.5) / 0.5
            t.append(int(a + (z - a) * w))
        canaux.append(g.point(t))
    return Image.merge("RGB", canaux)

def planche(nom, boite, largeur):
    im = duo(courbe(gris_bleu(SRC.crop(boite))))
    h = int(im.height * largeur / im.width)
    im.resize((largeur, h), Image.LANCZOS).save(nom, quality=84, optimize=True, progressive=True)
    print("%-30s %5d x %4d" % (nom, largeur, h))

planche("p1-place.jpg",   (486,  12, 1516, 1180), 1240)  # la façade sur sa place
planche("p2-clocher.jpg", (470,   8,  900, 1010),  900)  # le clocher, vertical
planche("p3-bande.jpg",   (486, 330, 1560, 1010), 1800)  # bandeau large
