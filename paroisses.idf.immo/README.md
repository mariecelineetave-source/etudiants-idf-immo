# paroisses.idf.immo

Site de proposition aux **paroisses d'Île-de-France** et à leurs paroissiens,
pour Marie-Céline Etave, conseillère en immobilier.

**La proposition :** un paroissien confie un projet immobilier, ou recommande
Marie-Céline à quelqu'un. Si l'opération aboutit, **10 % des honoraires nets**
sont reversés à la paroisse désignée. Le paroissien, lui, ne perçoit rien —
et c'est volontaire.

> ⚠️ **Le site n'est pas encore en ligne.** Il a été créé le 26 août 2026 dans
> le dépôt `etudiants-idf-immo`, branche `claude/paroisses-idf-immo-ytagsf`,
> dossier `paroisses.idf.immo/`. GitHub Pages n'acceptant qu'un domaine par
> dépôt, il devra être déplacé dans son propre dépôt avant publication —
> voir « Mise en ligne » plus bas.

---

## Ce que fait le site

Il s'adresse à un public précis, demandé explicitement : **des cadres et cadres
supérieurs catholiques**. Tout en découle.

1. **Il propose deux chemins.** Le projet immobilier est le vôtre (vendre,
   acheter, faire estimer), ou c'est celui de quelqu'un que vous connaissez.
   Le résultat est le même pour la paroisse.
2. **Il désamorce l'objection avant qu'elle ne soit posée.** « N'est-ce pas
   mêler l'argent à ce qui ne s'achète pas ? » a sa propre section sur
   l'accueil, et « N'est-ce pas une manière d'utiliser la paroisse pour trouver
   des clients ? » ouvre la page des questions — avec pour réponse : « Si. Et
   nous préférons le dire nous-mêmes. »
3. **Il promet la discrétion avant de promettre l'argent.** Par défaut, la
   paroisse reçoit un virement et une référence : ni le nom du paroissien, ni
   l'adresse du bien, ni le prix.
4. **Il donne d'avance le droit de refuser.** « Si votre curé préfère ne pas
   s'associer à cette démarche, la réponse est simplement non. »

### Ce qu'il ne fait pas

Pas de simulateur de gains, pas de compte à rebours, pas d'emoji, pas de point
d'exclamation, aucune citation religieuse utilisée comme accroche, aucune image
pieuse. Le site ne demande jamais d'annonce en chaire, de stand sur le parvis
ni de fichier de paroissiens — et il l'écrit.

---

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `index.html` | L'accueil |
| `nous-en-parler.html` | Le formulaire — deux volets, CSS et JS inclus |
| `comment-ca-marche.html` | Le déroulement, pour les deux chemins |
| `le-reversement.html` | Sur quoi portent les 10 %, quand, à qui |
| `votre-paroisse.html` | La page du curé, de l'économe et du conseil économique |
| `vos-questions.html` | Quinze questions, sans langue de bois |
| `notre-engagement.html` | Huit engagements |
| `conditions-du-reversement.html` | Le règlement, 14 articles |
| `mentions-legales.html` | Éditeur, hébergeur, RGPD |
| `contact.html` | Téléphone, SMS, courriel |
| `styles.css`, `site.js` | Feuille commune, barre d'action mobile |
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
qui est réellement perçu, pas sur les honoraires d'agence bruts : l'écart est
d'environ un quart, et cette erreur a déjà dû être corrigée sur
`associations.idf.immo`.

---

## Notes techniques

- **Aucune dépendance externe** hors les polices Google Fonts (EB Garamond aux
  titres, Archivo au texte). Aucune image externe : la rosace de l'accueil et
  l'église au milieu des immeubles sont des **SVG inline** qui reprennent les
  variables de couleur.
- **Contrastes vérifiés** (WCAG AA) : les dix-neuf paires de couleurs en usage
  sont toutes à 4,5 ou au-dessus.
- **Sans JavaScript**, toutes les pages restent lisibles et les boutons d'appel
  fonctionnent. Le formulaire part alors en POST classique vers FormSubmit :
  ses deux volets sont visibles au lieu d'un seul, ce qui est moins élégant
  mais utilisable.
- **Aucune base de données, aucun cookie, aucune mesure d'audience.**
- Contrôles passés avant chaque commit : équilibre des balises (`html.parser`),
  liens internes et ancres, validité du JSON-LD, mots interdits par la famille.

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
   reste à rédiger. Le modèle d'`etudiants.idf.immo` n'est pas réutilisable —
   il rémunère une personne physique, ce que ce site exclut.
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
