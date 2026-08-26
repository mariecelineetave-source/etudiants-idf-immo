# paroisses.idf.immo — consignes pour les sessions automatisées

Site de **proposition aux paroisses d'Île-de-France** et à leurs paroissiens.
Un paroissien confie un projet immobilier, ou recommande Marie-Céline Etave à
quelqu'un&nbsp;; si l'opération aboutit, **10 % des honoraires nets** sont reversés à
la paroisse désignée. **Le paroissien ne perçoit jamais rien.**

Public visé, explicitement demandé par Marie-Céline&nbsp;: **cadres et cadres
supérieurs catholiques**. Cela commande tout le reste — le ton, la typographie,
l'absence de simulateur, et la franchise sur le conflit d'intérêts.

## ⚠️ Où vit ce site aujourd'hui

Il a été **créé le 26 août 2026 dans le dépôt `etudiants-idf-immo`**, branche
`claude/paroisses-idf-immo-ytagsf`, dans le dossier `paroisses.idf.immo/`.
Ce n'est pas sa place définitive.

GitHub Pages n'acceptant **qu'un domaine par dépôt**, ce site doit être publié
depuis son propre dépôt `mariecelineetave-source/paroisses-idf-immo`, à la
racine, avec le `CNAME` fourni. Restent à faire, dans cet ordre&nbsp;:

1. Créer le dépôt public `paroisses-idf-immo` et y copier le contenu de ce
   dossier **à la racine**.
2. Chez Gandi&nbsp;: enregistrement **CNAME** `paroisses` →
   `mariecelineetave-source.github.io.`
3. GitHub → Settings → Pages&nbsp;: branche `main`, racine, puis cocher
   **Enforce HTTPS**.
4. **Activer FormSubmit pour ce site** (voir plus bas) — sans quoi le
   formulaire n'envoie rien.
5. Raccorder l'espace personnel au socle `app.idf.immo` **si et seulement si**
   Marie-Céline le demande&nbsp;: voir « Ce qui n'a pas été fait ».

## La famille `idf.immo`

Les réseaux de prescripteurs et leur socle, et rien d'autre&nbsp;:

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

**Chaque site reste autonome&nbsp;: ne jamais mélanger les contenus, ne jamais
modifier un autre dépôt depuis celui-ci, et ne jamais copier un texte d'un site
à l'autre.** Les publics n'ont pas les mêmes craintes.

## Deux mécaniques dans la famille — ce site relève de la seconde

| Mécanique | Sites | Bénéficiaire |
|---|---|---|
| **Prime forfaitaire** (800 €, 1 000 €) | etudiants, gardiens, nounous, pros | la personne qui partage |
| **Reversement de 10 % des honoraires nets** | associations, **paroisses** | l'organisme, jamais la personne |

Ne jamais confondre les deux. Sur ce site, **le mot « prime » ne doit désigner
que ce que le site ne fait pas**&nbsp;: le paroissien ne touche rien, et c'est
précisément ce qui le tient hors du statut d'apporteur d'affaires rémunéré.

## Les règles du dispositif

Écrites en dur dans les pages. **Ne jamais les modifier sans validation
explicite de Marie-Céline** — et si l'une change, la changer partout&nbsp;:
`index.html`, `comment-ca-marche.html`, `le-reversement.html`,
`votre-paroisse.html`, `vos-questions.html`, `conditions-du-reversement.html`
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
déjà dû être corrigée sur `associations.idf.immo`&nbsp;: le reversement porte sur ce
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

Communes à la famille&nbsp;:

- **Le mot « signalement » ne doit apparaître nulle part** — ni dans les textes,
  ni dans les URLs, ni dans les `alt`, ni dans les noms de classes.
- **Ne pas écrire « minimum » ni « sans minimum »** dans le texte visible.

Propres à ce site&nbsp;:

- On dit **« reversement »**, jamais « prime », « commission », « rétrocession »
  ni « don » pour désigner les 10 %.
- On dit **« la paroisse »** et **« le paroissien »**. On ne dit pas « le
  fidèle », ni « la communauté », ni « l'ouaille ».
- On écrit **« l'entité désignée par la paroisse »** dès qu'il s'agit d'argent&nbsp;:
  une paroisse n'a pas la personnalité juridique, et l'écrire prouve qu'on sait
  de quoi on parle.
