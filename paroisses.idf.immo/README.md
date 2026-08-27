# paroisses.idf.immo

Site de proposition aux **paroisses d'Île-de-France** et à leurs paroissiens,
pour Marie-Céline Etave, conseillère en immobilier.

**La proposition :** un paroissien confie un projet immobilier, ou recommande
Marie-Céline à quelqu'un. Si l'opération aboutit, **10 % des honoraires nets**
sont reversés à la paroisse désignée. Le paroissien, lui, ne perçoit rien —
et c'est volontaire.

> ⚠️ **Le site n'est pas en ligne.** Il vit pour l'instant dans le dépôt
> `etudiants-idf-immo`, branche `claude/paroisses-idf-immo-ytagsf`, dossier
> `paroisses.idf.immo/`. GitHub Pages n'acceptant qu'un domaine par dépôt, il
> devra être déplacé dans son propre dépôt avant publication — voir
> « Mise en ligne ».

---

## Le parti pris

Le public visé — des cadres et cadres supérieurs catholiques — commande tout le
reste. Le site est composé comme une page imprimée, non comme une page
d'atterrissage.

**Au dessin.** Papier chaud, encre, filets, et un seul ornement : le trilobe qui
figure sur le pignon de Saint-Saturnin. Trois interdits expliquent presque tout :
pas de carte à ombre portée, pas de dégradé, pas de bouton en gélule. Titres et
texte courant en EB Garamond ; le sans-serif (Archivo) n'intervient que pour les
mentions en marge et les boutons. La ponctuation française est posée
automatiquement — fine insécable devant `;` `!` `?` et dans les guillemets,
insécable devant `:` et `%`.

**Au texte.** L'argent arrive tard et une seule fois. Pas de phrase à effet, pas
d'interrogation rhétorique en accroche, pas d'impératif pressant. Quatre choses
tiennent le site debout :

1. **L'intérêt est avoué.** « Nous avons évidemment intérêt à ce que l'on pense
   à nous. Il nous a paru plus honnête de l'écrire que de le laisser deviner. »
2. **La discrétion passe avant l'argument.** La paroisse reçoit un virement, non
   un dossier : ni nom, ni adresse, ni prix.
3. **Le droit de refuser est donné d'avance**, au curé comme au conseil
   économique.
4. **La liste de ce que nous ne demanderons jamais** : annonce à l'issue d'une
   célébration, présence sur le parvis, prospectus, fichier de paroissiens,
   exclusivité.

**Ce qu'il n'y a pas.** Aucun simulateur de gains, aucun compte à rebours, aucun
emoji, aucune citation religieuse en accroche, aucune image pieuse.

---

## Les images

L'église **Saint-Saturnin d'Antony**, photographiée par **JC Allin** et publiée
sur Wikimedia Commons sous licence **CC BY-SA 3.0**. C'est la photographie déjà
utilisée par antony.immo.

Elle a été recadrée (l'enseigne de commerce et la signalétique de voirie sont
sorties du champ) puis tirée en bichromie : ombres à l'encre froide, hautes
lumières sur papier chaud, noir et blanc pondéré vers le bleu pour éclaircir un
ciel très saturé. L'original faisait carte postale ; l'objectif était une
planche imprimée.

> **Conséquence de la licence** : l'attribution est obligatoire (elle figure
> sous chaque planche et en pied de page), et les versions modifiées sont
> elles-mêmes diffusées sous CC BY-SA 3.0. C'est le régime sous lequel
> antony.immo utilise déjà cette photographie.

`outils/planche-saint-saturnin.py` régénère les tirages à partir de l'original.

---

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `index.html` | L'accueil |
| `nous-en-parler.html` | Le formulaire — deux volets, script inclus |
| `comment-cela-se-passe.html` | Le déroulement, pour les deux chemins |
| `le-reversement.html` | L'assiette, le fait générateur, le bénéficiaire |
| `votre-paroisse.html` | La page du curé, de l'économe et du conseil économique |
| `questions.html` | Quinze questions, sans langue de bois |
| `nos-engagements.html` | Huit engagements |
| `conditions-du-reversement.html` | Le règlement, 14 articles |
| `mentions-legales.html` | Éditeur, hébergeur, licences, RGPD |
| `contact.html` | Téléphone, message, courriel |
| `styles.css`, `site.js` | Feuille commune, barre d'action sur petit écran |
| `images/` | Les planches et le portrait |
| `outils/` | Contrôles et régénération des images — hors site |
| `CNAME`, `robots.txt`, `sitemap.xml` | Domaine et référencement |
| `CLAUDE.md` | Consignes détaillées pour les sessions automatisées |

