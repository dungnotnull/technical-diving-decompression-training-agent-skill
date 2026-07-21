---
name: technical-diving-decompression-training
description: Technical Diving Training & Decompression Planning (Bühlmann Algorithm) — Professional-grade harness for Technical Diving Decompression Physiology & Safety analysis with evidence-backed outputs, real-time authoritative data, recognized domain methods, academic research integration, risk/limitation-disclosed recommendations, and self-improving knowledge pipeline. Use when user mentions technical diving, decompression planning, Bühlmann algorithm, dive training, gas planning, trimix diving, decompression sickness, DCS, dive safety, dive physiology, or asks for dive plan analysis, decompression profiles, gas mix selection, diving risk assessment.
compatibility: python>=3.11,claude-code>=1.0
version: 1.0.0
---

# SKILL Registry — Technical Diving Decompression Training

## Skill Registration

### Skill Identity

- **Name**: `technical-diving-decompression-training`
- **Version**: `1.0.0`
- **Registry ID**: `skill-188`
- **Category**: Domain Analysis & Decision Support
- **Domains**: Technical Diving, Decompression Physiology, Hyperbaric Medicine

### Registration Protocol

Skills are registered through the following mechanism:

1. **File-based Registration**: Skill files are placed in `skills/` directory with frontmatter metadata
2. **Metadata Extraction**: YAML frontmatter (`name`, `description`, `compatibility`, `version`) is parsed
3. **Skill Resolution**: Claude Code matches user queries to skill descriptions
4. **Skill Loading**: Full skill content loaded into context when triggered

### Skill Metadata Schema

```yaml
---
name: string              # Unique skill identifier (kebab-case)
description: string       # Natural language description (primary trigger mechanism)
compatibility: string      # Required dependencies (optional)
version: string           # Semantic version (MAJOR.MINOR.PATCH)
---
```

**Description Best Practices**:
- Be specific about what the skill does
- Include trigger contexts and use cases
- List domain-specific terms and synonyms
- Make it "pushy" enough to ensure reliable triggering
- Target ~100-150 words for optimal context

---

## Skill Resolution

### Resolution Algorithm

When a user submits a query, the resolution process:

```
1. Parse user input for intent and domain keywords
2. Compare against all available skill descriptions
3. Score each skill based on:
   - Keyword overlap (domain terms, synonyms)
   - Semantic similarity (intent matching)
   - Context relevance (project state, recent activity)
4. Select highest-scoring skill if score > threshold
5. Load skill SKILL.md into context
6. Execute skill workflow
```

### Resolution Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `threshold` | 0.6 | Minimum similarity score to trigger |
| `max_skills` | 3 | Maximum skills to consider |
| `context_weight` | 0.3 | Weight of project context in scoring |
| `keyword_weight` | 0.5 | Weight of keyword matching |
| `semantic_weight` | 0.2 | Weight of semantic similarity |

### Trigger Phrases

**Direct Triggers**:
- "technical diving decompression"
- "Bühlmann algorithm"
- "dive plan analysis"
- "decompression profile"
- "gas mix selection"
- "trimix diving"
- "DCS risk assessment"

**Contextual Triggers**:
- "plan a dive to [depth]"
- "calculate decompression for [profile]"
- "analyze diving safety for [scenario]"
- "design training progression for [diver]"
- "recommend gas mix for [dive]"

**Implicit Triggers** (detected via context):
- Depth + time + diving terminology
- Multiple gas mixtures mentioned
- Decompression stop calculations
- Technical diving certifications referenced

---

## Skill Execution

### Execution Model

The skill uses a **sequential harness execution model** with 6 discrete steps:

```
Step 1: sub-gather-requirements
  ↓ (gate: object confirmed)
Step 2: sub-evidence-collector
  ↓ (gate: data retrieved)
Step 3: sub-core-analysis
  ↓ (gate: decompression profile computed)
Step 4: sub-knowledge-updater
  ↓ (gate: evidence surfaced)
Step 5: sub-advisor
  ↓ (gate: conclusion category valid)
Step 6: main quality gate
  ↓ (all gates passed)
FINAL OUTPUT
```

### Execution Context

Each step operates with:
- **Input Context**: Output from previous step
- **Tool Access**: Defined set of allowed tools
- **Quality Gates**: Validation checkpoints
- **Error Recovery**: Degradation levels (0-4)
- **Retry Logic**: Max 2 attempts per gate

