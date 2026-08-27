# -*- coding: utf-8 -*-
"""Contrôle des contrastes de la palette (WCAG AA : 4,5 pour le texte courant).

    python3 outils/contraste.py
"""

def lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(h):
    h = h.lstrip("#")
    return (0.2126 * lin(int(h[0:2], 16))
            + 0.7152 * lin(int(h[2:4], 16))
            + 0.0722 * lin(int(h[4:6], 16)))


def rapport(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


C = {
    "papier": "#F6F2EA", "papier-clair": "#FBF9F4", "papier-sombre": "#EDE7DB",
    "encre": "#1A1D22", "encre-doux": "#4C525A",
    "trait": "#DBD3C4", "trait-fin": "#E8E2D6",
    "bleu": "#1F3A5F", "bleu-clair": "#A9BED6",
    "bronze": "#7F6129", "bronze-clair": "#C9A968",
    "pied": "#B8C7D9", "pied-bas": "#9FB1C6", "sur-bleu": "#D3DEEB",
}

PAIRES = [
    ("encre", "papier", "texte courant"),
    ("encre", "papier-clair", "texte sur bande claire"),
    ("encre", "papier-sombre", "texte sur bande creusée"),
    ("encre-doux", "papier", "texte secondaire"),
    ("encre-doux", "papier-clair", "texte secondaire, bande claire"),
    ("encre-doux", "papier-sombre", "texte secondaire, bande creusée"),
    ("bleu", "papier", "lien survolé, titres"),
    ("bleu", "papier-clair", "lien sur bande claire"),
    ("bronze", "papier", "la part de la paroisse"),
    ("bronze", "papier-clair", "la part, sur bande claire"),
    ("papier", "bleu", "texte du bouton"),
    ("sur-bleu", "bleu", "texte sur fond bleu"),
    ("bleu-clair", "bleu", "mention sur fond bleu"),
    ("bronze-clair", "bleu", "la part, sur fond bleu"),
    ("pied", "bleu", "pied de page"),
    ("pied-bas", "bleu", "bas de pied de page"),
]

if __name__ == "__main__":
    bon = True
    for a, b, quoi in PAIRES:
        r = rapport(C[a], C[b])
        if r >= 4.5:
            etat = "OK  "
        elif r >= 3:
            etat = "gd  "          # accepté pour du grand texte seulement
        else:
            etat = "NON "
            bon = False
        print("%s %5.2f  %-34s %s sur %s" % (etat, r, quoi, a, b))
    print("\n%s" % ("tous les contrastes tiennent" if bon else "UNE PAIRE NE TIENT PAS"))