- **Ne jamais laisser entendre un agrément diocésain.** Une convention avec une
  paroisse n'est pas un agrément. C'est écrit noir sur blanc dans
  `votre-paroisse.html`, `vos-questions.html#diocese` et les mentions légales&nbsp;:
  ne pas l'affaiblir.
- **La foi n'est jamais un argument de vente.** Pas de citation d'Évangile
  détournée en accroche, pas d'image pieuse en bandeau, pas d'appel à la
  générosité déguisé en offre commerciale. C'est l'engagement n° 5.

## Le ton — la demande explicite était « très, très subtil »

Ce qui tient le site debout, dans l'ordre&nbsp;:

1. **L'intérêt est avoué.** `vos-questions.html#interet` répond « Si. Et nous
   préférons le dire nous-mêmes » à la question de l'instrumentalisation de la
   paroisse. **Ne jamais adoucir ce passage&nbsp;: c'est le plus persuasif du site
   pour ce public.**
2. **La discrétion prime sur l'argument.** La paroisse reçoit un virement, pas
   un dossier. « Un curé n'a pas à savoir ce que vaut l'appartement de ses
   paroissiens » — cette phrase reste.
3. **Le droit de dire non est offert d'avance.** « Si votre curé préfère ne pas
   s'associer à cette démarche, la réponse est simplement non, et il n'y a rien
   à ajouter. » Ne pas la retirer pour « ne pas décourager ».
4. **La liste de ce qu'on ne demandera jamais** (`votre-paroisse.html`) —
   annonce en chaire, stand sur le parvis, prospectus, fichier de paroissiens,
   exclusivité — vaut mieux que n'importe quelle promesse.
5. Phrases construites, pas de point d'exclamation, pas d'emoji, pas
   d'impératif pressant, pas de compte à rebours. Le vouvoiement partout.

## Palette, typographie et dessins

Le **bleu de la famille `.immo`**, posé sur une **pierre calcaire** au lieu du
bleu pâle des autres sites. Tout est dans `styles.css`, en variables.

- Fonds&nbsp;: `--pierre:#F2EFE9`, `--craie:#FBFAF7`, `--parvis:#E7E2D8`
- Bleus&nbsp;: `--voute:#1C4E80`, `--nuit:#10233D`, `--vitrail:#1E6FB8`,
  `--vitrail-fonce:#155A96`, `--ciel:#9CC8EE`
- Textes&nbsp;: `--encre:#16212E`, `--ardoise:#54626F`
- **Or&nbsp;: `--or:#7F6129` (fond clair), `--or-clair:#D0AE6E` (fond sombre) —
  réservé au seul reversement de 10 %.** Jamais ailleurs.

**Contrastes vérifiés le 26 août 2026** (script `contraste.py`, WCAG AA)&nbsp;: toutes
les paires en usage sont ≥ 4,5. Particularité de ce site&nbsp;: `--or` a été
volontairement assombri à `#7F6129` pour atteindre **5,02 sur `--pierre`** — il
passe donc **aussi en texte sur fond clair**, contrairement aux sites voisins où
l'or est plus clair. Ne pas le « réaligner » sur les autres sites sans
revérifier les contrastes.

**Typographie&nbsp;: EB Garamond aux titres, Archivo au texte courant.** La
famille utilise Fraunces&nbsp;; le garamond a été choisi ici parce que c'est la
lettre des livres qu'a lus ce public. Archivo maintient la parenté.

**Aucune image externe. Tout est en SVG inline**, avec les variables de couleur,
donc un changement de palette suffit à faire suivre les dessins. Trois motifs&nbsp;:

- **La rosace** (`index.html`, classe `.rosace`) — douze lancettes, **une seule
  éclairée en or**&nbsp;: la part qui revient à la paroisse dans un ensemble qui la
  dépasse. Géométrie produite par un script, pas à la main.
- **L'église au milieu des immeubles** (`votre-paroisse.html`, classe
  `.paysage`) — **une seule fenêtre allumée** dans un immeuble voisin&nbsp;: le bien
  que quelqu'un s'apprête à vendre. La rosace de l'église lui répond dans le
  même or. C'est le site entier en un dessin.
- **Les arcs en plein cintre** des deux portes de l'accueil, et les jetons
  d'étapes dont le haut est arrondi (`border-radius:16px 16px 4px 4px`).

Le seul fichier image est `marie-celine-etave.jpg`, portrait publié
volontairement par Marie-Céline sur les autres sites de la famille.

## Structure

