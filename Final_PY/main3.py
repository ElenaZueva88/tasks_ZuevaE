from datetime import datetime, timedelta
def future_date(days_from_now):
    today = datetime.now()
    future_date = today + timedelta(days=days_from_now)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date
if __name__ == '__main__':
    days = 30
    print(f'Date {days} days from now: {future_date(days)}')
