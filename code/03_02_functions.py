import pandas as pd
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = './data'

# load player-game data
pg = pd.read_csv(path.join(DATA_DIR, 'player_game.csv'))

pg[['game_id', 'player_id', 'date']] = (
    pg[['game_id', 'player_id', 'date']].astype(str))

# book picks up here:
pg[['fgm', 'fga', 'fg_pct', 'pts', 'fg3m', 'fg3a', 'fg3_pct']].mean()
pg[['fgm', 'fga', 'pts', 'fg3m', 'fg3a']].max()

pg.max()

# Axis
pg[['pts', 'ast', 'stl', 'reb']].mean(axis=0)
pg[['pts', 'ast', 'stl', 'reb']].mean(axis=1).head()

# Summary functions on boolean columns
pg['cold_shooting'] = (pg['fga'] > 10) & (pg['pts'] < 5)
pg['cold_shooting'].mean()

pg['cold_shooting'].sum()

(pg['fg3a'] > 30).any()
(pg['fg3a'] > 20).any()

(pg['min'] > 0).all()

(pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).any(axis=1)

pg['triple_double'] = ((pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10)
                       .sum(axis=1) >= 3)

(pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).head()
(pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).sum(axis=1).head()
((pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).sum(axis=1) >= 3).head()

pg['triple_double'].sum()

# Other misc built-in summary functions
pg['pos'].value_counts()

pg['pos'].value_counts(normalize=True)

pd.crosstab(pg['team'], pg['pos']).head()

######## Exercises

# 3.2.1
pg = pd.read_csv(path.join(DATA_DIR, 'player_game.csv'))

# 3.2.2
pg['total_shots1'] = pg['fga'] + pg['fta']
pg['total_shots2'] =  pg[['fga', 'fta']].sum(axis=1)

pg[['name', 'total_shots1', 'total_shots2']].head()

(pg['total_shots1'] == pg['total_shots2']).all()

# 3.2.3
pg[['pts', 'fga', 'reb']].mean()

# pts    10.659413
# fga     8.403500
# reb     4.242668

((pg['pts']>=40) & (pg['reb']>=10)).sum()
# 3
((pg['pts']>=40) & (pg['reb']>=10)).sum()/(pg['pts']>=40).sum()
# 0.3

pg['fg3a'].sum()
# 6809

pg['team'].value_counts().sort_values
# ORL