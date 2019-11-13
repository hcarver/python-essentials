import csv

with open('profile_data.csv') as f:
    reader = csv.DictReader(f)
    all_profiles_raw = [dict(x) for x in reader]


def flat_profile(raw_profile):
    d = raw_profile.copy()
    d['favourite_shop'] = raw_profile['shop_1']
    del d['shop_1'], d['shop_2']
    return d


def multiple_shops_profile(raw_profile):
    d = raw_profile.copy()
    d['favourite_shop'] = [raw_profile['shop_1'], raw_profile['shop_2']]
    del d['shop_1'], d['shop_2']
    return d


all_profiles = [flat_profile(p) for p in all_profiles_raw]
all_profiles_multishop = [multiple_shops_profile(p) for p in all_profiles_raw]
