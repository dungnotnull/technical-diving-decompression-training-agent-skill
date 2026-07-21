# Gas Mix Calculations Reference

## Gas Mix Fundamentals

### Trimix Composition
Technical diving uses trimix (O₂/He/N₂) to manage three key risks:
- Oxygen toxicity (controlled by O₂ fraction)
- Narcosis (reduced by helium substitution)
- Gas density/work of breathing (reduced by helium)

### Notation Convention
Trimix is denoted as:
```
Tx[O₂%]/[He%]
```
Examples:
- Tx21/35 = 21% O₂, 35% He, 44% N₂
- Tx18/45 = 18% O₂, 45% He, 37% N₂
- Tx15/55 = 15% O₂, 55% He, 30% N₂

## Critical Calculations

### Maximum Operating Depth (MOD)

**Formula:**
```
MOD (meters) = [(PO₂_max / fO₂) - 1] × 10
```
Where:
- PO₂_max = maximum acceptable PO₂ (1.4 bar working, 1.6 bar deco)
- fO₂ = oxygen fraction in gas mix

**Example (Tx21/35):**
```
MOD_working = [(1.4 / 0.21) - 1] × 10 = 56.7 meters
MOD_deco = [(1.6 / 0.21) - 1] × 10 = 66.2 meters
```

### Equivalent Narcotic Depth (END)

**Formula:**
```
END (meters) = [(fN₂ × (Depth + 10) / (1 - fO₂)) - 10]
```
Simplified approximation:
```
END ≈ Depth × fN₂ + (Depth × 0.79 × 0.1)
```
Or more commonly:
```
END = (1 - fHe) × (Depth + 10) - 10
```

**Example (Tx21/35 at 60m):**
```
END = (1 - 0.35) × (60 + 10) - 10 = 35.5 meters
```

**Target:** END < 40 meters (preferably < 30 meters)

### Equivalent Air Depth (EAD) - Nitrox Only

**Formula:**
```
EAD = [(fN₂ × (Depth + 10)) / 0.79] - 10
```

**Example (EAN32 at 30m):**
```
EAD = [(0.68 × 40) / 0.79] - 10 = 24.4 meters
```

### Gas Density

**Formula:**
```
Density = Σ(fraction × molecular_weight) × (Pressure / 22.4)
```
Molecular weights:
- O₂ = 32 g/mol
- N₂ = 28 g/mol
- He = 4 g/mol

**EN14143 Standard:**
- Maximum gas density: 6.2 g/L (recommended)
- Absolute maximum: 8.0 g/L

**Example (Tx21/35 at 60m = 7 bar):**
```
Average MW = (0.21×32) + (0.35×4) + (0.44×28) = 20.6 g/mol
Density = (20.6 / 22.4) × 7 = 6.44 g/L
```

*Result: Exceeds recommended density, consider shallower depth or higher helium*

### CNS Oxygen Toxicity

**CNS% Clock Calculation:**
```
CNS% = Σ [(PO₂ - 0.5) × exposure_time / limit_time] × 100
```
Where limit_time depends on PO₂:
| PO₂ (bar) | CNS% limit (min) |
|------------|------------------|
| 1.3 | 180 |
| 1.4 | 150 |
| 1.5 | 120 |
| 1.6 | 45 |

**OTU (Oxygen Toxicity Units):**
```
OTU = Σ [(PO₂ - 0.5)^1.4 × exposure_time] / 30.3
```
**Daily OTU limit:** 300

**Example (90 min at PO₂ 1.4):**
```
CNS% = (1.4 - 0.5) × 90 / 150 × 100 = 54%
```

### Partial Pressure Calculations

**For any gas component:**
```
P_gas = f_gas × (Depth / 10 + 1)
```

**Example (Tx21/35 at 45m = 5.5 bar):**
```
P_O₂ = 0.21 × 5.5 = 1.16 bar
P_He = 0.35 × 5.5 = 1.93 bar
P_N₂ = 0.44 × 5.5 = 2.42 bar
```

## Gas Selection Guidelines

### By Depth Range

**Shallow (0-40m):**
- Nitrox (EAN32-40) sufficient
- Trimix optional if high helium preference

**Medium (40-70m):**
- Trimix recommended
- Tx21/35 or Tx18/45 typical
- Balance O₂ toxicity and narcosis

**Deep (70-100m):**
- Trimix mandatory
- Tx15/55 or Tx12/60 typical
- High helium for narcosis control

**Extreme (100m+):**
- High helium trimix
- Specialized training required
- Consider CCR options

### By Mission Type

**Recreational Technical:**
- Standard trimix (21/35, 18/45)
- Conservative GF settings
- Ample reserves

**Exploration:**
- Optimized trimix for depth
- Higher helium for narcosis control
- Multiple gas switches

**Cave/Wreck:**
- Standardized gas mixes
- Emphasis on gas density
- Conservative reserves

## Gas Planning

### Rule of Thirds
```
Gas required = Volume_needed × 3
```
Breakdown:
- 1/3 for penetration/inward
- 1/3 for exit/outward
- 1/3 for reserve/emergency

### Rock Bottom Gas
**Formula (single diver failure):**
```
Rock_Bottom = SAC × Depth_ATA × (Ascent_time + Safety_margin)
```

**Formula (team of two, one fails):**
```
Rock_Bottom = SAC × 2 × Depth_ATA × (Ascent_time + Safety_margin)
```

**Typical values:**
- SAC = 20-40 L/min (depending on conditions)
- Ascent_time = from_depth_to_surface / ascent_rate
- Safety_margin = 5-10 minutes

**Example (60m, team ascent, SAC 30):**
```
Ascent from 60m at 9m/min with deco stops ≈ 30 min
Rock_Bottom = 30 × 2 × 7 × 40 = 1680 bar = 84L (12L tank)
```

### Gas Switching During Decompression

**Typical Sequence:**
```
Bottom Gas → Deco Gas 1 (High O₂) → Deco Gas 2 (Pure O₂)
```

**Example (Tx18/45 dive):**
```
Bottom: Tx18/45 (to 70m)
Switch 1: EAN50 (at 21m)
Switch 2: Pure O₂ (at 6m)
```

## Gas Mixing Procedures

### Continuous Blending
1. Start with helium (pure He first)
2. Add oxygen to target
3. Top up with air or nitrogen

### Partial Pressure Blending
1. Add helium to calculated PP
2. Add oxygen to calculated PP
3. Top with air to working pressure

### Safety Checks
- Always analyze final mix
- Verify O₂ percentage (analyzer)
- Check He percentage (helium analyzer or calculation)
- Label cylinder with MOD, mix, and date

## Problem Solving

### High Gas Density
- Increase helium fraction
- Reduce depth target
- Accept higher WOB (within limits)

### Excessive Oxygen Exposure
- Reduce O₂ fraction
- Reduce bottom time
- Increase deco gas O₂

### Hypoxia Risk at Switch
- Ensure minimum 0.16 bar PO₂ at switch depth
- Consider travel mix if deep switches required

### Cost Optimization
- Use lower helium where acceptable
- Plan gas reuse across similar dives
- Bank gases for team use

## References

- Hamilton RW, Thalmann ED. Decompression practice. 1993.
- US Navy Diving Manual. 2021.
- TI Technical Diving Operations Manual. 2020.

---

**Document Version:** 1.0  
**Last Updated:** 2026-07-10  
**Purpose:** Gas selection and calculation reference for technical diving