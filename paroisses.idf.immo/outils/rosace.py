import math
CX = CY = 200.0
R_OUT, R_IN = 172.0, 76.0
N = 12
HALF = 11.5   # demi-largeur angulaire d'une lancette, en degrés

def pt(r, deg):
    a = math.radians(deg)
    return (CX + r*math.cos(a), CY + r*math.sin(a))

def f(p):
    return f"{p[0]:.1f} {p[1]:.1f}"

# une lancette dessinée en haut (angle -90°), on la fera tourner
il = pt(R_IN,  -90-HALF); ir = pt(R_IN,  -90+HALF)
ol = pt(R_OUT, -90-HALF); orr= pt(R_OUT, -90+HALF)
lancette = (f"M{f(il)} L{f(ol)} "
            f"A{R_OUT} {R_OUT} 0 0 1 {f(orr)} "
            f"L{f(ir)} "
            f"A{R_IN} {R_IN} 0 0 0 {f(il)} Z")

out = []
out.append('          <!-- les douze lancettes ; celle du haut est la part qui revient -->')
for i in range(N):
    ang = i * (360.0/N)
    cls = "quartier-or" if i == 0 else "verre trait"
    petit = "coeur" if i == 0 else "verre-2 trait"
    out.append(f'          <g transform="rotate({ang:.0f} 200 200)">')
    out.append(f'            <path class="{cls}" d="{lancette}"/>')
    out.append(f'            <circle class="{petit}" cx="200" cy="76" r="13"/>')
    out.append('          </g>')

out.append('')
out.append('          <!-- les meneaux de pierre, entre les lancettes -->')
meneaux = []
for i in range(N):
    ang = -90 + (i + 0.5) * (360.0/N)
    a = pt(R_IN, ang); b = pt(R_OUT, ang)
    meneaux.append(f'            <line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>')
out.append('          <g class="trait">')
out.extend(meneaux)
out.append('          </g>')

out.append('')
out.append('          <!-- la couronne intérieure : six baies -->')
out.append('          <g>')
for i in range(6):
    ang = -90 + i*60
    c = pt(52, ang)
    out.append(f'            <circle class="verre-2 trait" cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="17"/>')
out.append('          </g>')

print("\n".join(out))