### Execution State Machine

```python
class ExecutionState(Enum):
    PENDING = "pending"           # Not yet started
    RUNNING = "running"           # Currently executing
    WAITING = "waiting"           # Awaiting user input
    FAILED = "failed"            # Step failed (max retries)
    COMPLETED = "completed"      # Step completed successfully
    SKIPPED = "skipped"           # Step skipped (degraded mode)
```

### Execution Parameters

```python
{
    "max_step_duration": 300,     # Maximum seconds per step
    "max_total_duration": 1800,   # Maximum seconds for full execution
    "max_retries_per_gate": 2,   # Retry attempts before failure
    "degradation_threshold": 2,  # Degradation level for warning
    "enable_parallel": false,    # Sequential execution only
}
```

---

## Skill Validation

### Input Validation Schema

All skill inputs conform to JSON Schema definitions:

#### Requirements Input Schema

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "object_of_analysis": {
            "type": "string",
            "description": "The dive scenario or profile to analyze"
        },
        "scope": {
            "type": "string",
            "enum": ["full", "decompression_only", "gas_only", "training_only"]
        },
        "timeframe": {
            "type": "string",
            "description": "Time constraints or dive date"
        },
        "available_inputs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "content": {"type": "string"}
                }
            }
        },
        "target_audience": {
            "type": "string",
            "enum": ["practitioner", "researcher", "decision_maker", "learner"]
        },
        "language": {
            "type": "string",
            "enum": ["en", "vi"],
            "default": "en"
        }
    },
    "required": ["object_of_analysis", "language"]
}
```

#### Diver Profile Schema

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "certification_level": {
            "type": "string",
            "enum": ["open_water", "advanced", "rescue", "divemaster",
                     "nitrox", "advanced_nitrox", "trimix", "ccr"]
        },
        "experience_dives": {
            "type": "integer",
            "minimum": 0
        },
        "max_depth_meters": {
            "type": "number",
            "minimum": 0,
            "maximum": 300
        },
        "fitness_level": {
            "type": "string",
            "enum": ["excellent", "good", "fair", "poor"]
        },
        "medical_considerations": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["certification_level", "experience_dives"]
}
```

#### Dive Objective Schema

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "depth_meters": {
            "type": "number",
            "minimum": 0,
            "maximum": 300
        },
        "bottom_time_minutes": {
            "type": "number",
            "minimum": 0,
            "maximum": 720
        },
        "environment": {
            "type": "string",
            "enum": ["ocean", "freshwater", "cave", "wreck", "ice"]
        },
        "temperature_celsius": {
            "type": "number",
            "minimum": -2,
            "maximum": 40
        },
        "altitude_meters": {
            "type": "number",
            "minimum": 0,
            "maximum": 5000
        }
    },
    "required": ["depth_meters", "bottom_time_minutes"]
}
```

### Output Validation Schema

#### Final Report Schema

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "report_metadata": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date"},
                "version": {"type": "string"},
                "language": {"type": "string"},
                "domain": {"type": "string"}
            },
            "required": ["date", "version", "language", "domain"]
        },
        "executive_summary": {
            "type": "string",
            "minLength": 50,
            "maxLength": 500
        },
        "inputs_and_scope": {"type": "object"},
        "evidence_collected": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "source": {"type": "string"},
                    "tier": {"type": "string", "enum": ["1", "2", "3", "4"]},
                    "content": {"type": "string"},
                    "date": {"type": "string"}
                }
            }
        },
        "analysis": {"type": "object"},
        "action_plan": {"type": "object"},
        "academic_evidence": {
            "type": "array",
            "minItems": 3,
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "authors": {"type": "array"},
                    "year": {"type": "integer"},
                    "venue": {"type": "string"},
                    "doi_url": {"type": "string"},
                    "tier": {"type": "string"}
                }
            }
        },
        "disclosure": {
            "type": "string",
            "minLength": 100
        },
        "conclusion": {
            "type": "object",
            "properties": {
                "verdict": {
                    "type": "string",
                    "enum": ["Safe", "Conservative Plan", "Conditional",
                            "High Risk", "Revise", "Inconclusive"]
                },
                "scenarios": {"type": "array"},
                "key_risks": {"type": "array"},
                "evidence_chain": {"type": "array"},
                "remediation": {"type": "array"}
            },
            "required": ["verdict"]
        },
        "gate_checklist": {
            "type": "object",
            "properties": {
                "universal_gates": {"type": "array"},
                "domain_gates": {"type": "array"},
                "limitations": {"type": "array"}
            }
        }
    },
    "required": [
        "report_metadata",
        "executive_summary",
        "inputs_and_scope",
        "evidence_collected",
        "analysis",
        "academic_evidence",
        "disclosure",
        "conclusion",
        "gate_checklist"
    ]
}
```

