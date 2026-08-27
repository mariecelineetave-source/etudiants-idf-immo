# paroisses.idf.immo — consignes pour les sessions automatisées

Site de **proposition aux paroisses d'Île-de-France** et à leurs paroissiens.
Un paroissien confie un projet immobilier, ou recommande Marie-Céline Etave à
quelqu'un ; si l'opération aboutit, **10 % des honoraires nets** sont reversés à
la paroisse désignée. **Le paroissien ne perçoit jamais rien.**

Public visé, explicitement demandé par Marie-Céline : **cadres et cadres
supérieurs catholiques**. Cela commande tout le reste — le ton, la typographie,
l'absence de simulateur, et la franchise sur le conflit d'intérêts.

## ⚠️ Où vit ce site aujourd'hui

Il a été **créé le 26 août 2026 dans le dépôt `etudiants-idf-immo`**, branche
`claude/paroisses-idf-immo-ytagsf`, dans le dossier `paroisses.idf.immo/`.
Ce n'est pas sa place définitive.

GitHub Pages n'acceptant **qu'un domaine par dépôt**, ce site doit être publié
depuis son propre dépôt `mariecelineetave-source/paroisses-idf-immo`, à la
racine, avec le `CNAME` fourni. Restent à faire, dans cet ordre :

1. Créer le dépôt public `paroisses-idf-immo` et y copier le contenu de ce
   dossier **à la racine**.
2. Chez Gandi : enregistrement **CNAME** `paroisses` →
   `mariecelineetave-source.github.io.`
3. GitHub → Settings → Pages : branche `main`, racine, puis cocher
   **Enforce HTTPS**.
4. **Activer FormSubmit pour ce site** (voir plus bas) — sans quoi le
   formulaire n'envoie rien.
5. Raccorder l'espace personnel au socle `app.idf.immo` **si et seulement si**
   Marie-Céline le demande : voir « Ce qui n'a pas été fait ».

## La famille `idf.immo`

Les réseaux de prescripteurs et leur socle, et rien d'autre :

| Domaine | Rôle |
|---|---|
| `gardiens.idf.immo` | réseau des gardiens et gardiennes d'immeubles |
| `etudiants.idf.immo` | réseau étudiant |
| `associations.idf.immo` | réseau des associations loi 1901 |
| `nounous.idf.immo` | réseau des assistantes maternelles et gardes d'enfants |
| `pros.idf.immo` | réseau des professionnels de proximité |
| `paroisses.idf.immo` | **ce site** — nouveau membre, à confirmer par Marie-Céline |
| `app.idf.immo` | le socle commun et le back-office |

**`antony.immo`, `paris7e.immo` et `cse.immo` n'en font PAS partie** (arbitrage
du 21 août 2026). Ne jamais les réintroduire dans cette liste.

**Chaque site reste autonome : ne jamais mélanger les contenus, ne jamais
modifier un autre dépôt depuis celui-ci, et ne jamais copier un texte d'un site
à l'autre.** Les publics n'ont pas les mêmes craintes.

## Deux mécaniques dans la famille — ce site relève de la seconde

| Mécanique | Sites | Bénéficiaire |
|---|---|---|
| **Prime forfaitaire** (800 €, 1 000 €) | etudiants, gardiens, nounous, pros | la personne qui partage |
| **Reversement de 10 % des honoraires nets** | associations, **paroisses** | l'organisme, jamais la personne |

Ne jamais confondre les deux. Sur ce site, **le mot « prime » ne doit désigner
que ce que le site ne fait pas** : le paroissien ne touche rien, et c'est
précisément ce qui le tient hors du statut d'apporteur d'affaires rémunéré.

## Les règles du dispositif

Écrites en dur dans les pages. **Ne jamais les modifier sans validation
explicite de Marie-Céline** — et si l'une change, la changer partout :
`index.html`, `comment-cela-se-passe.html`, `le-reversement.html`,
`votre-paroisse.html`, `questions.html`, `conditions-du-reversement.html`
et le texte de confirmation de `nous-en-parler.html`.

