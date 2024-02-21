from os import path
import pandas as pd

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = 'C:/Users/lukas/Documents/code-basketball-files/data'

##############
# Loading data
##############
shots = pd.read_csv(path.join(DATA_DIR, 'shots.csv'))

type(shots)

##################################
# DataFrame methods and attributes
##################################
shots.head()

shots.columns

shots.shape

#################################
# Working with subsets of columns
#################################
# A single column
shots['name'].head()

type(shots['name'])

shots['name'].to_frame().head()
type(shots['name'].to_frame().head())

# Multiple columns
shots[['name', 'dist', 'value', 'made']].head()

type(shots[['name', 'dist', 'value', 'made']].head())

# commented out because it throws an error
# shots['name', 'dist', 'value', 'made'].head() 

##########
# Indexing
##########
shots[['name', 'dist', 'value', 'made']].head()

shots.set_index('shot_id').head()

# Copies and the inplace argument
shots.head()  # note: player_id not the index, even though we just set it

shots.set_index('shot_id', inplace=True)
shots.head()  # now player_id is index

# alternate to using inplace, reassign adp
# reload shots with default 0, 1, ... index
shots = pd.read_csv(path.join(DATA_DIR, 'shots.csv'))
shots = shots.set_index('shot_id')
shots.head()  # now shot_id is index

shots.reset_index().head()

#############################
# Indexes keep things aligned
#############################
shots_ot = shots.loc[shots['period'] > 4, ['name', 'dist', 'value']]
shots_ot.head()

shots_ot.sort_values('name', inplace=True)
shots_ot.head()

shots_ot.shape

# assigning a new column
shots_ot['made'] = shots['made']
shots_ot.head()

# has the same index as shots['made'] and shots['made']
shots['made'].head()

#################
# Outputting data
#################
shots_ot.to_csv(path.join(DATA_DIR, 'shots_ot.csv'))

shots_ot.to_csv(path.join(DATA_DIR, 'shots_ot_no_index.csv'), index=False)

#################
# Exercises
#################

import pandas as pd
import os

# 3.1

DATA_DIR = 'C:/Users/lukas/Documents/code-basketball-files/data'
games = pd.read_csv(os.path.join(DATA_DIR, 'games.csv'))

# 3.2

games50 = games.sort_values('date')[0:49]
len(games50)

# 3.3

games50 = games50.sort_values('home_pts', ascending=False)
print(games50['home_pts'])

# 3.4
type(games50.sort_values('home_pts'))

#3.5

game_simple = games[['date', 'home', 'away', 'home_pts', 'away_pts']]
game_simple.head()

game_simple = game_simple[['home', 'away', 'date', 'home_pts', 'away_pts']]
game_simple.head()

game_simple['game_id'] = games['game_id']
game_simple.head()

game_simple.to_csv(os.path.join(DATA_DIR, 'game_simple.csv'), sep='|')

