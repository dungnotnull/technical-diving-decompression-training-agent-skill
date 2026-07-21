"""
Configuration Schema Definition for Technical Diving Decompression Training Skill
Defines all configuration parameters with types, defaults, and validation rules
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum


class LogLevel(str, Enum):
    """Logging levels for the application"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Environment(str, Enum):
    """Deployment environments"""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


@dataclass
class KnowledgeConfig:
    """Knowledge pipeline configuration"""
    domain: str = "Technical Diving Decompression Physiology & Safety"
    keywords: List[str] = field(default_factory=lambda: [
        "technical diving decompression",
        "Buhlmann ZHL-16 gradient factor",
        "trimix oxygen toxicity narcosis",
        "DCS decompression sickness",
        "gas planning rule of thirds",
        "deep diving fitness to dive"
    ])
    arxiv_categories: List[str] = field(default_factory=list)
    semantic_scholar_base: str = "https://api.semanticscholar.org/graph/v1/paper/search"
    rss_feeds: List[str] = field(default_factory=list)
    authoritative_docs: List[str] = field(default_factory=lambda: [
        "Undersea & Hyperbaric Medicine — UHMS",
        "Diving and Hyperbaric Medicine — SPUMS",
        "European Journal of Applied Physiology — Springer",
        "Journal of Applied Physiology — APS",
        "Aviation, Space, and Environmental Medicine — Aerospace Med. Assoc.",
        "Frontiers in Physiology",
        "Wilderness & Environmental Medicine — Elsevier"
    ])
    scoring_weights: Dict[str, float] = field(default_factory=lambda: {
        "recency": 0.4,
        "keyword_relevance": 0.4,
        "citation_count": 0.2
    })
    max_results_per_source: int = 10
    max_new_entries_per_run: int = 20
    crawl_timeout_seconds: int = 30
    dedup_algorithm: str = "SHA256"


@dataclass
class LLMConfig:
    """LLM model configuration"""
    model_name: str = "claude-3-5-sonnet-20241022"
    max_tokens: int = 8192
    temperature: float = 0.7
    top_p: float = 0.95
    top_k: int = 40
    timeout_seconds: int = 120
    max_retries: int = 3
    retry_delay_seconds: float = 2.0
    enable_cache: bool = True
    cache_ttl_seconds: int = 3600


@dataclass
class DecompressionConfig:
    """Decompression calculation parameters"""
    model: str = "Bühlmann ZHL-16C"
    gradient_factor_low: int = 30
    gradient_factor_high: int = 85
    tissue_compartments: int = 16
    half_time_range: Tuple[int, int] = (4, 635)
    m_value_precision: float = 0.01

    # Oxygen toxicity limits
    max_po2_working: float = 1.4
    max_po2_decompression: float = 1.6
    cns toxicity_limit_percent: int = 80
    otu_limit: int = 300

    # Gas density limits
    max_gas_density_grams_per_liter: float = 6.2  # EN14143 standard
    max_work_of_breathing_limit: float = 2.0

    # Narcosis limits
    max_end_meters: int = 40


@dataclass
class QualityGateConfig:
    """Quality gate thresholds and enforcement"""
    min_sources_required: int = 3
    min_academic_sources: int = 1
    max_retry_attempts: int = 2
    enable_auto_fix: bool = True
    strict_mode: bool = False
    evidence_hierarchy_levels: int = 4


@dataclass
class FeatureFlags:
    """Feature toggles for experimental or conditional features"""
    enable_probabilistic_dcs: bool = False
    enable_vpm_alternative_model: bool = False
    enable_rgbm_model: bool = False
    enable_cns_otu_tracking: bool = True
    enable_gas_density_validation: bool = True
    enable_pfo_screening_recommendation: bool = True
    enable_fitness_validation: bool = True
    enable_multigas_optimization: bool = True
    enable_decompression_comparison: bool = True
    enable_emergency_procedures_generation: bool = True


@dataclass
class APIConfig:
    """External API configuration"""
    requests_timeout: int = 30
    max_concurrent_requests: int = 5
    rate_limit_delay: float = 1.0
    user_agent: str = "technical-diving-skill/1.0"
    enable_proxy: bool = False
    proxy_url: Optional[str] = None
    verify_ssl: bool = True


@dataclass
class LoggingConfig:
    """Logging configuration"""
    level: LogLevel = LogLevel.INFO
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format: str = "%Y-%m-%d %H:%M:%S"
    file_enabled: bool = True
    file_path: str = "logs/technical_diving_skill.log"
    max_file_size_mb: int = 10
    backup_count: int = 5
    console_enabled: bool = True
    structured_logging: bool = True


@dataclass
class MonitoringConfig:
    """Monitoring and metrics configuration"""
    enable_metrics: bool = True
    metrics_port: int = 9090
    enable_tracing: bool = False
    trace_exporter: str = "stdout"
    performance_tracking: bool = True
    error_tracking: bool = True


@dataclass
class ValidationConfig:
    """Input validation and safety limits"""
    max_depth_meters: int = 300
    max_bottom_time_minutes: int = 720
    min_oxygen_percent: int = 10
    max_oxygen_percent: int = 100
    min_helium_percent: int = 0
    max_helium_percent: int = 90
    min_nitrogen_percent: int = 0
    max_nitrogen_percent: int = 100
    gas_sum_tolerance: float = 1.0


@dataclass
class SystemConfig:
    """Root configuration container"""
    environment: Environment = Environment.PRODUCTION
    debug: bool = False

    knowledge: KnowledgeConfig = field(default_factory=KnowledgeConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    decompression: DecompressionConfig = field(default_factory=DecompressionConfig)
    quality_gates: QualityGateConfig = field(default_factory=QualityGateConfig)
    features: FeatureFlags = field(default_factory=FeatureFlags)
    api: APIConfig = field(default_factory=APIConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    monitoring: MonitoringConfig = field(default_factory=MonitoringConfig)
    validation: ValidationConfig = field(default_factory=ValidationConfig)

    def validate(self) -> List[str]:
        """Validate configuration and return list of errors"""
        errors = []

        # Validate gas percentages
        gas_config = self.validation
        if gas_config.min_oxygen_percent < 0 or gas_config.max_oxygen_percent > 100:
            errors.append("Invalid oxygen percentage range")
        if gas_config.min_helium_percent < 0 or gas_config.max_helium_percent > 100:
            errors.append("Invalid helium percentage range")

        # Validate decompression limits
        decomp_config = self.decompression
        if decomp_config.gradient_factor_low < 0 or decomp_config.gradient_factor_high > 100:
            errors.append("Gradient factors must be between 0-100")
        if decomp_config.gradient_factor_low >= decomp_config.gradient_factor_high:
            errors.append("Gradient factor low must be less than high")

        # Validate knowledge config
        if self.knowledge.max_results_per_source < 0:
            errors.append("Max results must be positive")

        return errors
