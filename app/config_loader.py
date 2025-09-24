# app/config_loader.py
"""
Loads exclude file types from a YAML file
"""
import os
import yaml
from typing import Dict, Set


def load_exclude_config(config_path: str = "config/exclude_config.yaml") -> Dict[str, Set[str]]:
    """
    Loads a list of extensions and directories to exclude from a YAML file.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        dict: A dictionary with keys 'file_types' and 'directories' containing sets of strings.
    """
    default_config = {"file_types": set(), "directories": set()}

    if not os.path.exists(config_path):
        print(f"⚠️ Configuration file not found: {config_path}. Using default values.")
        return default_config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        file_types = set(data.get("exclude_file_types", []))
        directories = set(data.get("exclude_directories", []))

        return {
            "file_types": file_types,
            "directories": directories
        }
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        return default_config
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return default_config