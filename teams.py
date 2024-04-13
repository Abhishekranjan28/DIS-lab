from sql_connection import get_sql_connection

def get_all_teams(connection):
    cursor = connection.cursor()
    query = ("select team.team_id, team.team_name, team.total_purse, team.total_players, team.team_owner from team")
    cursor.execute(query)
    response = []
    for (team_id, team_name, total_purse,total_players, team_owner) in cursor:
        response.append({
            'team_id':team_id,
            'team_name': team_name,
            'total_purse': total_purse,
            'total_players': total_players,
            'team_owner':team_owner
        })
    return response

def insert_new_team(connection, team):
    cursor = connection.cursor()
    query = ("INSERT INTO team "
             "(team_id,team_name,total_purse,total_players,team_owner)"
             "VALUES (%s, %s, %s,%s,%s)")
    data = (team['team_id'], team['team_name'], team['total_purse'],team['total_players'],team['team_owner'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_team(connection, team_id):
    cursor = connection.cursor()
    query = ("DELETE FROM team where team_id=" + str(team_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_team(connection, {
        'team_id': 3,
        'team_name': 'RCB',
        'total_purse': 100,
        'total_players':25,
        'team_owner': 'Vijaya Malya'
    }))
    print(get_all_teams(connection))