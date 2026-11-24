# Skill: Accessibility Engineering (`accessibility-engineering`)

## 1. Purpose
Accessible software design, WCAG 2.1 AA/AAA compliance, screen readers, and universal design.

## 2. Activation Conditions
- Authoring or modifying frontend web and mobile user interfaces
- Running accessibility audits and remediating compliance defects
- Ensuring keyboard navigation and assistive technology compatibility

## 3. Required Knowledge
- WCAG 2.1 guidelines (Perceivable, Operable, Understandable, Robust)
- Accessible Rich Internet Applications (WAI-ARIA) roles, states, and properties
- Color contrast requirements: 4.5:1 for normal text, 3:1 for large text / UI elements
- Screen reader interaction paradigms (VoiceOver, NVDA, TalkBack)

## 4. Execution Methodology
- 1. Semantic Markup: Utilize native semantic HTML elements (<button>, <main>, <nav>, <form>).
- 2. Keyboard Traversal: Ensure all interactive elements have visible focus indicators and logical tab order.
- 3. ARIA Implementation: Add aria-label, aria-expanded, and role attributes where native HTML is insufficient.
- 4. Contrast Verification: Verify all text against background using color contrast analyzers.
- 5. Automated Audit: Run axe-core / Lighthouse accessibility audits in automated tests.
- 6. Manual Screen Reader Check: Test critical workflows with NVDA or VoiceOver.

## 5. Best Practices
- First rule of ARIA: Do not use ARIA if a native HTML element provides the required behavior.
- Never remove default CSS outline: none without providing an accessible :focus-visible replacement.
- Ensure all form controls have explicitly associated <label> elements.

## 6. Common Mistakes to Avoid
- Using generic <div> or <span> elements as click handlers without keyboard event listeners.
- Empty alt attributes on informative images or missing alt on decorative images.
- Inaccessible modal dialogs that fail to trap focus inside the modal.

## 7. Validation Criteria
- Automated axe-core / Lighthouse audit reports zero WCAG 2.1 AA violations.
- Complete keyboard navigation possible across all user journeys without a mouse.
- All interactive controls announce meaningful labels in screen readers.

## 8. Relevant Tools
`axe-core, Lighthouse, WAVE Evaluation Tool, Colour Contrast Analyser`

## 9. Authoritative References
- W3C Web Content Accessibility Guidelines (WCAG) 2.1
- WAI-ARIA Authoring Practices Guide (APG)
