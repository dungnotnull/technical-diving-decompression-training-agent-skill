# Data Schemas and Validation

## Schema Definitions

### Diver Profile Schema

```yaml
DiverProfile:
  type: object
  required:
    - certification_level
    - experience_dives
  properties:
    certification_level:
      type: string
      enum: [open_water, advanced, rescue, divemaster, nitrox, advanced_nitrox, trimix, ccr]
      description: Highest diving certification held
    experience_dives:
      type: integer
      minimum: 0
      description: Total number of dives completed
    max_depth_meters:
      type: number
      minimum: 0
      maximum: 300
      description: Deepest depth ever dived
    fitness_level:
      type: string
      enum: [excellent, good, fair, poor]
      description: Current physical fitness assessment
    medical_considerations:
      type: array
      items:
        type: string
      description: List of medical conditions or medications
    age:
      type: integer
      minimum: 12
      maximum: 80
      description: Diver age in years
    bmi:
      type: number
      minimum: 15
      maximum: 40
      description: Body mass index
    pfo_status:
      type: string
      enum: [unknown, negative, positive]
      description: Patent foramen ovale screening status
```

### Dive Objective Schema

```yaml
DiveObjective:
  type: object
  required:
    - depth_meters
    - bottom_time_minutes
  properties:
    depth_meters:
      type: number
      minimum: 0
      maximum: 300
      description: Maximum planned depth in meters
    bottom_time_minutes:
      type: number
      minimum: 0
      maximum: 720
      description: Planned bottom time in minutes
    environment:
      type: string
      enum: [ocean, freshwater, cave, wreck, ice]
      description: Diving environment type
    temperature_celsius:
      type: number
      minimum: -2
      maximum: 40
      description: Water temperature in Celsius
    altitude_meters:
      type: number
      minimum: 0
      maximum: 5000
      description: Altitude of dive site in meters
    mission_type:
      type: string
      enum: [recreational, training, exploration, survey, photography, scientific]
      description: Purpose of the dive
    team_size:
      type: integer
      minimum: 1
      maximum: 8
      description: Number of divers in team
```

### Gas Mix Schema

```yaml
GasMix:
  type: object
  required:
    - oxygen_percent
    - helium_percent
    - nitrogen_percent
  properties:
    oxygen_percent:
      type: number
      minimum: 10
      maximum: 100
      description: Percentage of oxygen in gas mix
    helium_percent:
      type: number
      minimum: 0
      maximum: 90
      description: Percentage of helium in gas mix
    nitrogen_percent:
      type: number
      minimum: 0
      maximum: 100
      description: Percentage of nitrogen in gas mix (calculated if not provided)
    name:
      type: string
      pattern: '^Tx\d{1,2}/\d{1,2}$'
      description: Standard trimix notation (e.g., Tx21/35)
    purpose:
      type: string
      enum: [bottom, travel, deco, oxygen]
      description: Intended use of the gas mix
```

### Decompression Profile Schema

```yaml
DecompressionProfile:
  type: object
  required:
    - model
    - gradient_factor_low
    - gradient_factor_high
    - stops
  properties:
    model:
      type: string
      enum: [Bühlmann ZHL-16C, VPM-B, RGBM]
      description: Decompression algorithm used
    gradient_factor_low:
      type: integer
      minimum: 0
      maximum: 100
      description: Low gradient factor for deep stops
    gradient_factor_high:
      type: integer
      minimum: 0
      maximum: 100
      description: High gradient factor for shallow stops
    leading_compartment:
      type: integer
      minimum: 1
      maximum: 16
      description: Tissue compartment controlling deco ceiling
    stops:
      type: array
      items:
        type: object
        required: [depth_meters, time_minutes]
        properties:
          depth_meters:
            type: number
            minimum: 3
            maximum: 90
            description: Stop depth in meters
          time_minutes:
            type: number
            minimum: 0
            maximum: 720
            description: Stop time in minutes
          gas_switch:
            type: string
            description: Gas to switch to at this stop
    total_run_time:
      type: number
      description: Total dive time in minutes
    total_deco_time:
      type: number
      description: Total decompression time in minutes
```

### Evidence Entry Schema

```yaml
EvidenceEntry:
  type: object
  required:
    - title
    - source
    - tier
    - content
    - date
  properties:
    title:
      type: string
      description: Title of the evidence source
    authors:
      type: array
      items:
        type: string
      description: List of authors
    year:
      type: integer
      minimum: 1900
      maximum: 2100
      description: Publication year
    venue:
      type: string
      description: Publication venue or journal name
    doi_or_url:
      type: string
      format: uri
      description: DOI or URL of the source
    tier:
      type: string
      enum: ["1", "2", "3", "4"]
      description: Evidence hierarchy tier
    content:
      type: string
      description: Summary or key findings
    date:
      type: string
      format: date
      description: Date the evidence was accessed or published
    relevance_score:
      type: number
      minimum: 0
      maximum: 10
      description: Relevance score for the current query
```

