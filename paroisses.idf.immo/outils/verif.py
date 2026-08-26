# -*- coding: utf-8 -*-
"""Contrôles avant commit : équilibre des balises, liens internes, JSON-LD."""
import os, re, json, glob
from html.parser import HTMLParser

DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
VIDES = {"area","base","br","col","embed","hr","img","input","link","meta",
         "param","source","track","wbr"}

class Equilibre(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pile, self.fautes = [], []
    def handle_starttag(self, tag, attrs):
        if tag not in VIDES:
            self.pile.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if tag in VIDES: return
        if not self.pile:
            self.fautes.append("</%s> sans ouverture, ligne %d" % (tag, self.getpos()[0]))
        elif self.pile[-1][0] != tag:
            self.fautes.append("</%s> ligne %d alors que <%s> (ligne %d) est ouverte"
                               % (tag, self.getpos()[0], self.pile[-1][0], self.pile[-1][1][0]))
            self.pile.pop()
        else:
            self.pile.pop()

fichiers = sorted(glob.glob(os.path.join(DEST, "*.html")))
noms = {os.path.basename(f) for f in fichiers}
autres = {"styles.css", "site.js", "marie-celine-etave.jpg", "robots.txt", "sitemap.xml", "CNAME"}
ok = True

for f in fichiers:
    src = open(f, encoding="utf-8").read()
    base = os.path.basename(f)

    p = Equilibre(); p.feed(src)
    if p.fautes or p.pile:
        ok = False
        print("✗ %-32s balises : %s" % (base, "; ".join(p.fautes) or
              "non refermées : " + ", ".join(t for t, _ in p.pile)))

    # liens internes
    for href in re.findall(r'(?:href|src)="([^"]+)"', src):
        if href.startswith(("http", "mailto:", "tel:", "sms:", "#", "data:")):
            continue
        cible, _, ancre = href.partition("#")
        if cible in ("", "/"):
            cible = "index.html"
        if cible not in noms and cible not in autres:
            ok = False
            print("✗ %-32s lien mort : %s" % (base, href))
        elif ancre and cible in noms:
            page = open(os.path.join(DEST, cible), encoding="utf-8").read()
            if ('id="%s"' % ancre) not in page:
                ok = False
                print("✗ %-32s ancre absente : %s" % (base, href))

    # JSON-LD
    for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        try:
            json.loads(bloc)
        except Exception as e:
            ok = False
            print("✗ %-32s JSON-LD invalide : %s" % (base, e))

    # règles de vocabulaire de la famille
    for interdit in ("signalement", "signaler", "sans minimum"):
        for m in re.finditer(interdit, src, re.I):
            ok = False
            print("✗ %-32s mot interdit « %s » (position %d)" % (base, interdit, m.start()))

print("\n%d pages contrôlées — %s" % (len(fichiers), "tout est bon" if ok else "CORRIGER CE QUI PRÉCÈDE"))
