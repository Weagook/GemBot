def get_leaderboard(database) -> str:
    all_users = database.get_all_users()
    sorted_users = sorted(all_users.items(), key=lambda item: item[1]['points'], reverse=True)

    top_users = sorted_users[:10]

    leaderboard = "🏆 Leaderboard 🏆\n"
    for index, (user_id, user_data) in enumerate(top_users, start=1):
        leaderboard += f"{index}. {user_data.get('name', 'Unknown')} - {user_data['points']} points\n"

    return leaderboard