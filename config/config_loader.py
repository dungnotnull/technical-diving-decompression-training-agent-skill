"""
Configuration Loader with Environment Variable Support
Provides type-safe configuration loading with environment variable overrides
"""

import os
import json
from pathlib import Path
from typing import TypeVar, Type, Optional, Any
from functools import lru_cache

from config.config_schema import SystemConfig, Environment, LogLevel


T = TypeVar('T', bound=SystemConfig)


class ConfigurationError(Exception):
    """Raised when configuration is invalid or missing"""
    pass


def get_env_bool(key: str, default: bool = False) -> bool:
    """Get boolean from environment variable"""
    value = os.getenv(key, str(default)).lower()
    return value in ('true', '1', 'yes', 'on')


def get_env_int(key: str, default: int) -> int:
    """Get integer from environment variable"""
    try:
        return int(os.getenv(key, str(default)))
    except ValueError:
        return default


def get_env_float(key: str, default: float) -> float:
    """Get float from environment variable"""
    try:
        return float(os.getenv(key, str(default)))
    except ValueError:
        return default


def get_env_str(key: str, default: str) -> str:
    """Get string from environment variable"""
    return os.getenv(key, default)


def get_env_list(key: str, default: list, separator: str = ',') -> list:
    """Get list from environment variable (comma-separated)"""
    value = os.getenv(key)
    if not value:
        return default
    return [item.strip() for item in value.split(separator) if item.strip()]