- `index.html` — l'accueil. Objectif unique&nbsp;: « Nous en parler ». Sections
  clés&nbsp;: les deux portes, le manifeste, le parcours en 4 temps, ce qui change /
  ne change pas, **la discrétion**, **l'objection**.
- `nous-en-parler.html` — le formulaire (deux volets&nbsp;: projet personnel /
  recommandation), CSS et JS inclus. La page la plus importante.
- `comment-ca-marche.html`, `le-reversement.html`, `votre-paroisse.html`,
  `vos-questions.html`, `notre-engagement.html` — les pages de contenu.
  `votre-paroisse.html` s'adresse au **curé, à l'économe et au conseil
  économique**, pas au paroissien&nbsp;: ne pas mélanger les deux voix.
- `conditions-du-reversement.html` — le règlement, 14 articles.
- `mentions-legales.html` — éditeur, hébergeur, RGPD.
- `contact.html` — téléphone, SMS, courriel.
- `styles.css` — feuille commune. `site.js` — barre d'action mobile.
- `CNAME`, `robots.txt`, `sitemap.xml`.

**Pas de pages par département** (leçon de `nounous.idf.immo`&nbsp;: 81 % de texte
identique, pages satellites déclassées par Google). **Pas de multilingue.**

## Contact — règle stricte

- **`contact@idf.immo` uniquement.** Jamais `contact@paroisses.idf.immo`, qui
  n'existe pas.
- **Téléphone&nbsp;: 06 60 98 92 92.**

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
   auprès d'un trésorier&nbsp;: ne pas le supprimer.
4. **Aucune donnée personnelle dans le dépôt** — il est public. Pas un nom de
   paroisse réelle, pas une coordonnée, pas un nom de curé.
5. **Ne jamais contacter qui que ce soit.**
6. Avant tout commit&nbsp;: relancer `verif.py` (équilibre des balises via
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
  n'est **pas** réutilisable tel quel&nbsp;: il rémunère un indicateur personne
  physique, ce que ce site exclut. Il faut une convention de reversement
  calquée sur celle d'`associations.idf.immo` (article 5.2, même assiette).

## Points à confirmer avec Marie-Céline

Volontairement absents du site tant qu'ils ne sont pas tranchés — ne rien
inventer en attendant.

- **L'accord de BSK Immobilier** sur le principe du reversement à un tiers.
- **L'entrée de `paroisses.idf.immo` dans la famille**, et la mise à jour des
  `CLAUDE.md` des sites voisins en conséquence.
- **Relecture juridique**, en particulier sur deux points&nbsp;: la qualification du
  reversement pour l'entité bénéficiaire, et le fait que le paroissien ne
  perçoive rien (ce qui est précisément ce qui l'écarte du statut d'apporteur
  d'affaires soumis à convention et déclaration).
- **Faut-il prévenir l'économat diocésain avant d'écrire aux paroisses&nbsp;?**
  Le site suppose un contact paroisse par paroisse. Une démarche diocésaine
  préalable serait plus lente mais plus solide. Non tranché.
- **Le tarif de l'expertise** pour les paroissiens&nbsp;: aucun prix n'est affiché.
  Pour mémoire, 1 190 € sur antony.immo, 990 € pour un salarié de CSE
  partenaire. Ne rien afficher tant que ce n'est pas décidé.

## Le formulaire passe par FormSubmit — activation PAR SITE

`nous-en-parler.html` envoie à `contact@idf.immo` via FormSubmit. Ce service
exige une **activation à la première soumission de chaque site**&nbsp;: il envoie un
courriel contenant un lien « Activate Form », et tant que personne n'a cliqué,
**rien ne part**.

**Ce site n'est pas encore activé** — il n'a jamais été mis en ligne. Le premier
envoi de test échouera&nbsp;: c'est normal, c'est lui qui déclenche le courriel
d'activation.

FormSubmit est **injoignable depuis les sessions Claude** (le proxy réseau le
bloque)&nbsp;: ce test ne peut être fait que depuis un vrai navigateur.

## Divers

- Tout en français. Commits clairs en français.
- Le proxy réseau bloque le fetch HTTP direct&nbsp;: un échec `curl` ne signifie PAS
  que le site est en panne.
- Push&nbsp;: `git push -u origin <branche>`&nbsp;; en cas d'erreur réseau, retenter
  jusqu'à 4 fois (2, 4, 8, 16 s).
