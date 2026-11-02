# Android packaging and instrumentation

For network-constrained `JobScheduler` work, declare the normal
`android.permission.ACCESS_NETWORK_STATE` permission and exercise the actual
receiver/job scheduling path on the selected Android version. Android 14 and
later enforce this permission when scheduling network jobs; compilation and
lint alone do not establish that scheduling succeeds. See the
[JobInfo network constraint contract](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setRequiredNetworkType(int)).

Before installing or running Android instrumentation after main-source changes, build both the
target application APK and the test APK in the same Gradle invocation (for example,
`assembleDebug assembleDebugAndroidTest`). Building only `assembleDebugAndroidTest` can leave a
stale target APK beside a newly compiled test APK and produce misleading `NoSuchMethodError`
failures on-device.

Java source or target compatibility does not make newer JDK library APIs available on Android.
Check the selected Android SDK/desugaring surface when adding test helpers; for example, use
explicit UTF-8 `Files.readAllBytes`/`Files.write` for small text files when `Files.readString` or
`Files.writeString` is absent from `android.jar`. Stream large media and model files instead of
loading them wholesale merely to hash or copy them.

Preflight both actual APK manifests and installed package versions before installing either APK.
Instrumentation APKs can omit declared version fields; keep that case distinct from malformed
metadata and the product's positive release-version policy. Bind any effective default to the
selected platform's parsing contract and the literal test package, then compare the actual guest
version without allowing downgrades. Test the real metadata reader with both LF and CRLF output
before launching a guest. After a partial setup, reconcile installed APK hashes and reuse matching
bytes; repair only the failed observer or unexecuted installation, preserving the original failure
without rebuilding, reinstalling both packages or wiping the guest merely to obtain a clean run.

Source-based instrumentation selectors must recognize valid runtime-eligibility annotations
between `@Test` and a method declaration, including `@SdkSuppress`. Verify the exact package,
class, method, annotation contract and complete selected inventory before guest mutation.
Preserve a parser refusal and repair that observer against the unchanged source; do not remove
a valid eligibility annotation or rebuild the APK merely to satisfy an outdated matcher.

Derive native pixel witnesses from the actual effect's opaque interior and observed clip,
including density-scaled rounding. An axis-aligned mask bound does not make its corner opaque.
Retain failed pixels and literal draw identity before assertions; distinguish a bad sample point
from missing coverage, and rerun only the corrected failed contract after verifying unchanged
production bytes and preserving independently recorded passing cases.
