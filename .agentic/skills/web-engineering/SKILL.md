# Skill: Web Engineering (`web-engineering`)

## 1. Purpose
Modern web platform standards, Core Web Vitals, SSR/SSG architectures, and browser performance.

## 2. Activation Conditions
- Architecting web applications, portals, and e-commerce platforms
- Optimizing Core Web Vitals (LCP, INP, CLS)
- Designing client-side caching, service workers, and SEO foundations

## 3. Required Knowledge
- Core Web Vitals: Largest Contentful Paint (LCP), Interaction to Next Paint (INP), Cumulative Layout Shift (CLS)
- Rendering paradigms: Client-Side Rendering (CSR), Server-Side Rendering (SSR), Static Site Generation (SSG), Incremental Static Regeneration (ISR)
- HTTP caching, Cache-Control headers, CDN edge routing, and service workers
- Web security: Content Security Policy (CSP), CORS, SameSite cookies

## 4. Execution Methodology
- 1. Architecture Selection: Choose optimal rendering model (SSR for content/SEO, CSR for rich apps).
- 2. Asset Optimization: Configure responsive image pipelines (AVIF/WebP), font subsetting, and critical CSS.
- 3. Code Splitting: Implement dynamic imports to minimize initial JavaScript bundle size.
- 4. Caching & CDN: Configure immutable asset caching with content hashes and stale-while-revalidate.
- 5. Security Hardening: Implement strict Content Security Policy headers and secure cookies.
- 6. Performance Audit: Run automated Lighthouse and WebPageTest checks in CI.

## 5. Best Practices
- Preload critical fonts and hero images; lazy-load all below-the-fold media.
- Set explicit width and height dimensions on images and containers to prevent CLS.
- Keep initial JavaScript bundle size below 150KB gzipped.

## 6. Common Mistakes to Avoid
- Blocking DOM rendering with render-blocking synchronous scripts in <head>.
- Serving uncompressed, full-resolution JPEG/PNG images to mobile viewports.
- Permitting layout shifts from dynamically injected advertisements or widgets.

## 7. Validation Criteria
- Lighthouse Performance score >= 90.
- LCP < 2.5s, INP < 200ms, CLS < 0.1 on emulated mobile device.
- Strict CSP header configured and verified without console evaluation errors.

## 8. Relevant Tools
`Lighthouse, WebPageTest, Chrome DevTools, Bundle Analyzer`

## 9. Authoritative References
- web.dev: Learn Web Vitals & Web Performance Guidelines
- MDN Web Docs: Web Security and HTTP Headers
