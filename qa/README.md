# Quality assurance

The source archive contains seven candidate batches. Their reports are preserved under `source/`, including prior replacements and caution flags. A fresh technical audit confirmed 65 complete A/B/C sets, 195 decodable 512 × 512 PNGs, and no exact duplicates by file or decoded RGB pixel hash. PNG bytes are preserved. The WebP copies are lossy delivery derivatives, not replacement masters.

A thumbnail contact-sheet review checked all 65 sets for broad exercise identity. It does not certify joint mechanics, anatomy, muscle overlays, branding or pixel-exact continuity. In particular, inspect the cycling/elliptical pedal and handle mechanics, rowing machine, incline treadmill, hip thrust, seated calf raise, dumbbell deadlift, hip abduction/adduction, triceps pushdown, overhead extension, dead bug and cable crunch. Additional notes are stored per exercise. The side plank is labeled as a kneeling variant. The supplied QA reports themselves describe candidates; none are marked biomechanically approved.

Every exercise has `qa.biomechanics: pending`. A qualified exercise reviewer should approve the seven gates from the supplied QA layer individually. Do not infer phase meaning from the letters alone, especially for holds, stretches or gait cycles. Preserve the original frames and identifiers when replacing assets; update the hashes and exports together.
