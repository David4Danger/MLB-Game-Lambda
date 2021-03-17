import json
import mlbgame


def lambda_handler(event, context):
    players = event["multiValueQueryStringParameters"]['playername']
    print("Started to retrieve live player data with player list {}".format(players))

    # Hardcode for now to test since season isnt live
    year = 2019
    month = 7
    day = 24

    league_info = mlbgame.league()
    jays_july_2019 = mlbgame.games(year, months=month, home='Blue Jays', away='Blue Jays')
    game_id = jays_july_2019[0][0].game_id
    game_events = mlbgame.game_events(game_id)
    league_info.nice_output()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == '__main__':
    playername_list = ['Chris Sale', 'Gerrit Cole']
    playername = dict(playername=playername_list)
    event = dict(multiValueQueryStringParameters=playername)
    lambda_handler(event, 'yeet')