| Règle | Valeur |
|---|---|
| Taux du reversement | **10 %** |
| Assiette | **Honoraires NETS** — après TVA **et** quote-part du réseau mandant (BSK) |
| Fait générateur | **Signature de l'acte authentique** — jamais le compromis ni le mandat |
| Cas couverts | mandat de vente, mandat de recherche, **expertise en valeur vénale** (celle-ci même sans vente) |
| Délai de versement | **15 jours** après encaissement effectif des honoraires |
| Bénéficiaire | l'**entité juridique** désignée par la paroisse (association diocésaine, association paroissiale, compte indiqué par l'économat) |
| Rattachement | désigné **avant le mandat**, une seule paroisse par opération |
| Rémunération du paroissien | **aucune, jamais** |
| Confidentialité | **par défaut la paroisse ne connaît ni le nom, ni l'adresse, ni le prix** |
| Zone | **Île-de-France uniquement** (75, 77, 78, 91, 92, 93, 94, 95) |

**L'assiette est le point où une première version se trompe toujours.** Elle a
déjà dû être corrigée sur `associations.idf.immo` : le reversement porte sur ce
que Marie-Céline perçoit réellement, **pas** sur les honoraires d'agence bruts
facturés au client. L'écart est d'environ un quart. Ne jamais « simplifier » ce
point.

## Pourquoi il n'y a pas de simulateur

Calculer un montant supposerait d'afficher la quote-part retenue par le réseau
mandant, qui n'est pas publique. Un chiffre approximatif serait plus trompeur
qu'utile, et ce public-là repère immédiatement un calcul flatteur. Le site
explique donc l'assiette en cascade (`.cascade` dans `styles.css`) **sans
afficher aucun montant**, et renvoie au décompte exact remis avant signature.
**Ne pas ajouter de simulateur** sans que Marie-Céline ait tranché la question
de la quote-part.

## Le vocabulaire — règles absolues

Communes à la famille :

- **Le mot « signalement » ne doit apparaître nulle part** — ni dans les textes,
  ni dans les URLs, ni dans les `alt`, ni dans les noms de classes.
- **Ne pas écrire « minimum » ni « sans minimum »** dans le texte visible.

Propres à ce site :

- On dit **« reversement »**, jamais « prime », « commission », « rétrocession »
  ni « don » pour désigner les 10 %.
- On dit **« la paroisse »** et **« le paroissien »**. On ne dit pas « le
  fidèle », ni « la communauté », ni « l'ouaille ».
- On écrit **« l'entité désignée par la paroisse »** dès qu'il s'agit d'argent :
  une paroisse n'a pas la personnalité juridique, et l'écrire prouve qu'on sait
  de quoi on parle.
- **Ne jamais laisser entendre un agrément diocésain.** Une convention avec une
  paroisse n'est pas un agrément. C'est écrit noir sur blanc dans
  `votre-paroisse.html`, `vos-questions.html#diocese` et les mentions légales :
  ne pas l'affaiblir.
- **La foi n'est jamais un argument de vente.** Pas de citation d'Évangile
  détournée en accroche, pas d'image pieuse en bandeau, pas d'appel à la
  générosité déguisé en offre commerciale. C'est l'engagement n° 5.

## Le ton — « beaucoup, beaucoup plus fin »

La première rédaction a elle aussi été refusée : « trop grossier ».
Ce qui pèche dans ce registre-là : les phrases à effet, les questions
rhétoriques en accroche, les listes à coches, les impératifs pressants, et
l'argent annoncé d'emblée en gros.

Ce qui tient le site debout, dans l'ordre :

1. **L'intérêt est avoué, sans forfanterie.** « Nous avons évidemment
   intérêt à ce que l'on pense à nous. Il nous a paru plus honnête de l'écrire
   que de le laisser deviner. » **Ne jamais adoucir ce passage, et ne jamais
   le durcir non plus** : la version « Si. Et nous préférons le dire
   nous-mêmes » avait été jugée trop cavalière.
2. **La discrétion passe avant l'argument.** La paroisse reçoit un virement, non
   un dossier. La formule « un curé n'a pas à savoir ce que vaut
   l'appartement de ses paroissiens » a été retirée : juste sur le fond,
   familière sur la forme.
3. **Le droit de refuser est donné d'avance**, au curé comme au conseil
   économique.
4. **La liste de ce que nous ne demanderons jamais** (`votre-paroisse.html`)
   vaut mieux que n'importe quelle promesse.

Règles d'écriture :

- L'argent arrive **tard et une seule fois** sur l'accueil. Le titre ne parle
  pas de pourcentage.
- Phrases construites, subordonnées admises, aucun point d'exclamation, aucun
  emoji, aucun compte à rebours. Vouvoiement partout.
