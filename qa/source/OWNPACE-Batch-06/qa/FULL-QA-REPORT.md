# OWNPACE Exercise Library — Visual QA Report

Audit scope: 65 exercises / 195 phase images.

## QA gates

1. Exercise identity matches filename and master brief.
2. Equipment is mechanically plausible and remains continuous across A/B/C.
3. A/B/C show distinct, correctly ordered movement phases.
4. Anatomy contains no merged, missing, duplicated, or malformed limbs.
5. Body scale, camera, lighting, clothing, and equipment stay consistent.
6. Primary and secondary muscle colouring is plausible.
7. Output is 512×512 sRGB PNG with the official OWNPACE overlay.

## Result

- Passed without replacement: **56 exercises / 168 images**
- Rejected and separated: **9 exercises / 27 images**
- Regenerated replacements: **9 exercises / 27 images**
- Final delivery count: **65 exercises / 195 images**

## Rejected and replaced

| Batch | Exercise | Failure found | Corrective action |
|---|---|---|---|
| 01 | Elliptical | Linked handle/pedal opposition and phase geometry were unreliable | Regenerated with flat feet, opposed handles, and fixed rails |
| 01 | Incline treadmill walk | Machine deck read as flat and gait phases were unreliable | Regenerated on a clearly inclined deck with grounded uphill gait |
| 03 | Dumbbell deadlift | Starting blocks changed relationship to the athlete/equipment | Regenerated with blocks fixed on the floor throughout |
| 03 | Hip abduction machine | Pad placement and outward range were insufficiently explicit | Regenerated with clear closed → halfway → open phases |
| 03 | Hip adduction machine | Pad placement and inward range were insufficiently explicit | Regenerated with clear open → halfway → closed phases |
| 06 | Rope triceps pushdown | Wrong exercise imagery was assigned | Regenerated as standing high-pulley rope pushdown |
| 06 | Overhead triceps extension | Wrong exercise imagery was assigned | Regenerated as seated two-hand dumbbell overhead extension |
| 06 | Dead bug | Cable-crunch imagery was assigned to this filename | Regenerated as a supine contralateral dead bug |
| 06 | Kneeling cable crunch | Dead-bug imagery was assigned to this filename | Regenerated as a kneeling high-pulley cable crunch |

The original rejected files are retained separately for audit and are not part of the corrected delivery batches.
