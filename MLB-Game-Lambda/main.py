import json
import statsapi
from datetime import datetime


# TODO return proper 400 for player not found for year, work on year formatting for getting player id
def lambda_handler(event, context):
    player_name = event["queryStringParameters"]['player_name']
    year = event["queryStringParameters"]['year']
    stat_group = event["queryStringParameters"]['stat_group']

    print("Started to retrieve player data for player {} in year {}".format(player_name, year))
    updated_year = 'career' if ('~' == year) else 'yearByYear'
    formatted_stat_group = '[{0}]'.format(stat_group)
    last_year = datetime.now().year - 1 # Cant use current year until season starts

    person_id = statsapi.lookup_player(player_name, season=last_year)[0].get('id')
    player_data = statsapi.player_stat_data(person_id, group=formatted_stat_group, type=updated_year)

    if updated_year == 'yearByYear':
        filtered_year_list = [stat_year for stat_year in player_data.get('stats') if stat_year.get('season') == year]
        player_data['stats'] = filtered_year_list

    print("Successfully Returning player data for player {}".format(player_name))
    return {
        'statusCode': 200,
        'body': json.dumps(player_data)
    }

#if __name__ == '__main__':
#    query_params = dict(player_name='Cole, Gerrit', year='2019', stat_group='pitching')
#    event = dict(queryStringParameters=query_params)
#    lambda_handler(event, 'yeet')
