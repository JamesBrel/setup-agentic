# Skill: Desktop Engineering (`desktop-engineering`)

## 1. Purpose
Cross-platform desktop application engineering with Electron, Tauri, Flutter Desktop, and OS integration.

## 2. Activation Conditions
- Building native desktop applications for Windows, macOS, and Linux
- Implementing desktop IPC, native system menus, and tray management
- Packaging installers, code signing, and auto-updating

## 3. Required Knowledge
- Desktop architectures: Electron (Chromium + Node), Tauri (Rust + Webview), Flutter Desktop
- Desktop window lifecycles, multi-window management, and native menus
- Secure Inter-Process Communication (IPC) and context isolation
- Desktop packaging formats: MSIX, DMG, AppImage, DEB, RPM

## 4. Execution Methodology
- 1. Framework Selection: Select Tauri for minimal memory footprint or Flutter/Electron.
- 2. IPC Hardening: Implement strictly validated, message-based IPC bridge with contextIsolation.
- 3. OS Integration: Implement system tray, native menus, keyboard shortcuts, and file associations.
- 4. Auto-Update Pipeline: Configure secure, signed auto-update manifests (Sparkle, Squirrel).
- 5. Installer Packaging: Generate target installers with bundled runtime dependencies.
- 6. Verification: Test window resize, multi-monitor display, sleep/resume, and uninstall.

## 5. Best Practices
- Always enable contextIsolation: true and nodeIntegration: false in Electron WebPreferences.
- Validate and sanitize all arguments passed across IPC boundaries.
- Minimize idle CPU and memory consumption when window is minimized or hidden.

## 6. Common Mistakes to Avoid
- Exposing raw Node.js child_process or filesystem APIs directly to the renderer process.
- Failing to handle high-DPI scaling across heterogeneous multi-monitor setups.
- Leaving zombie background processes running after main window is closed.

## 7. Validation Criteria
- Zero security warnings in Electron / Tauri security audit tools.
- Clean installation and uninstallation on target Windows, macOS, and Linux systems.
- Application cleanly terminates all child worker processes upon window exit.

## 8. Relevant Tools
`Tauri CLI, Electron Forge, electron-builder, WiX Toolset`

## 9. Authoritative References
- Tauri Architecture and Security Guide (tauri.app)
- Electron Security Tutorial and Checklist (electronjs.org/docs)