### Quality Gate Validation

Each quality gate implements:

```python
def validate_gate(gate_id: str, context: dict) -> ValidationResult:
    """
    Validate a quality gate against execution context

    Args:
        gate_id: Gate identifier (U1-U6, G1-G4)
        context: Current execution context

    Returns:
        ValidationResult with pass/fail and auto-fix procedure
    """
    result = ValidationResult(
        gate_id=gate_id,
        passed=False,
        auto_fix_available=False,
        errors=[],
        warnings=[]
    )

    # Gate-specific validation logic
    if gate_id == "U1":
        # Validate source count
        sources = context.get('sources', [])
        if len(sources) < 3:
            result.errors.append("Minimum 3 sources required")
            result.auto_fix_available = True
        else:
            result.passed = True

    # ... (similar logic for other gates)

    return result
```

---

## Sub-Skill Registry

### Sub-Skill Registration

Each sub-skill is registered with:

```yaml
---
name: sub-{subskill-name}
description: One-line summary of purpose
version: 1.0.0
---
```

### Available Sub-Skills

| Sub-Skill | Purpose | Input Schema | Output Schema |
|-----------|---------|--------------|---------------|
| `sub-gather-requirements` | Clarify analysis parameters | User query | Requirements object |
| `sub-evidence-collector` | Fetch authoritative data | Requirements | Evidence bundle |
| `sub-core-analysis` | Compute decompression profile | Diver profile + objective | Decompression plan |
| `sub-knowledge-updater` | Query knowledge base | Analysis topics | Academic evidence |
| `sub-advisor` | Synthesize recommendations | All previous outputs | Final conclusion |

### Sub-Skill Execution Protocol

```python
class SubSkillExecutor:
    def execute_subskill(
        self,
        skill_name: str,
        input_context: dict,
        timeout: int = 300
    ) -> SubSkillResult:
        """
        Execute a sub-skill with input context

        Args:
            skill_name: Name of sub-skill to execute
            input_context: Input data for sub-skill
            timeout: Maximum execution time in seconds

        Returns:
            SubSkillResult with output and validation status
        """
        # Load sub-skill definition
        skill_def = self.load_subskill(skill_name)

        # Validate input against schema
        validation_errors = self.validate_input(
            input_context,
            skill_def.input_schema
        )
        if validation_errors:
            raise InputValidationError(validation_errors)

        # Execute sub-skill
        output = self.run_skill_workflow(skill_def, input_context)

        # Validate output against schema
        output_errors = self.validate_output(
            output,
            skill_def.output_schema
        )
        if output_errors:
            raise OutputValidationError(output_errors)

        return SubSkillResult(
            skill_name=skill_name,
            output=output,
            passed_internal_gate=True,
            execution_time=self.elapsed_time
        )
```

---

## Tool Registry

### Available Tools

| Tool | Purpose | Permission Required | Rate Limit |
|------|---------|-------------------|------------|
| `WebSearch` | Search domain sources | network | 10 req/min |
| `WebFetch` | Fetch authoritative docs | network | 20 req/min |
| `Read` | Read local files | filesystem | unlimited |
| `Write` | Write local files | filesystem | unlimited |
| `Bash` | Execute system commands | shell | restricted |
| `Skill` | Invoke sub-skills | skill | unlimited |

### Tool Execution Wrapper

