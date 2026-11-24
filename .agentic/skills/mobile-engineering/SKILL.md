# Skill: Mobile Engineering (`mobile-engineering`)

## 1. Purpose
Mobile application lifecycle, offline-first architectures, memory constraints, and app store readiness.

## 2. Activation Conditions
- Architecting mobile applications across iOS, Android, and cross-platform runtimes
- Designing offline synchronization and local caching strategies
- Configuring push notifications, background tasks, and battery efficiency

## 3. Required Knowledge
- Mobile OS lifecycles (foreground, background, suspended, terminated)
- Local storage engines (SQLite, Realm, Keychain / Keystore secure storage)
- Mobile network resiliency, exponential backoff, and offline queueing
- Mobile security (SSL pinning, root/jailbreak detection, code obfuscation)

## 4. Execution Methodology
- 1. Architecture Definition: Establish offline-first data synchronization patterns.
- 2. State & Storage: Configure secure credential storage and encrypted local database.
- 3. Network Layer: Implement request interceptors with automatic token refresh and offline queue.
- 4. Performance Profiling: Profile memory footprint, UI thread frame rate, and startup time.
- 5. Platform Integration: Configure push notification handlers and deep linking routers.
- 6. Release Hardening: Apply ProGuard/R8 rules and verify permissions manifest.

## 5. Best Practices
- Design for intermittent connectivity: all user actions should optimistic-update locally.
- Never store sensitive API tokens or secrets in unencrypted SharedPreferences/UserDefaults.
- Keep cold app startup time under 1.5 seconds.

## 6. Common Mistakes to Avoid
- Performing synchronous disk or database operations on the main UI thread.
- Requesting excessive device permissions at initial app launch before context is clear.
- Failing to handle push notification payloads when the app is in terminated state.

## 7. Validation Criteria
- App functions gracefully in airplane mode with offline queue sync on reconnection.
- Zero ANRs (Application Not Responding) or main thread jank.
- All private credentials stored in secure hardware-backed keystore/keychain.

## 8. Relevant Tools
`Xcode Instruments, Android Profiler, Flipper, Fastlane`

## 9. Authoritative References
- Apple Human Interface Guidelines & iOS Architecture Guides
- Android Developer Guides & Architecture Guidelines (developer.android.com)
