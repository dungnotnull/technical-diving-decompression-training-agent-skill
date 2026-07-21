# Analysis Prompt Templates

## Template 1: Dive Profile Analysis

**User Input:** User provides dive plan with depth, time, gas mix

**System Response Template:**

```
# Dive Profile Analysis: [Depth]m for [Time]min on [Gas Mix]

## Input Parameters
- Depth: [X] meters ([X] bar absolute)
- Bottom Time: [X] minutes
- Gas Mix: [O₂]%/[He]%/[N₂]%
- Environment: [Freshwater/Saltwater], [Temperature]°C
- Diver Level: [Certification], [X] dives

## Gas Mix Validation
- MOD (working PO₂ 1.4): [X]m ✓/✗
- MOD (deco PO₂ 1.6): [X]m ✓/✗
- END at [Depth]m: [X]m ✓/✗ (target <40m)
- Gas Density at [Depth]m: [X] g/L ✓/✗ (limit 6.2 g/L)
- Assessment: [PASS/FAIL - detailed issues]

## Decompression Profile (Bühlmann ZHL-16C, GF [Low]/[High])
- Leading Compartment: #[X] (half-time [X] min)
- Required Stops:
  - [X]m: [X] minutes
  - [X]m: [X] minutes
  - ...
  - 6m: [X] minutes
  - 3m: [X] minutes (safety)
- Total Run Time: [X] minutes
- Total Deco Time: [X] minutes

## Oxygen Exposure
- Bottom Phase PO₂: [X] bar (CNS%: [X]%)
- Deco Phase PO₂: [X] bar (CNS%: [X]%)
- Total CNS%: [X]% (limit: 80%)
- OTU: [X] (limit: 300/day)
- Assessment: [PASS/FAIL]

## Gas Requirements
- Bottom Gas Required: [X] bar (Rule of Thirds)
- Deco Gas Required: [X] bar
- Reserve Gas: [X] bar (Rock Bottom calculation)
- Total Gas: [X] bar

## Risk Assessment
- Decompression Stress: [LOW/MEDIUM/HIGH]
- Oxygen Toxicity Risk: [LOW/MEDIUM/HIGH]
- Narcosis Risk: [LOW/MEDIUM/HIGH]
- Gas Density Risk: [LOW/MEDIUM/HIGH]
- Overall Risk Level: [LOW/MEDIUM/HIGH]

## ⚠️ DISCLOSURE
> This analysis is based on [model] with [GF] settings. Actual dive
> conditions may vary. Always add safety margins and monitor for
> DCS symptoms. This is not medical advice.

## Recommendation
**Verdict:** [SAFE/CONSERVATIVE/CONDITIONAL/HIGH RISK/REVISE]

**Conditions (if applicable):**
- [Condition 1]
- [Condition 2]

**Recommended Actions:**
- [Action 1]
- [Action 2]

**Evidence Sources:**
- [Source 1 with Tier]
- [Source 2 with Tier]
- [Source 3 with Tier]

---
*Analysis by technical-diving-decompression-training v1.0*
```

## Template 2: Gas Mix Optimization

**User Input:** User requests gas mix recommendation for depth range

**System Response Template:**

```
# Gas Mix Optimization for [Depth Range]

## Requirements
- Target Depth: [X]m
- Mission Type: [Recreation/Exploration/Cave/Wreck]
- Diver Level: [Certification]
- Preferences: [Cost/Safety/Performance priority]

## Gas Mix Options

### Option 1: Tx[O₂]/[He] (Recommended)
**Composition:** [O₂]% O₂ / [He]% He / [N₂]% N₂

**Analysis:**
- MOD (1.4 bar): [X]m ✓
- END at [Depth]m: [X]m ✓
- Density: [X] g/L ✓
- Cost: [$/L]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Best For: [Use cases]

### Option 2: Tx[O₂]/[He] (Alternative)
**Composition:** [O₂]% O₂ / [He]% He / [N₂]% N₂

**Analysis:**
- MOD (1.4 bar): [X]m ✓
- END at [Depth]m: [X]m ✓
- Density: [X] g/L ✓
- Cost: [$/L]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Best For: [Use cases]

### Option 3: [Other Option]
[Similar structure]

## Comparison Matrix

| Metric | Option 1 | Option 2 | Option 3 |
|--------|----------|----------|----------|
| MOD (m) | [X] | [X] | [X] |
| END (m) | [X] | [X] | [X] |
| Density (g/L) | [X] | [X] | [X] |
| CNS%/min | [X] | [X] | [X] |
| Cost ($/fill) | [X] | [X] | [X] |

## Recommendation
**Best Option:** [Option X]

**Reasoning:**
- [Reason 1]
- [Reason 2]

**Implementation Notes:**
- [Mixing procedure]
- [Analysis requirements]
- [Labeling requirements]

## ⚠️ DISCLOSURE
> Gas selection involves trade-offs between safety, performance, and cost.
> Always analyze final mix and verify with O₂/He analyzers before use.

## Evidence Sources
- [Source 1]
- [Source 2]
- [Source 3]

---
*Gas analysis by technical-diving-decompression-training v1.0*
```

