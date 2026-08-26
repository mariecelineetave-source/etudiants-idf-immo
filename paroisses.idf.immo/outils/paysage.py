# -*- coding: utf-8 -*-
"""L'église au milieu des immeubles. Une seule fenêtre est allumée :
le bien que quelqu'un s'apprête à vendre. La rosace lui répond dans
le même or. Tout est en SVG, aucune image externe."""

SOL = 250.0
L = []

def immeuble(x, larg, haut_y, cols, rangs, allumee=None):
    """allumee = (col, rang) de la fenêtre en or, ou None."""
    L.append('    <rect class="mur" x="%.0f" y="%.0f" width="%.0f" height="%.0f"/>'
             % (x, haut_y, larg, SOL - haut_y))
    marge_x, marge_y = 11.0, 14.0
    pas_x = (larg - 2*marge_x) / cols
    dispo = (SOL - haut_y) - 2*marge_y
    pas_y = dispo / rangs
    lf, hf = pas_x*0.56, pas_y*0.54
    for r in range(rangs):
        for c in range(cols):
            fx = x + marge_x + c*pas_x + (pas_x - lf)/2
            fy = haut_y + marge_y + r*pas_y + (pas_y - hf)/2
            cls = "allumee" if allumee == (c, r) else "vitre mur"
            L.append('    <rect class="%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1"/>'
                     % (cls, fx, fy, lf, hf))

# --- les immeubles de gauche ---
immeuble(14,  72, 126, 3, 4)
immeuble(94,  62,  96, 2, 5)

# --- les immeubles de droite ; une fenêtre allumée dans le premier ---
immeuble(490, 66, 112, 3, 5, allumee=(1, 1))
immeuble(564, 62, 134, 2, 4)

# --- l'église : le clocher ---
L.append('    <rect class="mur" x="196" y="70" width="66" height="180"/>')
L.append('    <path class="mur" d="M190 70 L229 22 L268 70"/>')
L.append('    <path class="mur" d="M229 22 V6 M221 12 h16"/>')          # la croix
L.append('    <path class="baie" d="M210 108 v-14 a7 7 0 0 1 14 0 v14 z"/>')
L.append('    <path class="baie" d="M234 108 v-14 a7 7 0 0 1 14 0 v14 z"/>')
L.append('    <line class="mur" x1="196" y1="126" x2="262" y2="126"/>')

# --- la nef ---
L.append('    <rect class="mur" x="262" y="150" width="208" height="100"/>')
L.append('    <path class="mur" d="M252 150 L366 104 L480 150"/>')
# la rosace, écho de celle de l'accueil
L.append('    <circle class="rosace-or" cx="366" cy="140" r="19"/>')
L.append('    <g class="mur">')
for i in range(6):
    import math
    a = math.radians(i*60)
    L.append('      <line x1="366" y1="140" x2="%.1f" y2="%.1f"/>'
             % (366 + 19*math.cos(a), 140 + 19*math.sin(a)))
L.append('    </g>')
# le portail
L.append('    <path class="baie" d="M344 250 v-30 a22 22 0 0 1 44 0 v30 z"/>')
# les lancettes de la nef
for x in (288, 316, 416, 444):
    L.append('    <path class="baie" d="M%d 232 v-30 a9 9 0 0 1 18 0 v30 z"/>' % x)

# --- le sol ---
L.append('    <line class="sol" x1="0" y1="250" x2="640" y2="250"/>')

print("\n".join(L))
