from datetime import datetime, timedelta
import asyncio

async def get_leaderboard(database) -> str:
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())  # Начало недели (понедельник)
    end_of_week = start_of_week + timedelta(days=6)  # Конец недели (воскресенье)
    start_of_week_str = start_of_week.strftime("%d.%m")
    end_of_week_str = end_of_week.strftime("%d.%m")

    all_users = await database.get_all_users()
    sorted_users = sorted(all_users.items(), key=lambda item: item[1]['points'], reverse=True)

    top_users = sorted_users[:10]

    leaderboard = f"⭐️ Leaderboard (week {start_of_week_str} - {end_of_week_str})⭐️\n"
    for index, (user_id, user_data) in enumerate(top_users, start=1):
        leaderboard += f"{index}. {user_data.get('name', 'Unknown')} - {user_data['points']} points\n"

    leaderboard += "\nThe leaderboard of the current day resets daily at 00:00\n"

    return leaderboard