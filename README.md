# technical-diving-decompression-training

**Technical Diving Training & Decompression Planning (Bühlmann Algorithm)**

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Version 1.0.1](https://img.shields.io/badge/version-1.0.1--enhanced-brightgreen.svg)](https://github.com/)

A **production-grade** Claude Code harness for **Technical Diving Decompression Physiology & Safety** — gathers real-time authoritative data, applies recognized domain methods, integrates academic research, and delivers evidence-backed, risk-disclosed outputs with **zero placeholder code**.

## Features

### Core Capabilities
- Real-time data aggregation from authoritative Technical Diving Decompression Physiology & Safety sources
- Systematic domain analysis methods using Bühlmann ZHL-16C algorithm
- Academic research integration with auto-updating knowledge base
- Risk/limitation-disclosed outputs with scenario coverage
- Self-improving knowledge pipeline (weekly crawl)

### Enhanced Features (v1.0.1)
- **Flexible Agent & Skill Architecture:** Modular design for easy extension
- **Type-safe Configuration:** Production-grade config with environment variable support
- **Structured Logging:** Comprehensive logging with degradation tracking
- **Error Recovery:** Graceful degradation with 5 levels (0-4)
- **Quality Gates:** 10 gates (U1-U6 universal + G1-G4 domain) with auto-fix
- **Evidence Hierarchy:** Tier 1-4 source classification with validation

### Modular Structure
```
├── config/           # Type-safe configuration management
├── scripts/          # Automation and initialization tools
├── references/       # Domain documentation and prompt templates
├── assets/          # System diagrams and data schemas
├── skills/          # Main harness and sub-skills
├── tools/           # Knowledge pipeline and validation
├── tests/           # Test scenarios and results
└── SECOND-KNOWLEDGE-BRAIN.md  # Self-updating knowledge base
```

## Installation

### Quick Start
```bash
# Clone or download the project
cd 188-technical-diving-decompression-training

# Run initialization script
python scripts/initialize_project.py

# Seed knowledge base with foundational entries
python scripts/seed_knowledge_base.py

# Install dependencies
pip install -r requirements.txt
```

### Manual Installation
```bash
pip install -r requirements.txt
```
Install skill files to `~/.claude/skills/` or use via project CLAUDE.md.

## Usage

### Basic Usage
```bash
/technical-diving-decompression-training [your query]
```

### Example Queries
- "Plan a 60m dive for 30 minutes on trimix"
- "Analyze DCS risk for this dive profile"
- "Recommend gas mix for 45m wreck dive"
- "Calculate decompression for 70m, 25min bottom time"

### Configuration
Set environment variables or edit `config/config.json`:
```bash
export TECHDIVE_ENV=production
export TECHDIVE_DEBUG=false
export TECHDIVE_GF_LOW=30
export TECHDIVE_GF_HIGH=85
```

## Architecture
Harness flow: requirements → evidence → core analysis → knowledge → synthesis → quality gate.
See `PROJECT-detail.md` for the full architecture diagram.

## Quality Gates
Universal gates U1–U6 plus domain gates defined in `skills/main.md`.

## Data Sources
- DAN (Divers Alert Network) — diversalertnetwork.org (DCS research)
- US Navy Diving Manual
- BSAC / NAUI / TDI training standards
- NOAA Diving Program
- WorkSafe/UK HSE diving standards
- Büllmann decompression model references (UWATEC/Trimix)
- Hyperbaric medical references (UHMS)
- ISO 24803 recreational diving safety

## Testing
```bash
python tools/test_knowledge_updater.py
python tools/run_test_scenarios.py --all
```

## Knowledge Base
`SECOND-KNOWLEDGE-BRAIN.md` is auto-updated weekly via `tools/knowledge_updater.py`.

## Roadmap
- [x] Phase 0: Architecture
- [x] Phase 1: Core sub-skills
- [x] Phase 2: Main harness + gates
- [x] Phase 3: Knowledge pipeline
- [x] Phase 4: Testing
- [x] Phase 5: Integration & polish
- [x] **Enhanced: Modular architecture & production-grade code**
- [x] **Enhanced: Type-safe configuration management**
- [x] **Enhanced: Comprehensive documentation & diagrams**

## Version History
| Version | Date | Changes |
|---------|------|---------|
| 1.0.1 | 2026-07-20 | **Enhanced Architecture:** Modular structure, type-safe config, production-grade code quality, comprehensive documentation |
| 1.0.0 | 2026-07-10 | Initial production release with full 8-File Contract compliance |

## License
MIT — see LICENSE.

## Citation
```bibtex
@software{technical-diving-decompression-training,
  title = {technical-diving-decompression-training: Technical Diving Training & Decompression Planning (Bühlmann Algorithm)},
  year = {2026},
  version = {1.0.0}
}
```


## Why This Skill

Technical Diving Decompression Physiology & Safety practitioners face fragmented data, inconsistent methodology, and tools
that do not self-improve. This skill unifies authoritative real-time data, recognized
domain methods, and a continuously-updated academic knowledge base into one
evidence-backed, risk-disclosed workflow.

## Roadmap

- [x] Phase 0: Architecture
- [x] Phase 1: Core sub-skills (5)
- [x] Phase 2: Main harness + gates
- [x] Phase 3: Knowledge pipeline
- [x] Phase 4: Testing
- [x] Phase 5: Integration & polish â€” PRODUCTION READY v1.0.0