@lru_cache(maxsize=1)
def load_config(config_path: Optional[Path] = None) -> SystemConfig:
    """
    Load and validate configuration from environment variables and optional config file

    Args:
        config_path: Optional path to JSON configuration file

    Returns:
        Validated SystemConfig instance

    Raises:
        ConfigurationError: If configuration is invalid
    """
    # Load from file if provided
    file_config = {}
    if config_path and config_path.exists():
        try:
            file_config = json.loads(config_path.read_text(encoding='utf-8'))
        except Exception as e:
            raise ConfigurationError(f"Failed to load config file: {e}")

    # Base configuration
    config_dict = {
        'environment': get_env_str('TECHDIVE_ENV', file_config.get('environment', 'production')),
        'debug': get_env_bool('TECHDIVE_DEBUG', file_config.get('debug', False)),

        # Knowledge configuration
        'knowledge': {
            'domain': get_env_str('TECHDIVE_KNOWLEDGE_DOMAIN', file_config.get('knowledge', {}).get('domain', 'Technical Diving Decompression Physiology & Safety')),
            'keywords': get_env_list('TECHDIVE_KEYWORDS', file_config.get('knowledge', {}).get('keywords', [])),
            'max_results_per_source': get_env_int('TECHDIVE_MAX_RESULTS', file_config.get('knowledge', {}).get('max_results_per_source', 10)),
            'max_new_entries_per_run': get_env_int('TECHDIVE_MAX_ENTRIES', file_config.get('knowledge', {}).get('max_new_entries_per_run', 20)),
            'crawl_timeout_seconds': get_env_int('TECHDIVE_CRAWL_TIMEOUT', file_config.get('knowledge', {}).get('crawl_timeout_seconds', 30)),
        },

        # LLM configuration
        'llm': {
            'model_name': get_env_str('TECHDIVE_LLM_MODEL', file_config.get('llm', {}).get('model_name', 'claude-3-5-sonnet-20241022')),
            'max_tokens': get_env_int('TECHDIVE_MAX_TOKENS', file_config.get('llm', {}).get('max_tokens', 8192)),
            'temperature': get_env_float('TECHDIVE_TEMPERATURE', file_config.get('llm', {}).get('temperature', 0.7)),
            'timeout_seconds': get_env_int('TECHDIVE_LLM_TIMEOUT', file_config.get('llm', {}).get('timeout_seconds', 120)),
            'enable_cache': get_env_bool('TECHDIVE_CACHE_ENABLED', file_config.get('llm', {}).get('enable_cache', True)),
        },

        # Decompression configuration
        'decompression': {
            'model': get_env_str('TECHDIVE_DECOMP_MODEL', file_config.get('decompression', {}).get('model', 'Bühlmann ZHL-16C')),
            'gradient_factor_low': get_env_int('TECHDIVE_GF_LOW', file_config.get('decompression', {}).get('gradient_factor_low', 30)),
            'gradient_factor_high': get_env_int('TECHDIVE_GF_HIGH', file_config.get('decompression', {}).get('gradient_factor_high', 85)),
            'max_po2_working': get_env_float('TECHDIVE_MAX_PO2_WORK', file_config.get('decompression', {}).get('max_po2_working', 1.4)),
            'max_po2_decompression': get_env_float('TECHDIVE_MAX_PO2_DECO', file_config.get('decompression', {}).get('max_po2_decompression', 1.6)),
            'max_gas_density_grams_per_liter': get_env_float('TECHDIVE_MAX_DENSITY', file_config.get('decompression', {}).get('max_gas_density_grams_per_liter', 6.2)),
        },

        # Quality gates
        'quality_gates': {
            'min_sources_required': get_env_int('TECHDIVE_MIN_SOURCES', file_config.get('quality_gates', {}).get('min_sources_required', 3)),
            'min_academic_sources': get_env_int('TECHDIVE_MIN_ACADEMIC', file_config.get('quality_gates', {}).get('min_academic_sources', 1)),
            'enable_auto_fix': get_env_bool('TECHDIVE_AUTO_FIX', file_config.get('quality_gates', {}).get('enable_auto_fix', True)),
            'strict_mode': get_env_bool('TECHDIVE_STRICT_MODE', file_config.get('quality_gates', {}).get('strict_mode', False)),
        },

        # Feature flags
        'features': {
            'enable_probabilistic_dcs': get_env_bool('TECHDIVE_FEATURE_PROBABILISTIC', file_config.get('features', {}).get('enable_probabilistic_dcs', False)),
            'enable_vpm_alternative_model': get_env_bool('TECHDIVE_FEATURE_VPM', file_config.get('features', {}).get('enable_vpm_alternative_model', False)),
            'enable_rgbm_model': get_env_bool('TECHDIVE_FEATURE_RGBM', file_config.get('features', {}).get('enable_rgbm_model', False)),
            'enable_cns_otu_tracking': get_env_bool('TECHDIVE_FEATURE_CNS', file_config.get('features', {}).get('enable_cns_otu_tracking', True)),
            'enable_gas_density_validation': get_env_bool('TECHDIVE_FEATURE_DENSITY', file_config.get('features', {}).get('enable_gas_density_validation', True)),
        },

        # API configuration
        'api': {
            'requests_timeout': get_env_int('TECHDIVE_API_TIMEOUT', file_config.get('api', {}).get('requests_timeout', 30)),
            'max_concurrent_requests': get_env_int('TECHDIVE_MAX_CONCURRENT', file_config.get('api', {}).get('max_concurrent_requests', 5)),
            'user_agent': get_env_str('TECHDIVE_USER_AGENT', file_config.get('api', {}).get('user_agent', 'technical-diving-skill/1.0')),
            'verify_ssl': get_env_bool('TECHDIVE_VERIFY_SSL', file_config.get('api', {}).get('verify_ssl', True)),
        },

        # Logging configuration
        'logging': {
            'level': LogLevel(get_env_str('TECHDIVE_LOG_LEVEL', file_config.get('logging', {}).get('level', 'INFO')).upper()),
            'file_enabled': get_env_bool('TECHDIVE_LOG_FILE', file_config.get('logging', {}).get('file_enabled', True)),
            'file_path': get_env_str('TECHDIVE_LOG_PATH', file_config.get('logging', {}).get('file_path', 'logs/technical_diving_skill.log')),
            'console_enabled': get_env_bool('TECHDIVE_LOG_CONSOLE', file_config.get('logging', {}).get('console_enabled', True)),
            'structured_logging': get_env_bool('TECHDIVE_STRUCTURED_LOGS', file_config.get('logging', {}).get('structured_logging', True)),
        },

        # Monitoring
        'monitoring': {
            'enable_metrics': get_env_bool('TECHDIVE_METRICS_ENABLED', file_config.get('monitoring', {}).get('enable_metrics', True)),
            'performance_tracking': get_env_bool('TECHDIVE_PERF_TRACKING', file_config.get('monitoring', {}).get('performance_tracking', True)),
            'error_tracking': get_env_bool('TECHDIVE_ERROR_TRACKING', file_config.get('monitoring', {}).get('error_tracking', True)),
        },
    }

    # Create configuration instance
    try:
        config = SystemConfig(**config_dict)
    except Exception as e:
        raise ConfigurationError(f"Failed to create configuration: {e}")

    # Validate configuration
    errors = config.validate()
    if errors:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {err}" for err in errors)
        raise ConfigurationError(error_msg)

    return config


