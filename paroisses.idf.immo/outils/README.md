# Outils

Scripts de contrôle et de dessin. **Ils ne font pas partie du site** : ils
servent à le vérifier et à régénérer ses illustrations.

| Script | Rôle |
|---|---|
| `verif.py` | Contrôle avant commit : équilibre des balises HTML (`html.parser`), liens internes et ancres, validité des blocs JSON-LD, mots interdits par la famille. À lancer après toute modification. |
| `contraste.py` | Vérifie que les paires de couleurs de la palette tiennent le seuil WCAG AA de 4,5. |
| `rosace.py` | Régénère la géométrie de la rosace du héros (`index.html`). Douze lancettes, une seule en or. |
| `paysage.py` | Régénère l'église au milieu des immeubles (`votre-paroisse.html`). Une seule fenêtre allumée. |

Les deux scripts de dessin écrivent un fragment SVG sur la sortie standard :
il faut ensuite le recoller dans la page concernée.

```
python3 outils/verif.py
python3 outils/contraste.py
```
