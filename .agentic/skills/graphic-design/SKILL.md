# Skill: Graphic Design & Brand Identity (`graphic-design`)

## 1. Purpose
Concevoir l'identité visuelle complète, les logos vectoriels et les icônes d'application multiplateformes (iOS, Android, Web, Desktop) à partir d'une idée produit, en s'appuyant à 100% sur les outils MCP Stitch (`StitchMCP`) et Figma (`figma-dev-mode-mcp-server`), et en générant tous les livrables visuels exclusivement dans le dossier `docs/`.

## 2. Activation Conditions
- Conception d'un logo de marque ou d'application à partir d'un concept ou d'une idée.
- Génération d'icônes d'application adaptatives (Android adaptive icons, iOS app icons, web favicons).
- Création de palettes chromatiques harmonieuses, typographies de marque et assets graphiques vectoriels.
- Exécution de la commande `/design_project` ou sollicitation de l'agent `project_designer`.

## 3. Required Knowledge
- Théorie des couleurs, contrastes d'accessibilité WCAG 2.1 AA/AAA et psychologie des teintes.
- Conception vectorielle (SVG, courbes de Bézier, grilles d'icônes 24x24dp, 48x48dp, 1024x1024px).
- Spécifications d'icônes mobiles (Apple HIG App Icons, Google Material Adaptive Icons avec foreground/background).
- Outils MCP Stitch (`generate_variants`, `upload_design_md`, `download_file`).
- Outils MCP Figma (`generate_vector_illustration`, `generate_image`, `upload_assets`, `download_assets`).

## 4. Execution Methodology
- 1. Analyse de l'Idée & Moodboard : Extraire l'essence du produit, les émotions clés et les métaphores visuelles.
- 2. Logo Design (Figma MCP / Stitch MCP) :
   - Invoquer `generate_vector_illustration` ou `generate_image` pour explorer les concepts de logo (isotype, logotype, monogramme).
   - Générer les variantes (fond clair, fond sombre, monochrome, version compacte).
   - Sauvegarder les rendus et métadonnées dans `docs/logos/`.
- 3. App Icons Suite :
   - Concevoir l'icône maîtresse en haute résolution (1024x1024px).
   - Décliner les calques pour Android (Foreground + Background 432x432px) et les formats iOS / Favicon.
   - Sauvegarder l'ensemble des exports vectoriels et rasterisés dans `docs/icons/`.
- 4. Guide de Marque Graphique : Rédiger le document `docs/BRAND_GUIDELINES.md` récapitulant les règles d'utilisation du logo, les marges de sécurité et les interdits visuels.

## 5. Best Practices
- Toujours générer les logos sous forme vectorielle pour garantir une mise à l'échelle parfaite.
- Vérifier la lisibilité des icônes d'application à petite échelle (16x16px et 32x32px).
- Centraliser l'ensemble des exports graphiques strictement dans `docs/` (jamais dans la racine ni dans `app/`).

## 6. Common Mistakes to Avoid
- Produire des logos trop détaillés illisibles une fois réduits en taille d'icône smartphone.
- Omettre le fond opaque ou les calques séparés requis par les spécifications Android.
- Générer des assets en dehors du répertoire `docs/`.

## 7. Validation Criteria
- Les fichiers de logo et variantes sont exportés dans `docs/logos/`.
- Les icônes d'application sont conformes aux grilles iOS et Android dans `docs/icons/`.
- La documentation de charte graphique est validée dans `docs/BRAND_GUIDELINES.md`.

## 8. Relevant Tools
`StitchMCP: generate_variants, download_file | FigmaMCP: generate_vector_illustration, generate_image, upload_assets`

## 9. Authoritative References
- Apple Human Interface Guidelines - App Icons (developer.apple.com/design/human-interface-guidelines/app-icons)
- Material Design 3 - Icons and Shape (m3.material.io)