```python
class ToolExecutor:
    def execute_tool(
        self,
        tool_name: str,
        parameters: dict,
        timeout: int = 30
    ) -> ToolResult:
        """
        Execute a tool with parameters and timeout

        Handles:
        - Permission checks
        - Rate limiting
        - Error recovery
        - Result validation
        """
        # Check permissions
        if not self.check_permission(tool_name):
            raise PermissionError(f"No permission for tool: {tool_name}")

        # Check rate limits
        if not self.check_rate_limit(tool_name):
            raise RateLimitError(f"Rate limit exceeded for: {tool_name}")

        # Execute with timeout
        try:
            result = self.execute_with_timeout(
                tool_name,
                parameters,
                timeout
            )
        except TimeoutError:
            raise ToolExecutionTimeout(f"Tool {tool_name} timed out")

        # Validate result
        if not self.validate_result(result):
            raise ToolResultError(f"Invalid result from {tool_name}")

        return result
```

---

## Error Handling & Recovery

### Error Classification

```python
class ErrorType(Enum):
    TIMEOUT = "timeout"              # Request timeout
    INVALID_INPUT = "invalid_input"  # Schema validation failure
    MISSING_INPUT = "missing_input"  # Required field absent
    STALE_DATA = "stale_data"        # Outdated information
    KNOWLEDGE_MISS = "knowledge_miss"  # No KB matches
    CONFLICTING_ACTIONS = "conflicting_actions"  # Mutually exclusive
    ENVELOPE_UNAVAILABLE = "envelope_unavailable"  # No setpoint
    OBJECT_AMBIGUOUS = "object_ambiguous"  # Classification unclear
```

### Recovery Strategies

```python
RECOVERY_STRATEGIES = {
    ErrorType.TIMEOUT: {
        "max_retries": 3,
        "backoff": "exponential",
        "alternate_source": True
    },
    ErrorType.INVALID_INPUT: {
        "max_retries": 2,
        "action": "request_confirmation"
    },
    ErrorType.STALE_DATA: {
        "max_retries": 1,
        "action": "flag_and_proceed"
    },
    ErrorType.KNOWLEDGE_MISS: {
        "max_retries": 2,
        "action": "websearch_gap_fill"
    }
}
```

### Degradation Levels

```python
class DegradationLevel(Enum):
    FULL = 0      # All sources available
    PARTIAL = 1  # Some sources failed, using alternatives
    HISTORICAL = 2  # Using KB only, flagging as historical
    MISSING_DATA = 3  # Variables missing, marking unavailable
    UNAVAILABLE = 4  # All sources failed, cannot proceed
```

---

## Performance & Monitoring

### Execution Metrics

```python
class ExecutionMetrics:
    duration_ms: int
    total_tokens: int
    tool_calls: Dict[str, int]
    gate_passes: int
    gate_failures: int
    degradation_level: int
    retry_count: int
```

### Monitoring Endpoints

```python
# Metrics collection
@dataclass
class MetricsCollector:
    execution_count: int = 0
    success_count: int = 0
    failure_count: int = 0
    average_duration_ms: float = 0.0
    average_tokens: int = 0
    gate_pass_rates: Dict[str, float] = field(default_factory=dict)
    tool_usage: Dict[str, int] = field(default_factory=dict)

    def record_execution(self, metrics: ExecutionMetrics):
        """Record execution metrics"""
        self.execution_count += 1
        if metrics.gate_failures == 0:
            self.success_count += 1
        else:
            self.failure_count += 1
        # ... update other metrics
```

---

## Extension Points

### Custom Decompression Models

Additional decompression models can be registered:

```python
class DecompressionModel(ABC):
    @abstractmethod
    def compute_profile(
        self,
        depth: float,
        bottom_time: float,
        gas_mix: GasMix
    ) -> DecompressionProfile:
        pass

# Register custom model
register_model("VPM-B", VPMBModel())
register_model("RGBM", RGBMModel())
```

### Custom Evidence Sources

Additional evidence sources can be added:

```python
class EvidenceSource(ABC):
    @abstractmethod
    def fetch(self, query: str) -> List[Evidence]:
        pass

# Register custom source
register_source("custom_database", CustomDatabaseSource())
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-07-10 | Initial production release |
| | | Full 8-File Contract compliance |
| | | All 6 phases complete |
| | | Production-grade quality gates |
| | | Self-improving knowledge pipeline |

---

## References

- `PROJECT-detail.md` — Full technical specification
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — Build roadmap
- `CLAUDE.md` — Project identity and harness flow
- `SECOND-KNOWLEDGE-BRAIN.md` — Knowledge base
- `config/` — Configuration management
- `skills/` — Sub-skill implementations
- `tools/` — Python utilities and scripts
