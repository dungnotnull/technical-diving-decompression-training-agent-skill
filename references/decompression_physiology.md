# Decompression Physiology Reference

## Inert Gas Kinetics

### Overview
Decompression physiology governs how inert gases (nitrogen N₂ and helium He) are absorbed and eliminated by body tissues during pressure changes. Understanding these kinetics is fundamental to safe technical diving.

### Henry's Law
The amount of gas dissolved in a liquid is proportional to its partial pressure:
```
C = α × P
```
Where:
- C = concentration of dissolved gas
- α = solubility coefficient of the gas in the tissue
- P = partial pressure of the gas

### Tissue Compartments

#### Parallel Compartment Model
The body is modeled as a set of theoretical tissue compartments, each with a specific half-time for gas uptake/elimination.

**Bühlmann ZHL-16C Model:**
- 16 tissue compartments
- Half-times ranging from 4 to 635 minutes
- Each compartment has unique M-value coefficients (a, b)

#### Half-Time Table

| Compartment | Half-Time (min) | Description |
|-------------|-----------------|-------------|
| 1 | 4 | Fast tissues (brain, spinal cord) |
| 2 | 8 | |
| 3 | 12 | |
| 4 | 16 | |
| 5 | 20 | |
| 6 | 30 | Intermediate tissues |
| 7 | 40 | |
| 8 | 50 | |
| 9 | 60 | |
| 10 | 80 | |
| 11 | 100 | |
| 12 | 120 | Slow tissues (ligaments, cartilage) |
| 13 | 160 | |
| 14 | 200 | |
| 15 | 240 | |
| 16 | 635 | Very slow tissues (bone, fat) |

### Gas Uptake and Elimination

#### Exponential Kinetics
The partial pressure in a tissue compartment changes exponentially:
```
P_t = P_ambient + (P_initial - P_ambient) × e^(-t/τ)
```
Where:
- P_t = tissue partial pressure at time t
- P_ambient = ambient partial pressure
- P_initial = initial tissue partial pressure
- τ = time constant = half_time / ln(2)

#### Uptake (Descent)
During descent, inert gas partial pressure increases:
- Rate depends on tissue blood flow and gas solubility
- Fast tissues saturate quickly but also desaturate quickly
- Slow tissues take longer to saturate but hold gas longer

#### Elimination (Ascent)
During ascent, inert gas partial pressure decreases:
- Same exponential kinetics in reverse
- Supersaturation can lead to bubble formation
- Decompression stops allow safe elimination

### Bubble Formation and Growth

#### Supersaturation
When tissue gas pressure exceeds ambient pressure:
```
Supersaturation Gradient = P_tissue - P_ambient
```

#### Critical Supersaturation
The point at which bubbles begin to form (nucleation):
- Varies by tissue and individual factors
- Influenced by:
  - Rate of ascent
  - Micronuclei (tiny gas pockets)
  - Exercise levels
  - Temperature
  - Hydration status

#### Bubble Dynamics
Once formed, bubbles can:
- Grow by gas diffusion from supersaturated tissues
- Coalesce (merge into larger bubbles)
- Obstruct blood flow (ischemia)
- Compress nerves/neurological symptoms
- Trigger inflammatory response

### Decompression Sickness (DCS)

#### Types of DCS

**Type I (Mild):**
- Joint pain (limb bends)
- Skin manifestations (cutaneous DCS)
- Lymphatic obstruction
- Generally resolves with recompression

**Type II (Serious):**
- Neurological symptoms (numbness, paralysis)
- Pulmonary symptoms (chokes)
- Inner ear/vestibular symptoms
- Cardiopulmonary symptoms
- Requires immediate treatment

#### Venous Gas Emboli (VGE)
- Asymptomatic bubbles detectable via doppler
- Graded on a scale (Spencer scale: 0-4)
- Higher grades correlate with DCS risk
- Used in decompression research

#### PFO (Patent Foramen Ovale)
- Congenital heart defect (hole between atria)
- Allows venous bubbles to enter arterial circulation
- Increases risk of serious DCS (arterial gas embolism)
- Screening recommended for technical divers

### M-Values and Tolerable Supersaturation

#### Bühlmann M-Values
Maximum allowable tissue gas pressures at each depth:
```
P_max = M-value = (Depth + 1) × a × b
```
Where:
- a, b = coefficients specific to each tissue compartment
- Depth = current ambient depth in bar

#### Gradient Factors
Personalized conservatism adjustment:
```
P_limit = GF × (M-value - P_ambient) + P_ambient
```
- GF Low: conservatism at start of decompression (typically 30-40)
- GF High: conservatism at end of decompression (typically 70-85)

## Clinical Applications

### Pre-Dive Considerations
- Medical fitness assessment
- PFO screening for high-risk dives
- Proper hydration
- Avoid alcohol/nitrate vasodilators pre-dive

### In-Water Considerations
- Controlled ascent rates (<9m/min recommended)
- Adequate decompression stops
- Avoid exercise during decompression
- Maintain thermal comfort

### Post-Dive Considerations
- No flying for 12-24 hours post-dive
- Avoid mountain altitude changes
- Monitor for DCS symptoms (up to 24 hours)
- Hydration and rest

### Emergency Management
- Immediate oxygen administration (100%)
- Fluid resuscitation if needed
- Urgent recompression therapy
- Contact diving medical services (DAN)

## References

- Bühlmann AA. Tauchmedizin. Springer, 1995.
- Vann RD, et al. Decompression sickness and bubble formation. Undersea Hyperb Med. 2011.
- Bitterman N, Bitterman S. Oxygen toxicity in diving. Aviat Space Environ Med. 2007.

---

**Document Version:** 1.0  
**Last Updated:** 2026-07-10  
**Purpose:** Domain knowledge reference for technical diving decompression physiology