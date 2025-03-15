import os
import yaml
from pathlib import Path

class Config:
    def __init__(self, config_path=None):
        # Default to production config if not specified
        if config_path is None:
            env = os.getenv("ENVIRONMENT", "prod")
            config_path = Path(__file__).parent.parent.parent / f"configs/{env}.yaml"
        
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
    
    def get(self, key, default=None):
        """Get a configuration value."""
        return self.config.get(key, default)
    
    @property
    def data_path(self):
        """Get the data directory path."""
        return Path(self.get('data_path', 'data/'))
    
    @property
    def raw_data_path(self):
        """Get the raw data directory path."""
        return self.data_path / 'raw'
    
    @property
    def processed_data_path(self):
        """Get the processed data directory path."""
        return self.data_path / 'processed'