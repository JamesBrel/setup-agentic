# Skill: Flutter & Dart (`flutter-dart`)

## 1. Purpose
Cross-platform mobile and multi-platform development using Flutter framework and Dart language.

## 2. Activation Conditions
- Building mobile applications for iOS and Android
- Authoring Flutter widgets, state management (Bloc/Riverpod), and platform channels
- Optimizing 60fps rendering and mobile performance

## 3. Required Knowledge
- Dart 3 language features (Sound null safety, records, patterns, sealed classes)
- Flutter widget tree, element tree, and render object pipeline
- Predictable state management (flutter_bloc, Riverpod, Provider)
- Platform channels, method channels, and native event streams

## 4. Execution Methodology
- 1. Architecture Setup: Structure project using feature-first or Clean Architecture layers.
- 2. State Management: Implement Bloc / Cubit classes with immutable states and events.
- 3. UI Implementation: Build responsive widget hierarchies using layout builders and tokens.
- 4. API & Data Binding: Integrate Dio or http with interceptors and json_serializable models.
- 5. Offline Storage: Configure Hive, Isar, or sqflite for local persistence.
- 6. Verification: Run flutter analyze, flutter test, and widget tests.

## 5. Best Practices
- Use const constructors wherever possible to avoid unnecessary widget rebuilds.
- Keep widgets small, focused, and composed of specialized child widgets.
- Offload expensive computations (JSON parsing, crypto) to Dart isolates.

## 6. Common Mistakes to Avoid
- Calling setState() at the root of a large widget tree.
- Blocking the UI isolate with synchronous file or network I/O.
- Ignoring platform-specific design guidelines (Material vs Cupertino).

## 7. Validation Criteria
- flutter analyze reports 0 issues, 0 warnings.
- flutter test passes 100% of unit and widget tests.
- Zero frame drops during standard scroll interactions in profile mode.

## 8. Relevant Tools
`flutter, dart analyze, flutter_test, mocktail, bloc_test`

## 9. Authoritative References
- Official Flutter Documentation (flutter.dev)
- Effective Dart: Style and Design Guidelines