## Template 3: DCS Risk Assessment

**User Input:** User describes dive profile and asks for DCS risk

**System Response Template:**

```
# DCS Risk Assessment: [Dive Profile Summary]

## Dive Profile
- Depth: [X]m
- Bottom Time: [X] min
- Ascent Rate: [X] m/min
- Deco Profile: [GF settings, stops]
- Gas Used: [Mix]

## Risk Factors Analysis

### Tissue Loading
- Leading Compartment: #[X] (half-time [X] min)
- Peak Supersaturation: [X]% above M-value
- Gas Elimination Efficiency: [HIGH/MEDIUM/LOW]

### Individual Risk Factors
- **Age:** [X] years → [INCREASED/NORMAL] risk
- **BMI:** [X] → [INCREASED/NORMAL] risk
- **Fitness Level:** [EXCELLENT/GOOD/FAIR/POOR] → Risk impact
- **PFO Status:** [UNKNOWN/NEGATIVE/POSITIVE] → Risk impact
- **Hydration Status:** [GOOD/FAIR/POOR] → Risk impact
- **Recent Diving:** [X] dives in [X] days → Risk impact

### Dive Factors
- **Ascent Rate:** [X] m/min → [ACCEPTABLE/FAST]
- **Deco Compliance:** [All stops/Missed stops] → Risk impact
- **Thermal Stress:** [COLD/COMFORTABLE/WARM] → Risk impact
- **Exercise During Deco:** [HIGH/MODERATE/NONE] → Risk impact
- **Gas Density:** [X] g/L → Risk impact

### Overall DCS Risk
**Estimated Risk Level:** [VERY LOW/LOW/MODERATE/HIGH/VERY HIGH]

**Risk Estimate:** [X]% ([Confidence interval])

**Compared To:** [Similar profiles: X% DCS rate]

## Mitigation Strategies

### Immediate Actions
- [Action 1] (e.g., slower ascent, additional safety stops)
- [Action 2] (e.g., hydration monitoring)

### Protocol Adjustments
- [Adjustment 1] (e.g., GF adjustment: 30/70 → 20/80)
- [Adjustment 2] (e.g., nitrox for deco gas)

### Post-Dive Monitoring
- Monitor for symptoms for: [X] hours
- Key symptoms to watch: [symptom list]
- Action if symptoms appear: [medical protocol]

## ⚠️ CRITICAL DISCLOSURE
> DCS risk estimation is probabilistic, not deterministic. Even
> conservative profiles carry some residual risk. This assessment
> does not replace medical evaluation. If symptoms occur, seek
> immediate medical attention and contact DAN emergency services.

## Recommendation
**Proceed:** [YES/NO/CONDITIONAL]

**If Proceeding:**
- Follow conservative GF settings
- Add safety stops
- Monitor closely post-dive

**If Not Proceeding:**
- Required modifications: [list]
- Re-assessment after: [changes]

## Evidence Sources
- [Study 1 with DCS incidence data]
- [Study 2 with risk factor analysis]
- [Standard 3 with guidelines]

---
*DCS risk assessment by technical-diving-decompression-training v1.0*
```

## Template 4: Emergency Procedure Planning

**User Input:** User requests emergency planning for dive

**System Response Template:**

