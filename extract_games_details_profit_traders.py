import json

read_file = open('games_between_11_24_Aug_2022.json', encoding='utf-8')
games = json.load(read_file)
query: str = "WITH PROVIDED_GAMES AS (\n"

for i in games['data']['sportMarkets']:
    
    if ['isResolved']:
        game: str = i['homeTeam'] + ' VS ' + i['awayTeam']
        address: str = i['address']
        game_tag: str = (i['tags'][0][2:])
        
        if game_tag == '01':
            league_name = 'NCAA Mens Football'
        
        if game_tag == '02':
            league_name = 'NFL- American football'
        
        if game_tag == '03':
            league_name = 'MLB - Baseball'
        
        if game_tag == '04':
            league_name = 'NBA - Basketball'
        
        if game_tag == '05':
            league_name = 'NCAA - Mens Basketball'
        
        if game_tag == '06':
            league_name = 'NHL - Hockey'
        
        if game_tag == '07':
            league_name = 'MMA'
        
        if game_tag == '08':
            league_name = 'WNBA - Basketball'
        
        elif game_tag == '10':
            league_name = 'MLS - Soccer'
        
        if game_tag == '11':
            league_name = 'EPL - Soccer'
        
        if game_tag == '12':
            league_name = 'Ligue 1 - Soccer'
        
        if game_tag == '13':
            league_name = 'Bundesliga - Soccer'
        
        if game_tag == '14':
            league_name = 'La Liga - Soccer'
        
        if game_tag == '15':
            league_name = 'Serie A - Soccer'
        
        if game_tag == '16':
            league_name = 'UCL - Soccer'
        
        game_tag = (i['tags'][0][2:])
        
        if game_tag == '10' or game_tag == '11' or game_tag == '12' or game_tag == '13' or game_tag == '14' or game_tag == '15' or game_tag == '16':
            sport_type = 'Soccer'
        
        if game_tag == '01' or game_tag == '02':
            sport_type = 'American football'
        
        if game_tag == '03':
            sport_type = 'Baseball'
        
        if game_tag == '04' or game_tag == '05' or game_tag == '08':
            sport_type = 'Basketball'
        
        if game_tag == '06':
            sport_type = 'Hockey'
        
        if game_tag == '07':
            sport_type = 'MMA'
            

        sql_str: str = f"SELECT '{game}' AS GAME, '{sport_type}' AS Sport ,'{league_name}' AS League, '{address}' AS ADDRESS UNION\n"
        query = query + sql_str

query = query[:-7] + ')'
with open('optimism_profitable_traders_between_11_24_Aug_2022.sql', 'w', encoding='utf-8') as f:
    f.write(query)


