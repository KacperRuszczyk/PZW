import numpy as np
import pandas as pd
from datetime import datetime, timedelta


num = 100

def random_date(base_date, days_range=60):
    return base_date + timedelta(days=int(np.random.randint(-days_range, days_range)))

today = datetime.now()
np.random.seed(int(str(today)[-3::]))

data = {
    "ID": range(1, num + 1),
    "registration_number": [f"SC{np.random.randint(10000,99999)}" for _ in range(num)],
    "technical_inspection_date": [random_date(today) for _ in range(num)],
    "insurance_expiry_date": [random_date(today) for _ in range(num)],
    "owner_email": [f"user{i}@PZW.pl" for i in range(1, num + 1)]
}

df = pd.DataFrame(data)

def notify(df, date_column, notify_type):
    for _, row in df.iterrows():
        check = (row[date_column] - today).days
        if check in [30, 7, 3]:
            print(f"[{notify_type}] Powiadomienie dla {row['owner_email']}:")
            print(f" - Samochód: {row['registration_number']}")
            print(f" - Data {notify_type}: {row[date_column].strftime('%Y-%m-%d')}")
            print(f" - Pozostało {check} dni\n")

notify(df, 'technical_inspection_date', 'Przegląd')
notify(df, 'insurance_expiry_date', 'OC')