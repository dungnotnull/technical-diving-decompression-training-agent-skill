# Bühlmann ZHL-16C Algorithm Reference

## Algorithm Overview

The Bühlmann ZHL-16C (Zürich Hemisphere 16 Compartment) algorithm is the most widely used decompression model in technical diving. It calculates inert gas kinetics in 16 theoretical tissue compartments to determine safe decompression profiles.

## Mathematical Model

### Tissue Gas Kinetics

#### Schreiner Equation
For each tissue compartment, gas loading follows:
```
P = P_alv + (P_i - P_alv) × (1 - e^(-kt))
```
Where:
- P = tissue partial pressure at time t
- P_alv = alveolar partial pressure of inert gas
- P_i = initial tissue partial pressure
- k = gas constant = ln(2) / half_time
- t = elapsed time

#### For Multi-Gas Mixtures
For trimix (O₂/He/N₂):
```
P_alv_N2 = f_N2 × (P_amb - P_H2O) - RQ × P_CO2
P_alv_He = f_He × (P_amb - P_H2O)
```
Where:
- f_N2, f_He = fractions of inert gases in breathing mix
- P_amb = ambient pressure
- P_H2O = water vapor pressure (0.0627 bar)
- RQ = respiratory quotient (typically 0.8-1.0)

### M-Value Calculation

#### M-Value Coefficients
Each tissue compartment has unique (a, b) coefficients for N₂ and He:

**Nitrogen (N₂) Coefficients:**
| Comp | Half-time (min) | a (bar) | b |
|------|-----------------|---------|---|
| 1 | 4 | 1.6597 | 0.6352 |
| 2 | 8 | 1.5778 | 0.6940 |
| 3 | 12 | 1.5214 | 0.7361 |
| 4 | 16 | 1.4694 | 0.7751 |
| 5 | 20 | 1.4248 | 0.8104 |
| 6 | 30 | 1.3620 | 0.8587 |
| 7 | 40 | 1.3125 | 0.8974 |
| 8 | 50 | 1.2719 | 0.9289 |
| 9 | 60 | 1.2382 | 0.9549 |
| 10 | 80 | 1.1920 | 0.9924 |
| 11 | 100 | 1.1572 | 1.0211 |
| 12 | 120 | 1.1295 | 1.0443 |
| 13 | 160 | 1.0931 | 1.0779 |
| 14 | 200 | 1.0669 | 1.1042 |
| 15 | 240 | 1.0469 | 1.1254 |
| 16 | 635 | 1.0005 | 1.1742 |

**Helium (He) Coefficients:**
| Comp | Half-time (min) | a (bar) | b |
|------|-----------------|---------|---|
| 1 | 4 | 1.6167 | 0.5054 |
| 2 | 8 | 1.4985 | 0.5801 |
| 3 | 12 | 1.4285 | 0.6299 |
| 4 | 16 | 1.3764 | 0.6694 |
| 5 | 20 | 1.3358 | 0.7029 |
| 6 | 30 | 1.2808 | 0.7526 |
| 7 | 40 | 1.2392 | 0.7919 |
| 8 | 50 | 1.2062 | 0.8243 |
| 9 | 60 | 1.1796 | 0.8515 |
| 10 | 80 | 1.1436 | 0.8904 |
| 11 | 100 | 1.1160 | 0.9200 |
| 12 | 120 | 1.0936 | 0.9445 |
| 13 | 160 | 1.0622 | 0.9787 |
| 14 | 200 | 1.0386 | 1.0050 |
| 15 | 240 | 1.0199 | 1.0259 |
| 16 | 635 | 0.9816 | 1.0795 |

#### M-Value Formula
Maximum allowable tissue pressure at depth P:
```
M = (P / b) + a
```
Where P is ambient pressure in bar absolute.

## Gradient Factors

### Theory
Gradient factors personalize decompression conservatism by adjusting the allowable supersaturation gradient.

### Calculation
```
P_limit = GF × (M - P_ambient) + P_ambient
```
Where:
- GF = gradient factor (0-1)
- M = M-value for the compartment
- P_ambient = ambient pressure

### Common GF Settings

**Conservative:**
- GF Low: 30/High: 70
- Longer decompression, reduced DCS risk

**Standard:**
- GF Low: 30/High: 85
- Balance of safety and efficiency

**Aggressive:**
- GF Low: 40/High: 90
- Shorter decompression, increased risk

## Decompression Profile Calculation

### Algorithm Steps

1. **Bottom Phase Calculation**
   - Calculate gas loading for each compartment during bottom time
   - Track compartment pressures at end of bottom time

2. **Ascent Phase Calculation**
   - Calculate gas elimination during ascent
   - Identify leading compartment (most supersaturated)

3. **Stop Determination**
   - Calculate required stops to keep all compartments below limits
   - Apply gradient factors if used
   - Account for gas switching during decompression

### Example Calculation

**Dive Profile:**
- Depth: 45 meters (5.5 bar absolute)
- Bottom time: 30 minutes
- Gas: Tx21/35 (21% O₂, 35% He, 44% N₂)
- GF: 30/85

**Step 1: Calculate Alveolar Pressures**
```
P_amb = 5.5 bar
P_H2O = 0.0627 bar

P_alv_N2 = 0.44 × (5.5 - 0.0627) = 2.39 bar
P_alv_He = 0.35 × (5.5 - 0.0627) = 1.90 bar
```

**Step 2: Calculate Tissue Loading**
For each compartment i:
```
k = ln(2) / half_time_i
t = 30 minutes

P_N2_i = P_alv_N2 + (P_initial_N2_i - P_alv_N2) × (1 - e^(-k×30))
P_He_i = P_alv_He + (P_initial_He_i - P_alv_He) × (1 - e^(-k×30))
```

**Step 3: Calculate Decompression Ceiling**
For each compartment at surface (1 bar):
```
M_N2 = (1 / b_N2_i) + a_N2_i
M_He = (1 / b_He_i) + a_He_i

P_total = P_N2_i + P_He_i + 0.79 (residual N2)

Ceiling_i = P_total / b_effective
```

**Step 4: Determine Stops**
Starting from deepest ceiling, calculate stops at 3-meter intervals, applying GF values for deep vs shallow stops.

## Implementation Considerations

### Accuracy Factors
- Descent rate (typically 20-30 m/min)
- Ascent rate (typically 9-10 m/min)
- Gas switch handling (isobaric switches)
- Respiratory quotient variations
- Individual tissue variability

### Safety Margins
- Always add safety stops (3-6 meters)
- Consider deeper first stops (GF Low adjustment)
- Account for exercise and cold water
- Plan for lost gas scenarios

## Alternative Models

### VPM-B (Variable Permeability Model)
- More conservative for deep dives
- Accounts for bubble nuclei
- Slower decompression schedules

### RGBM (Reduced Gradient Bubble Model)
- Used in some dive computers
- Incorporates bubble mechanics
- Similar to VPM-B conceptually

## References

- Bühlmann AA. Tauchmedizin. Springer, 1995.
- Baker EC. Gradient factors for decompression. 1998.
- Wienke BR. Reduced gradient bubble model. 2001.

---

**Document Version:** 1.0  
**Last Updated:** 2026-07-10  
**Purpose:** Algorithm implementation reference for decompression planning