---

## Les règles du dispositif

| Règle | Valeur |
|---|---|
| Taux | **10 %** |
| Assiette | **Honoraires nets** — après TVA **et** quote-part du réseau mandant |
| Fait générateur | **Signature de l'acte authentique** |
| Cas couverts | Mandat de vente, mandat de recherche, expertise en valeur vénale |
| Délai | **15 jours** après encaissement des honoraires |
| Bénéficiaire | L'entité juridique désignée par la paroisse |
| Rémunération du paroissien | **Aucune** |
| Zone | Île-de-France (75, 77, 78, 91, 92, 93, 94, 95) |

**L'assiette est le point à ne jamais simplifier.** Le reversement porte sur ce
qui est réellement perçu, non sur les honoraires d'agence bruts : l'écart
avoisine le quart, et cette erreur a déjà dû être corrigée sur
`associations.idf.immo`.

---

## Notes techniques

- **Aucune dépendance externe** hors les polices Google Fonts. Aucune
  bibliothèque, aucun cadre, aucun outil de construction.
- **Contrastes vérifiés** (WCAG AA) : les seize paires en usage tiennent toutes
  4,5 ou davantage — `python3 outils/contraste.py`.
- **Sans JavaScript**, toutes les pages restent lisibles et les boutons d'appel
  fonctionnent. Le formulaire part alors en POST classique vers FormSubmit : ses
  deux volets sont visibles au lieu d'un seul, ce qui est moins élégant mais
  utilisable.
- **Aucune base de données, aucun cookie, aucune mesure d'audience.**
- Contrôles avant commit : `python3 outils/verif.py` — équilibre des balises,
  liens internes, ancres, `srcset`, JSON-LD, sitemap, vocabulaire proscrit.

---

## Mise en ligne

Rien de ceci n'est fait à ce jour.

1. **Créer le dépôt public** `mariecelineetave-source/paroisses-idf-immo` et y
   copier le contenu de ce dossier **à la racine**.
2. **DNS chez Gandi** : enregistrement `CNAME` `paroisses` →
   `mariecelineetave-source.github.io.`
3. **GitHub → Settings → Pages** : branche `main`, racine. Puis cocher
   **Enforce HTTPS**.
4. **Activer FormSubmit** : le service exige une activation par site. Le premier
   envoi échoue et déclenche un courriel « Activate Form » vers
   `contact@idf.immo` ; tant que le lien n'est pas cliqué, rien ne part. Ce test
   ne peut se faire que depuis un vrai navigateur.

---

## À trancher avant diffusion

Ces points sont **volontairement absents du site**.

1. **L'accord de BSK Immobilier** sur le principe d'un reversement à un tiers.
2. **La convention de reversement** : le site l'annonce (« une page »), elle
   reste à rédiger. Le modèle d'`etudiants.idf.immo` n'est pas réutilisable — il
   rémunère une personne physique, ce que ce site exclut.
3. **La relecture juridique**, sur deux points surtout : la qualification
   comptable du reversement pour l'entité bénéficiaire, et le fait que le
   paroissien ne perçoive rien (c'est ce qui l'écarte du statut d'apporteur
   d'affaires).
4. **Faut-il passer par l'économat diocésain avant d'écrire aux paroisses ?**
   Le site suppose un contact paroisse par paroisse. Une démarche diocésaine
   préalable serait plus lente, mais nettement plus solide.
5. **Le tarif de l'expertise** pour les paroissiens : aucun prix n'est affiché.

---

## Ce qui n'a pas été fait, volontairement

Marie-Céline a demandé que **le site soit créé d'abord, l'intégration ensuite**.
Il n'y a donc ni espace personnel, ni raccordement au socle commun
`app.idf.immo`. Le jour venu, le socle devra recevoir une catégorie dédiée et
une vue propre — et surtout pas un second projet Supabase.