```
# Emergency Procedure Planning: [Dive Profile]

## Dive Summary
- Profile: [Depth]m, [Time]min bottom
- Team Size: [X] divers
- Environment: [Location/Conditions]
- Planned Gas: [Mixes]

## Emergency Scenarios

### Scenario 1: Lost Gas at Bottom
**Trigger:** Complete gas loss at maximum depth

**Immediate Actions:**
1. [Action 1 - e.g., Signal team, deploy SMB]
2. [Action 2 - e.g., Switch to backup gas]
3. [Action 3 - e.g., Begin controlled ascent]

**Gas Requirements:**
- Rock Bottom: [X] bar (team ascent from [X]m)
- Required SAC: [X] L/min (stress elevated)
- Ascent Time: [X] min with omitted deco

**Risk Assessment:**
- DCS Risk: [HIGH/MODERATE]
- Recommended Action: [Immediate surface / Controlled ascent]

### Scenario 2: Team Member DCS Symptoms
**Trigger:** DCS symptoms during dive

**Immediate Actions:**
1. [Action 1 - e.g., Stop ascent, stabilize diver]
2. [Action 2 - e.g., Administer 100% O₂ if available]
3. [Action 3 - e.g., Call emergency services]

**Medical Management:**
- Position: [Supine/Left lateral]
- Oxygen: [Flow rate, duration]
- Fluids: [Yes/No, type]
- Transport: [Ground/Air, destination]

**Contact Information:**
- DAN Emergency: [+1 number]
- Local Chamber: [Facility, number]
- Emergency Services: [911/local]

### Scenario 3: Hypoxia at Gas Switch
**Trigger:** PO₂ drops below 0.16 bar

**Immediate Actions:**
1. [Action 1 - e.g., Verify gas supply]
2. [Action 2 - e.g., Switch to backup gas]
3. [Action 3 - e.g., Ascend to safer depth]

**Prevention:**
- Minimum switch PO₂: [X] bar
- Check gas before: [switch depth]
- Have travel mix: [YES/NO]

### Scenario 4: Separated from Team
**Trigger:** Loss of visual/contact with team

**Immediate Actions:**
1. [Action 1 - e.g., Search 1 min, use audible signal]
2. [Action 2 - e.g., Deploy SMB, ascend to safety stop]
3. [Action 3 - e.g., Surface at planned interval]

**Prevention:**
- Team protocols: [description]
- Communication: [method/frequency]
- SMB procedures: [deployment method]

### Scenario 5: Equipment Failure
**Trigger:** [Specific failure - e.g., BC inflator failure]

**Immediate Actions:**
1. [Action 1 - e.g., Switch to backup inflation]
2. [Action 2 - e.g., Abort dive, team aware]
3. [Action 3 - e.g., Controlled ascent using fins]

**Backup Systems:**
- BC inflation: [method]
- Buoyancy control: [alternative]
- Gas supply: [redundancy]

## Emergency Gas Planning

### Gas Reserves Required
- Bottom Gas Reserve: [X] bar
- Deco Gas Reserve: [X] bar
- Oxygen Reserve: [X] bar
- **Total Reserve:** [X] bar

### Rock Bottom Calculations
- Depth: [X]m
- Ascent Time: [X] min
- Team Size: [X] divers
- SAC (stress): [X] L/min
- **Rock Bottom:** [X] bar

## Pre-Dive Emergency Checklist
- [ ] Emergency contacts verified and accessible
- [ ] Oxygen system functional (deco dives)
- [ ] First aid kit accessible
- [ ] Emergency signaling devices ready
- [ ] Team emergency procedures reviewed
- [ ] Nearest chamber location confirmed
- [ ] Transport options identified

## Post-Emergency Procedures

### If DCS Suspected
1. Administer 100% O₂ immediately
2. Keep patient calm and hydrated
3. Log dive profile and symptoms
4. Contact DAN/emergency services
5. Transport to chamber facility

### Incident Reporting
- DAN Incident Report: [filing process]
- Agency notification: [if applicable]
- Equipment inspection: [manufacturer]

## ⚠️ CRITICAL DISCLOSURE
> Emergency procedures must be practiced regularly. This plan
> does not replace formal emergency training. In a real emergency,
> prioritize safety over dive completion objectives.

## Evidence Sources
- [DAN Emergency Procedures]
- [Agency Emergency Guidelines]
- [Medical References]

---
*Emergency planning by technical-diving-decompression-training v1.0*
```

---

**Template Version:** 1.0  
**Purpose:** Standardized response templates for common analysis scenarios  
**Usage:** Agents should adapt these templates to specific user contexts while maintaining structure and completeness