/* paroisses.idf.immo — comportements communs.
   Le site reste entièrement lisible et utilisable sans JavaScript :
   ce fichier ne fait qu'afficher la barre d'action fixe sur mobile. */
(function () {
  "use strict";
  var barre = document.getElementById("barre");
  if (!barre) return;

  function ajuste() {
    // On révèle la barre une fois le premier écran dépassé : avant,
    // le bouton du héros est déjà à portée de pouce.
    if (window.scrollY > window.innerHeight * 0.55) {
      barre.classList.add("visible");
    } else {
      barre.classList.remove("visible");
    }
  }

  var enAttente = false;
  window.addEventListener("scroll", function () {
    if (enAttente) return;
    enAttente = true;
    window.requestAnimationFrame(function () {
      ajuste();
      enAttente = false;
    });
  }, { passive: true });

  ajuste();
})();