- Ne jamais dire au lecteur ce qu'il pense ou ce qu'il ressent.
- Employer le vocabulaire du milieu avec justesse et sans le surjouer :
  *conseil économique*, *économat diocésain*, *feuille paroissiale*, *denier*,
  *casuel*. Trop en mettre trahit celui qui récite.
- Ne jamais appeler le paroissien « client ».

## Le dessin — refait le 27 août 2026

La première version a été refusée par Marie-Céline : « très cheap ».
Elle avait raison — c'était une page d'atterrissage (héros sombre, cartes à
ombre portée, dégradés, boutons en gélule, rosace vectorielle) et non un objet
destiné à des gens qui lisent. **Ne pas y revenir.**

Le parti pris est désormais celui d'une **page imprimée**. Trois interdits, qui
expliquent presque tout le reste :

1. **Aucune carte à ombre portée.** Là où il faut grouper, on emploie des filets
   (`--trait`) et du blanc, jamais une boîte.
2. **Aucun dégradé**, nulle part.
3. **Aucun bouton en gélule.** Rayon 2 px, un seul bouton plein par page.

### Palette

| Rôle | Variable | Valeur |
|---|---|---|
| La page | `--papier` | `#F6F2EA` |
| Bandes claires / creusées | `--papier-clair` / `--papier-sombre` | `#FBF9F4` / `#EDE7DB` |
| Texte | `--encre` / `--encre-doux` | `#1A1D22` / `#4C525A` |
| Filets | `--trait` / `--trait-fin` | `#DBD3C4` / `#E8E2D6` |
| Le bleu de la famille | `--bleu` / `--bleu-clair` | `#1F3A5F` / `#A9BED6` |
| **La part de la paroisse** | `--bronze` / `--bronze-clair` | `#7F6129` / `#C9A968` |

**Le bronze ne désigne qu'une chose : les 10 % qui reviennent à la paroisse.**
Jamais autre chose. Il a été assombri à `#7F6129` pour tenir 4,5 sur les trois
tons de papier ; `#8A6A33` tombait à 4,49 et ne passait pas.
`python3 outils/contraste.py` vérifie les seize paires en usage.

### Typographie

**EB Garamond aux titres et au texte courant**, 20 px, interligne 1,64, mesure
64 caractères. Archivo n'intervient que pour les mentions en marge, les
étiquettes et les boutons — en petites capitales espacées.

La **ponctuation française est posée automatiquement** par `ponctue()` dans le
générateur : fine insécable devant `;` `!` `?` et dans les guillemets,
insécable devant `:` et `%`. C'est un détail que ce lectorat voit. La fonction
ne touche jamais l'intérieur des balises ni des blocs `<script>`.

### La grille

Une seule structure de page : `.rubrique`, deux colonnes au-delà de 1000 px —
une mention en marge (186 px), le texte à côté. Toutes les pages ont ainsi le
**même bord gauche**, et les mentions servent de titres courants. La mise en
rubriques est **automatique** : `enrubrique()` découpe les sections `.texte` aux
`<h2>` et lit la mention dans `data-mention` du titre. Une page qui contient
déjà des `.rubrique` écrites à la main est laissée telle quelle.

### Les images

**La photographie de l'église Saint-Saturnin d'Antony**, demandée explicitement
par Marie-Céline. C'est celle qu'utilise déjà antony.immo :
`92-Antony-place-St-Saturnin.jpg`, de **JC Allin**, Wikimedia Commons,
**CC BY-SA 3.0**.

- **L'attribution est obligatoire.** Elle figure sous chaque planche et en pied
  de page. Ne jamais la retirer.
- **Le partage à l'identique s'applique aux versions modifiées.** Nos tirages
  recadrés et retraités sont donc eux-mêmes sous CC BY-SA 3.0, et les mentions
  légales le disent. Ce n'est pas contagieux pour le reste du site.
- **Traitement** : recadrage (l'enseigne de commerce et la signalétique de
  voirie sortent du champ), puis bichromie — ombres à l'encre froide, hautes
  lumières sur papier chaud, noir et blanc pondéré vers le bleu pour éclaircir
  un ciel très saturé. `outils/planche-saint-saturnin.py` régénère les tirages.