### Analysis Report Schema

```yaml
AnalysisReport:
  type: object
  required:
    - report_metadata
    - executive_summary
    - inputs_and_scope
    - evidence_collected
    - analysis
    - academic_evidence
    - disclosure
    - conclusion
    - gate_checklist
  properties:
    report_metadata:
      type: object
      required: [date, version, language, domain]
      properties:
        date:
          type: string
          format: date
        version:
          type: string
          pattern: '^\d+\.\d+\.\d+$'
        language:
          type: string
          enum: [en, vi]
        domain:
          type: string
    executive_summary:
      type: string
      minLength: 50
      maxLength: 500
    inputs_and_scope:
      type: object
    evidence_collected:
      type: array
      items:
        $ref: '#/EvidenceEntry'
      minItems: 1
    analysis:
      type: object
      properties:
        decompression_profile:
          $ref: '#/DecompressionProfile'
        gas_mix:
          $ref: '#/GasMix'
        risk_assessment:
          type: object
        calculations:
          type: object
    academic_evidence:
      type: array
      items:
        $ref: '#/EvidenceEntry'
      minItems: 3
    disclosure:
      type: string
      minLength: 100
    conclusion:
      type: object
      required: [verdict]
      properties:
        verdict:
          type: string
          enum: [Safe, Conservative Plan, Conditional, High Risk, Revise, Inconclusive]
        scenarios:
          type: array
          items:
            type: object
        key_risks:
          type: array
          items:
            type: string
        evidence_chain:
          type: array
          items:
            type: string
        remediation:
          type: array
          items:
            type: string
    gate_checklist:
      type: object
      properties:
        universal_gates:
          type: array
          items:
            type: string
        domain_gates:
          type: array
          items:
            type: string
        limitations:
          type: array
          items:
            type: string
```

## Validation Functions

### Gas Mix Validation

```python
def validate_gas_mix(mix: dict) -> dict:
    """Validate gas mix composition"""
    errors = []

    # Check percentages sum to 100
    total = mix.get('oxygen_percent', 0) + \
            mix.get('helium_percent', 0) + \
            mix.get('nitrogen_percent', 0)

    if abs(total - 100.0) > 1.0:
        errors.append(f"Gas percentages sum to {total}%, not 100%")

    # Validate MOD
    if mix.get('oxygen_percent', 0) < 10:
        errors.append("O₂ percentage too low (<10%)")

    # Validate helium limits
    if mix.get('helium_percent', 0) > 90:
        errors.append("He percentage too high (>90%)")

    # Calculate and validate END
    # Calculate and validate density

    return {'valid': len(errors) == 0, 'errors': errors}
```

### Decompression Profile Validation

```python
def validate_decompression_profile(profile: dict) -> dict:
    """Validate decompression profile"""
    errors = []

    # Check model is specified
    if 'model' not in profile:
        errors.append("Decompression model not specified")

    # Validate gradient factors
    gf_low = profile.get('gradient_factor_low', 0)
    gf_high = profile.get('gradient_factor_high', 0)

    if gf_low >= gf_high:
        errors.append("GF Low must be less than GF High")

    if not (0 <= gf_low <= 100 and 0 <= gf_high <= 100):
        errors.append("Gradient factors must be 0-100")

    # Validate stops
    if 'stops' in profile:
        for i, stop in enumerate(profile['stops']):
            if stop.get('depth_meters', 0) < 3:
                errors.append(f"Stop {i}: depth < 3m")

            if stop.get('time_minutes', 0) < 0:
                errors.append(f"Stop {i}: negative time")

    return {'valid': len(errors) == 0, 'errors': errors}
```

### Evidence Validation

```python
def validate_evidence(entry: dict) -> dict:
    """Validate evidence entry"""
    errors = []

    # Check required fields
    required = ['title', 'source', 'tier', 'content', 'date']
    for field in required:
        if field not in entry:
            errors.append(f"Missing required field: {field}")

    # Validate tier
    if 'tier' in entry:
        if entry['tier'] not in ['1', '2', '3', '4']:
            errors.append(f"Invalid tier: {entry['tier']}")

    # Validate relevance score
    if 'relevance_score' in entry:
        score = entry['relevance_score']
        if not (0 <= score <= 10):
            errors.append(f"Relevance score out of range: {score}")

    return {'valid': len(errors) == 0, 'errors': errors}
```

## JSON Schema Examples

### Complete Dive Analysis Request

