from multiprocessing import cpu_count
import pandas as pd
from tqdm import tqdm
from faker import Faker

fake = Faker()
num_cores = cpu_count() - 1


def create_dataframe():
    x = int(60000 / num_cores)
    data = pd.DataFrame()
    for i in tqdm(range(x), desc='Creating DataFrame'):
        data.loc[i, 'first_name'] = fake.first_name()
        data.loc[i, 'last_name'] = fake.last_name()
        data.loc[i, 'job'] = fake.job()
        data.loc[i, 'company'] = fake.company()
        data.loc[i, 'address'] = fake.address()
        data.loc[i, 'city'] = fake.city()
        data.loc[i, 'country'] = fake.country()
        data.loc[i, 'email'] = fake.email()
    return data


data = create_dataframe()
data.to_csv('Fake_empl_data.csv',header=True,index=False)