"""
Configuration Module for Technical Diving Decompression Training Skill
Provides type-safe, validated configuration with environment variable support
"""

from config.config_schema import (
    SystemConfig,
    KnowledgeConfig,
    LLMConfig,
    DecompressionConfig,
    QualityGateConfig,
    FeatureFlags,
    APIConfig,
    LoggingConfig,
    MonitoringConfig,
    ValidationConfig,
    LogLevel,
    Environment,
)

from config.config_loader import (
    load_config,
    get_config,
    reload_config,
    save_default_config,
    ConfigurationError,
)

__all__ = [
    # Schema
    'SystemConfig',
    'KnowledgeConfig',
    'LLMConfig',
    'DecompressionConfig',
    'QualityGateConfig',
    'FeatureFlags',
    'APIConfig',
    'LoggingConfig',
    'MonitoringConfig',
    'ValidationConfig',
    'LogLevel',
    'Environment',
    # Loader
    'load_config',
    'get_config',
    'reload_config',
    'save_default_config',
    'ConfigurationError',
]
