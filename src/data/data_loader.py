import pandas as pd
from src.utils.config import Config
from src.utils.logger import get_logger

logger = get_logger(__name__)

class IPLDataLoader:
    def __init__(self, config=None):
        self.config = config or Config()
        self.raw_data_path = self.config.raw_data_path
    
    def load_matches(self):
        """Load matches data."""
        logger.info("Loading matches data")
        matches_path = self.raw_data_path / "matches.csv"
        return pd.read_csv(matches_path)
    
    def load_deliveries(self):
        """Load ball-by-ball deliveries data."""
        logger.info("Loading deliveries data")
        deliveries_path = self.raw_data_path / "deliveries.csv"
        return pd.read_csv(deliveries_path)
    
    def load_players(self):
        """Load players data."""
        logger.info("Loading players data")
        players_path = self.raw_data_path / "players.csv"
        return pd.read_csv(players_path)