def get_config() -> SystemConfig:
    """Get current configuration (cached)"""
    return load_config()


def reload_config(config_path: Optional[Path] = None) -> SystemConfig:
    """Reload configuration from disk"""
    load_config.cache_clear()
    return load_config(config_path)


def save_default_config(output_path: Path) -> None:
    """Save a default configuration file with all settings documented"""
    config = SystemConfig()

    config_dict = {
        'environment': config.environment.value,
        'debug': config.debug,
        'knowledge': {
            'domain': config.knowledge.domain,
            'keywords': config.knowledge.keywords,
            'max_results_per_source': config.knowledge.max_results_per_source,
            'max_new_entries_per_run': config.knowledge.max_new_entries_per_run,
            'crawl_timeout_seconds': config.knowledge.crawl_timeout_seconds,
        },
        'llm': {
            'model_name': config.llm.model_name,
            'max_tokens': config.llm.max_tokens,
            'temperature': config.llm.temperature,
            'timeout_seconds': config.llm.timeout_seconds,
            'enable_cache': config.llm.enable_cache,
        },
        'decompression': {
            'model': config.decompression.model,
            'gradient_factor_low': config.decompression.gradient_factor_low,
            'gradient_factor_high': config.decompression.gradient_factor_high,
            'max_po2_working': config.decompression.max_po2_working,
            'max_po2_decompression': config.decompression.max_po2_decompression,
            'max_gas_density_grams_per_liter': config.decompression.max_gas_density_grams_per_liter,
        },
        'quality_gates': {
            'min_sources_required': config.quality_gates.min_sources_required,
            'min_academic_sources': config.quality_gates.min_academic_sources,
            'enable_auto_fix': config.quality_gates.enable_auto_fix,
            'strict_mode': config.quality_gates.strict_mode,
        },
        'features': {
            'enable_probabilistic_dcs': config.features.enable_probabilistic_dcs,
            'enable_vpm_alternative_model': config.features.enable_vpm_alternative_model,
            'enable_rgbm_model': config.features.enable_rgbm_model,
            'enable_cns_otu_tracking': config.features.enable_cns_otu_tracking,
            'enable_gas_density_validation': config.features.enable_gas_density_validation,
        },
        'api': {
            'requests_timeout': config.api.requests_timeout,
            'max_concurrent_requests': config.api.max_concurrent_requests,
            'user_agent': config.api.user_agent,
            'verify_ssl': config.api.verify_ssl,
        },
        'logging': {
            'level': config.logging.level.value,
            'file_enabled': config.logging.file_enabled,
            'file_path': config.logging.file_path,
            'console_enabled': config.logging.console_enabled,
            'structured_logging': config.logging.structured_logging,
        },
        'monitoring': {
            'enable_metrics': config.monitoring.enable_metrics,
            'performance_tracking': config.monitoring.performance_tracking,
            'error_tracking': config.monitoring.error_tracking,
        },
    }

    output_path.write_text(json.dumps(config_dict, indent=2), encoding='utf-8')
