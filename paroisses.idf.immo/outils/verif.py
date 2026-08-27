# -*- coding: utf-8 -*-
"""Contrôles avant commit : balises, liens, ancres, JSON-LD, vocabulaire.

    python3 outils/verif.py
"""
import glob
import json
import os
import re
from html.parser import HTMLParser

DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
VIDES = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
         "meta", "param", "source", "track", "wbr"}

# le vocabulaire proscrit dans la famille idf.immo, et propre à ce site
PROSCRITS = ["signalement", "signaler", "sans minimum",
             "agrément diocésain de", "mandatée par le diocèse pour"]


class Equilibre(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pile, self.fautes = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VIDES:
            self.pile.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VIDES:
            return
        if not self.pile:
            self.fautes.append("</%s> sans ouverture, ligne %d" % (tag, self.getpos()[0]))
        elif self.pile[-1][0] != tag:
            self.fautes.append("</%s> ligne %d alors que <%s> (ligne %d) est ouverte"
                               % (tag, self.getpos()[0], self.pile[-1][0], self.pile[-1][1][0]))
            self.pile.pop()
        else:
            self.pile.pop()


def cibles(src):
    """Toutes les ressources internes citées : href, src, et srcset."""
    for m in re.findall(r'(?:href|src)="([^"]+)"', src):
        yield m
    for lot in re.findall(r'srcset="([^"]+)"', src):
        for bout in lot.split(","):
            bout = bout.strip().split(" ")[0]
            if bout:
                yield bout


def controle():
    fichiers = sorted(glob.glob(os.path.join(DEST, "*.html")))
    noms = {os.path.basename(f) for f in fichiers}
    ok = True

    for f in fichiers:
        src = open(f, encoding="utf-8").read()
        base = os.path.basename(f)

        p = Equilibre()
        p.feed(src)
        if p.fautes or p.pile:
            ok = False
            print("✗ %-30s balises : %s" % (base, "; ".join(p.fautes) or
                  "non refermées : " + ", ".join(t for t, _ in p.pile)))

        for lien in cibles(src):
            if lien.startswith(("http", "mailto:", "tel:", "sms:", "#", "data:")):
                continue
            chemin, _, ancre = lien.partition("#")
            if chemin in ("", "/"):
                chemin = "index.html"
            if not os.path.exists(os.path.join(DEST, chemin)):
                ok = False
                print("✗ %-30s ressource absente : %s" % (base, lien))
            elif ancre and chemin in noms:
                page = open(os.path.join(DEST, chemin), encoding="utf-8").read()
                if ('id="%s"' % ancre) not in page:
                    ok = False
                    print("✗ %-30s ancre absente : %s" % (base, lien))

        for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
            try:
                json.loads(bloc)
            except Exception as e:
                ok = False
                print("✗ %-30s JSON-LD invalide : %s" % (base, e))

        for mot in PROSCRITS:
            for m in re.finditer(mot, src, re.I):
                ok = False
                print("✗ %-30s mot proscrit « %s » (position %d)" % (base, mot, m.start()))

    # les pages listées au sitemap doivent exister, et réciproquement
    chemin_sitemap = os.path.join(DEST, "sitemap.xml")
    if os.path.exists(chemin_sitemap):
        listees = set()
        for loc in re.findall(r"<loc>https://paroisses\.idf\.immo/([^<]*)</loc>",
                              open(chemin_sitemap, encoding="utf-8").read()):
            listees.add(loc or "index.html")
        for manque in sorted(listees - noms):
            ok = False
            print("✗ sitemap.xml                   page annoncée mais absente : %s" % manque)
        for oublie in sorted(noms - listees):
            ok = False
            print("✗ sitemap.xml                   page présente mais non listée : %s" % oublie)

    print("\n%d pages contrôlées — %s"
          % (len(fichiers), "tout est bon" if ok else "CORRIGER CE QUI PRÉCÈDE"))
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if controle() else 1)
