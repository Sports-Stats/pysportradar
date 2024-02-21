
from pysportradar.api import Api


class NCAAMBApi(Api):
    def __init__(self, api_key, format_="json", access_type="trial"):
        super().__init__(api_key=api_key)
        self.access_type = access_type
        self.format = format_
        self.sport = "ncaamb"
        self.version = "v8"
        self.language = "en"
        self.base_url = f"{self.base_url}/{self.sport}/{self.access_type}/{self.version}/{self.language}"

    def get_daily_change_log(self, year, month, day):
        return self._get(path=f"/league/{year}/{month}/{day}/changes.{self.format}")
    
    def get_daily_schedule(self, year, month, day):
        return self._get(path=f"/games/{year}/{month}/{day}/schedule.{self.format}")
    
    def get_boxscore(self, game_id):
        return self._get(path=f"/games/{game_id}/boxscore.{self.format}")
    
    def get_game_summary(self, game_id):
        return self._get(path=f"/games/{game_id}/summary.{self.format}")
    
    def get_league_hierarchy(self):
        return self._get(path=f"/league/hierarchy.{self.format}")

    def get_league_leaders(self, year, type_, div_or_conf):
        return self._get(path=f"/seasons/{year}/{type_}/{div_or_conf}/leaders.{self.format}")
    
    def get_play_by_play(self, game_id):
        return self._get(path=f"/games/{game_id}/pbp.{self.format}")
    
    def get_player_profile(self, player_id):
        return self._get(path=f"/players/{player_id}/profile.{self.format}")
    
    def get_current_ranking(self, poll_name, year):
        return self._get(path=f"/polls/{poll_name}/{year}/rankings.{self.format}")
    
    def get_rankings_by_week(self, poll_name, season_year, season_week):
        return self._get(path=f"/polls/{poll_name}/{season_year}/{season_week}/rankings.{self.format}")
    
    def get_rpi_rankings(self, year):
        return self._get(path=f"/rpi/{year}/rankings.{self.format}")
    
    def get_schedule(self, year, season_type):
        return self._get(path=f"/games/{year}/{season_type}/schedule.{self.format}")
    
    def get_season_statistics(self, year, season_type, team_id):
        return self._get(path=f"/seasons/{year}/{season_type}/teams/{team_id}/statistics.{self.format}")
    
    def get_seasons(self):
        return self._get(path=f"/league/seasons.{self.format}")
    
    def get_standings(self, year, season_type):
        return self._get(path=f"/seasons/{year}/{season_type}/standing.{self.format}")
    
    def get_team_profile(self, team_id):
        return self._get(path=f"/teams/{team_id}/profile.{self.format}")

    def get_tournament_list(self, year, season_type):
        return self._get(path=f"/tournaments/{year}/{season_type}/schedule.{self.format}")

    def get_tournament_schedule(self, tournament_id):
        return self._get(path=f"/tournaments/{tournament_id}/schedule.{self.format}")
    
    def get_tournament_statistics(self, tournament_id, team_id):
        return self._get(path=f"/tournaments/{tournament_id}/{team_id}/statistics.{self.format}")
    
    def get_tournament_summary(self, tournament_id):
        return self._get(path=f"/tournaments/{tournament_id}/summary.{self.format}")
    