- Deux cadrages : `saint-saturnin-*.jpg` (la façade et le clocher, à l'accueil)
  et `clocher-*.jpg` (le clocher seul, en marge de `votre-paroisse.html`).

**Le seul ornement dessiné est le trilobe** du pignon de Saint-Saturnin : trois
cercles tangents, en SVG, tracés sans remplissage. Il sert de fleuron entre les
sections, de puce de liste et de favicon. Il n'y a **aucun autre dessin** — la
rosace vectorielle et l'église au milieu des immeubles de la première version
ont été supprimées.

## Structure

- `index.html` — l'accueil. Objectif unique : « Nous en parler ».
  Sections clés : les deux situations, le déroulement, **la discrétion**, la
  citation sur fond bleu, **la réserve**, l'interlocutrice, la zone.
- `nous-en-parler.html` — le formulaire (deux volets : projet personnel /
  recommandation), script inclus. **Marie-Céline a jugé cette page réussie dès
  la première version : ne pas la remanier sans raison.**
- `comment-cela-se-passe.html`, `le-reversement.html`, `votre-paroisse.html`,
  `questions.html`, `nos-engagements.html` — les pages de contenu.
  `votre-paroisse.html` s'adresse au **curé, à l'économe et au conseil
  économique**, non au paroissien : ne pas mélanger les deux voix.
- `conditions-du-reversement.html` — le règlement, 14 articles.
- `mentions-legales.html` — éditeur, hébergeur, **licence des photographies**,
  RGPD.
- `contact.html` — téléphone, message, courriel.
- `styles.css` — feuille commune. `site.js` — barre d'action sur petit écran
  (retirée d'office sur la page du formulaire).
- `images/` — les planches et le portrait. `outils/` — contrôles et
  régénération des images, hors site.
- `CNAME`, `robots.txt`, `sitemap.xml`.

**Pas de pages par département** (leçon de `nounous.idf.immo` : 81 % de texte
identique, pages satellites déclassées par Google). **Pas de multilingue.**

Le site est produit par des scripts de génération conservés hors dépôt, dans le
répertoire de travail de la session. **Les fichiers HTML du dépôt font foi** :
en cas de reprise, éditer le HTML directement plutôt que de chercher à
reconstituer les générateurs.

## Contact — règle stricte

- **`contact@idf.immo` uniquement.** Jamais `contact@paroisses.idf.immo`, qui
  n'existe pas.
- **Téléphone : 06 60 98 92 92.**

## Règles de contenu

1. **Aucun chiffre ni référence juridique inventés.** Sans source vérifiée, on
   n'écrit rien. Pas de statistique sur la pratique religieuse, pas de nombre de
   paroisses, pas de « taux moyen du marché » d'honoraires.
2. **Ne jamais promettre un résultat.** On décrit la méthode, jamais une
   garantie.
3. **Ne pas édulcorer le point fiscal.** `le-reversement.html` et
   `votre-paroisse.html` renvoient à l'économat diocésain ou à l'expert-comptable
   et précisent que le reversement peut constituer une **ressource ordinaire** et
   non un don — donc sans reçu fiscal. C'est ce qui rend la proposition crédible
   auprès d'un trésorier : ne pas le supprimer.
4. **Aucune donnée personnelle dans le dépôt** — il est public. Pas un nom de
   paroisse réelle, pas une coordonnée, pas un nom de curé.
5. **Ne jamais contacter qui que ce soit.**
6. Avant tout commit : relancer `verif.py` (équilibre des balises via
   `html.parser`, liens internes, ancres, JSON-LD, mots interdits).
7. Quand le contenu d'une page publiée change, mettre son `<lastmod>` dans
   `sitemap.xml` à la date du jour (AAAA-MM-JJ).

## Publication

- **Toute modification attend la validation explicite de Marie-Céline
  (« publie »).** Aucune rubrique n'est en publication automatique.

## Ce qui n'a pas été fait, volontairement

- **Pas d'espace personnel (`mon-espace.html`) ni de raccordement Supabase.**
  Marie-Céline a demandé que le site soit **créé d'abord**, l'intégration
  ensuite. Le socle commun `app.idf.immo` devrait recevoir une catégorie
  `paroisse` (ou `paroissien`) et une vue dédiée avant tout branchement.
  **Ne jamais créer un second projet Supabase pour ce site.**
- **Pas de convention de partenariat rédigée.** Le site l'annonce (« une
  page »). Le modèle `convention-indicateur-affaires.md` d'etudiants.idf.immo
  n'est **pas** réutilisable tel quel : il rémunère un indicateur personne
  physique, ce que ce site exclut. Il faut une convention de reversement
  calquée sur celle d'`associations.idf.immo` (article 5.2, même assiette).

## Ce que rapporte la session pros.idf.immo — 27 août 2026

Reçu par routine programmée, à la demande de Marie-Céline. **Ces faits n'ont pas
été vérifiés depuis cette session** : les traiter comme un renseignement utile,
non comme un acquis, et les contrôler avant de s'en servir.

- **FormSubmit s'active par site, non par adresse.** Aucun des cinq formulaires
  de la famille ne l'était avant le 22 août ; gardiens était muet depuis le 13.
  Le premier envoi échoue toujours et déclenche le courriel « Activate Form ».
  C'est une étape normale, pas une panne. (Déjà noté plus bas.)
- **FormSubmit répond 200 en refusant un envoi.** `etudiants` et `associations`
  affichaient donc une confirmation alors que rien ne partait ; corrigé le
  22 août. **Contrôlé ici le 27 août : `nous-en-parler.html` vérifie bien
  `rep.success` avant d'afficher le reçu (ligne 466) et affiche le message exact
  du service en cas de refus (ligne 489).** Ne pas défaire ce contrôle.
- **Pas de pages par département** — confirmé par leur suppression sur pros,
  gardiens et nounous le 27 août. Il n'y en a aucune ici, et il ne faut pas en
  créer.
- **Brevo serait en place et le domaine `idf.immo` authentifié** (DKIM
  brevo1/brevo2, DMARC, SPF Gandi intact) depuis le 22 août. Ne pas redemander à
  Marie-Céline, et ne pas toucher au SPF : l'alignement se ferait par DKIM.
- **Le socle `app.idf.immo` (projet `uiciolavnalimrjlpesx`) serait à jour**, avec
  cinq réseaux actifs — gardiens, nounous, etudiants, associations, pros —
  chacun doté de sa vue. Le réseau `paroisses` reste à ouvrir par un correctif
  SQL, le jour où Marie-Céline demandera le raccordement.

**Répartition proposée par cette session** : elle prendrait la mise en ligne et
le raccordement, ce site gardant le contenu et le ton. **Arbitrage de
Marie-Céline attendu.** Le point important est qu'une seule session à la fois
touche au dépôt et au socle. Les sessions ne s'écrivent pas entre elles ici :
toute réponse passe par elle.

## Points à confirmer avec Marie-Céline

Volontairement absents du site tant qu'ils ne sont pas tranchés — ne rien
inventer en attendant.

- **L'accord de BSK Immobilier** sur le principe du reversement à un tiers.
- **L'entrée de `paroisses.idf.immo` dans la famille**, et la mise à jour des
  `CLAUDE.md` des sites voisins en conséquence.
- **Relecture juridique**, en particulier sur deux points : la qualification du
  reversement pour l'entité bénéficiaire, et le fait que le paroissien ne
  perçoive rien (ce qui est précisément ce qui l'écarte du statut d'apporteur
  d'affaires soumis à convention et déclaration).
- **Faut-il prévenir l'économat diocésain avant d'écrire aux paroisses ?**
  Le site suppose un contact paroisse par paroisse. Une démarche diocésaine
  préalable serait plus lente mais plus solide. Non tranché.
- **Le tarif de l'expertise** pour les paroissiens : aucun prix n'est affiché.
  Pour mémoire, 1 190 € sur antony.immo, 990 € pour un salarié de CSE
  partenaire. Ne rien afficher tant que ce n'est pas décidé.

## Le formulaire passe par FormSubmit — activation PAR SITE

`nous-en-parler.html` envoie à `contact@idf.immo` via FormSubmit. Ce service
exige une **activation à la première soumission de chaque site** : il envoie un
courriel contenant un lien « Activate Form », et tant que personne n'a cliqué,
**rien ne part**.

**Ce site n'est pas encore activé** — il n'a jamais été mis en ligne. Le premier
envoi de test échouera : c'est normal, c'est lui qui déclenche le courriel
d'activation.

FormSubmit est **injoignable depuis les sessions Claude** (le proxy réseau le
bloque) : ce test ne peut être fait que depuis un vrai navigateur.

## Divers

- Tout en français. Commits clairs en français.
- Le proxy réseau bloque le fetch HTTP direct : un échec `curl` ne signifie PAS
  que le site est en panne.
- Push : `git push -u origin <branche>` ; en cas d'erreur réseau, retenter
  jusqu'à 4 fois (2, 4, 8, 16 s).
