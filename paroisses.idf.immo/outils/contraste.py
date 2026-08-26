def lin(c):
    c = c/255
    return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
def L(h):
    h = h.lstrip('#')
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def ratio(a,b):
    la, lb = L(a), L(b)
    hi, lo = max(la,lb), min(la,lb)
    return (hi+0.05)/(lo+0.05)

C = dict(pierre="#F2EFE9", craie="#FBFAF7", parvis="#E7E2D8", voute="#1C4E80",
         nuit="#10233D", vitrail="#1E6FB8", vitrail_fonce="#155A96", ciel="#9CC8EE",
         encre="#16212E", ardoise="#54626F", ligne="#DAD3C6", or_="#7F6129",
         or_clair="#D0AE6E", chapo_sombre="#CBDCEE", pied="#AFC6DC")

paires = [
 ("encre","pierre","texte courant"), ("encre","craie","texte sur carte"),
 ("encre","parvis","texte sur section douce"),
 ("ardoise","pierre","texte secondaire"), ("ardoise","craie","texte secondaire carte"),
 ("ardoise","parvis","texte secondaire douce"),
 ("vitrail_fonce","pierre","lien / surtitre"), ("vitrail_fonce","craie","lien sur carte"),
 ("vitrail_fonce","parvis","lien sur douce"),
 ("voute","pierre","titre bleu"), ("nuit","pierre","titre marine"),
 ("or_","pierre","OR en texte sur clair"), ("or_","craie","OR en texte sur carte"),
 ("or_clair","nuit","OR sur fond sombre"), ("ciel","nuit","accent clair sur sombre"),
 ("chapo_sombre","nuit","chapo sur sombre"), ("pied","nuit","pied de page"),
 ("craie","voute","texte blanc sur bouton"), ("craie","nuit","blanc sur marine"),
]
for a,b,quoi in paires:
    r = ratio(C[a],C[b])
    etat = "OK  " if r>=4.5 else ("gd  " if r>=3 else "NON ")
    print(f"{etat} {r:5.2f}  {quoi:34s} {a} sur {b}")