```json
{
  "type": "dive_analysis_request",
  "diver_profile": {
    "certification_level": "trimix",
    "experience_dives": 250,
    "max_depth_meters": 80,
    "fitness_level": "good",
    "age": 35,
    "pfo_status": "negative"
  },
  "dive_objective": {
    "depth_meters": 60,
    "bottom_time_minutes": 30,
    "environment": "ocean",
    "temperature_celsius": 18,
    "altitude_meters": 0,
    "mission_type": "exploration",
    "team_size": 3
  },
  "gas_mixes": [
    {
      "name": "Tx18/45",
      "oxygen_percent": 18,
      "helium_percent": 45,
      "nitrogen_percent": 37,
      "purpose": "bottom"
    },
    {
      "name": "EAN50",
      "oxygen_percent": 50,
      "helium_percent": 0,
      "nitrogen_percent": 50,
      "purpose": "deco"
    }
  ],
  "analysis_options": {
    "decompression_model": "Bühlmann ZHL-16C",
    "gradient_factor_low": 30,
    "gradient_factor_high": 85,
    "include_emergency_planning": true,
    "language": "en"
  }
}
```

### Complete Analysis Response

```json
{
  "type": "dive_analysis_response",
  "report_metadata": {
    "date": "2026-07-10",
    "version": "1.0.0",
    "language": "en",
    "domain": "technical_diving_decompression_training"
  },
  "executive_summary": "Dive profile is within acceptable safety parameters. Conservative plan recommended due to depth.",
  "inputs_and_scope": {
    "depth_range": "60-6m",
    "total_run_time": "112 minutes",
    "environment": "ocean, 18°C"
  },
  "evidence_collected": [
    {
      "title": "Bühlmann decompression model",
      "source": "SECOND-KNOWLEDGE-BRAIN.md",
      "tier": "2",
      "content": "ZHL-16C model with 16 tissue compartments..."
    }
  ],
  "analysis": {
    "gas_mix_validation": {
      "tx18_45": {
        "mod": "87m (1.4 bar)",
        "end": "33m",
        "density": "5.8 g/L",
        "status": "PASS"
      }
    },
    "decompression_profile": {
      "model": "Bühlmann ZHL-16C",
      "gradient_factor_low": 30,
      "gradient_factor_high": 85,
      "leading_compartment": 10,
      "stops": [
        {"depth_meters": 21, "time_minutes": 2, "gas_switch": "EAN50"},
        {"depth_meters": 15, "time_minutes": 4},
        {"depth_meters": 12, "time_minutes": 8},
        {"depth_meters": 9, "time_minutes": 15},
        {"depth_meters": 6, "time_minutes": 23},
        {"depth_meters": 3, "time_minutes": 30}
      ],
      "total_run_time": 112,
      "total_deco_time": 82
    },
    "oxygen_exposure": {
      "cns_percent": 54,
      "otu": 185,
      "status": "PASS"
    },
    "gas_requirements": {
      "bottom_gas": "210 bar",
      "deco_gas": "120 bar",
      "reserve": "150 bar"
    }
  },
  "academic_evidence": [
    {
      "title": "Gradient factors for decompression",
      "authors": ["Erik C. Baker"],
      "year": 1998,
      "venue": "Sources",
      "doi_or_url": "http://www.decompression.org/algorithm/gradient_factors.htm",
      "tier": "2"
    }
  ],
  "disclosure": "This analysis is based on theoretical models and does not guarantee...",
  "conclusion": {
    "verdict": "Conservative Plan",
    "scenarios": [
      {"name": "Best", "description": "All parameters nominal, reduced deco time"},
      {"name": "Base", "description": "As calculated above"},
      {"name": "Worst", "description": "High exertion, cold water, extended deco"}
    ],
    "key_risks": [
      "Decompression sickness risk: MODERATE",
      "Oxygen toxicity risk: LOW",
      "Narcosis risk: LOW (controlled by helium)"
    ],
    "evidence_chain": [
      "Bühlmann ZHL-16C model → Tissue loading calculation",
      "Gradient factors → Conservatism adjustment",
      "Gas physics → MOD/END/Density validation"
    ],
    "remediation": [
      "Add 3-minute safety stop at 6m",
      "Consider GF 20/80 for additional conservatism",
      "Monitor CNS% closely during deco"
    ]
  },
  "gate_checklist": {
    "universal_gates": ["U1✓", "U2✓", "U3✓", "U4✓", "U5✓", "U6✓"],
    "domain_gates": ["G1✓", "G2✓", "G3✓", "G4✓"],
    "limitations": []
  }
}
```

---

**Document Version:** 1.0  
**Last Updated:** 2026-07-10  
**Purpose:** Data schemas for validation and type safety