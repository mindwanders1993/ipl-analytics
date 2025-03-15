import pandas as pd
import numpy as np
from src.utils.logger import get_logger

logger = get_logger(__name__)

class TeamAnalysis:
    def __init__(self, matches_df):
        self.matches_df = matches_df
        logger.info("TeamAnalysis initialized with matches data")
    
    def get_win_percentage(self, team_name=None):
        """Calculate win percentage for all teams or a specific team."""
        if team_name:
            team_matches = self.matches_df[(self.matches_df['team1'] == team_name) | 
                                           (self.matches_df['team2'] == team_name)]
            wins = team_matches[team_matches['winner'] == team_name].shape[0]
            total = team_matches.shape[0]
            return (wins / total) * 100 if total > 0 else 0
        
        # For all teams
        all_teams = set(self.matches_df['team1'].unique()) | set(self.matches_df['team2'].unique())
        results = {}
        
        for team in all_teams:
            results[team] = self.get_win_percentage(team)
        
        return pd.DataFrame(list(results.items()), columns=['Team', 'Win Percentage']).sort_values(
            by='Win Percentage', ascending=False)
    
    def get_head_to_head(self, team1, team2):
        """Get head-to-head statistics between two teams."""
        matches = self.matches_df[((self.matches_df['team1'] == team1) & 
                                   (self.matches_df['team2'] == team2)) | 
                                  ((self.matches_df['team1'] == team2) & 
                                   (self.matches_df['team2'] == team1))]
        
        team1_wins = matches[matches['winner'] == team1].shape[0]
        team2_wins = matches[matches['winner'] == team2].shape[0]
        no_result = matches[matches['winner'].isna()].shape[0]
        
        return {
            'total_matches': matches.shape[0],
            f'{team1}_wins': team1_wins,
            f'{team2}_wins': team2_wins,
            'no_result': no_result
        }