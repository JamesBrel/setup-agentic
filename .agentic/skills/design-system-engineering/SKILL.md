# Skill: Design System Engineering (`design-system-engineering`)

## 1. Purpose
Concevoir, structurer et maintenir un Design System complet et professionnel (tokens, composants atomiques, grilles, thèmes clair/sombre, maquettes haute fidélité) pour les interfaces applicatives à partir d'une idée, en s'appuyant à 100% sur les outils MCP Stitch (`StitchMCP`) et Figma (`figma-dev-mode-mcp-server`), et en sauvegardant tous les documents et maquettes exclusivement dans le dossier `docs/`.

## 2. Activation Conditions
- Définition d'un Design System pour une nouvelle application ou refonte UI/UX.
- Conception de maquettes d'écrans haute fidélité interactives à partir d'un prompt d'idée ou d'un PRD.
- Déclinaison de variantes de composants (boutons, formulaires, cartes, barres de navigation).
- Exécution de la commande `/design_project` ou mission assignée à l'agent `project_designer`.

## 3. Required Knowledge
- Méthodologie Atomic Design (Atomes, Molécules, Organismes, Gabarits, Pages).
- Design Tokens (couleurs sémantiques, échelles typographiques, espacements 4px/8px, arrondis, ombres portées).
- Accessibilité visuelle et conformité WCAG 2.1 AA/AAA (ratios de contraste >= 4.5:1).
- Outils Stitch MCP (`create_project`, `create_design_system`, `generate_screen_from_text`, `edit_screens`, `generate_variants`, `apply_design_system`, `upload_design_md`).
- Outils Figma MCP (`generate_figma_design`, `get_design_context`, `get_variable_defs`, `create_new_file`, `send_code_to_figma`).

## 4. Execution Methodology
- 1. Élicitation des Tokens & Style : Définir la palette chromatique (Primary, Secondary, Neutral, Semantic), l'échelle modale de typographie et les espacements de grille.
- 2. Instanciation du Design System via Stitch / Figma MCP :
   - Invoquer `create_design_system` ou `create_design_system_from_design_md` sur Stitch MCP.
   - Initialiser le projet et les variables Figma avec `create_new_file` et `get_variable_defs`.
   - Exporter la spécification complète dans `docs/design/design_system.md` et `docs/design/tokens.json`.
- 3. Génération des Écrans Applicatifs (UI/UX) :
   - Invoquer `generate_screen_from_text` (Stitch MCP) ou `generate_figma_design` (Figma MCP) pour chaque parcours utilisateur (Onboarding, Auth, Dashboard, Profil, etc.).
   - Utiliser `generate_variants` pour produire les états (vide, chargement, erreur, succès) et les modes clair/sombre.
   - Enregistrer les métadonnées, aperçus et spécifications dans `docs/screens/`.
- 4. Compilation de la Spécification Globale :
   - Assembler le document `docs/DESIGN_SPECIFICATION.md` contenant la cartographie visuelle, les liens de prototypes et les directives pour l'équipe de développement qui implémentera le code dans `app/`.

## 5. Best Practices
- Tous les écrans et composants doivent utiliser exclusivement les tokens déclarés dans le Design System.
- Prévoir systématiquement le mode sombre (Dark Mode) et les états responsives (Mobile / Tablette / Desktop).
- Règle stricte d'emplacement : tous les fichiers de design doivent être générés dans `docs/` et aucun fichier de design ne doit polluer `app/` ou la racine.

## 6. Common Mistakes to Avoid
- Utiliser des valeurs brutes de couleurs (hexadécimales en dur) au lieu de tokens sémantiques.
- Omettre les états interactifs des composants (hover, active, focus, disabled).
- Écrire du code d'application ou placer des fichiers de maquettes en dehors de `docs/`.

## 7. Validation Criteria
- Le Design System est généré et documenté dans `docs/design/design_system.md`.
- Les tokens JSON sont validés dans `docs/design/tokens.json`.
- Tous les écrans de parcours sont générés via Stitch ou Figma MCP et consignés dans `docs/screens/`.
- La spécification maîtresse `docs/DESIGN_SPECIFICATION.md` est finalisée pour le handoff vers `app/`.

## 8. Relevant Tools
`StitchMCP: create_project, create_design_system, generate_screen_from_text, edit_screens, generate_variants | FigmaMCP: generate_figma_design, get_variable_defs, create_new_file`

## 9. Authoritative References
- Atomic Design by Brad Frost (atomicdesign.bradfrost.com)
- Design Tokens Community Group (W3C Community Group)
- Material 3 Design System & Apple Human Interface Guidelines
