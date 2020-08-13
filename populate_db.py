import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xinohack.settings')

import django
django.setup()
from core.models import Places, InterestsActivities, CustomUser, Hiring

def main():

    places = [
        {'name':'New Delhi','country':'India','general_price':300, 'currency':'₹'},
        {'name':'Chennai', 'country':'India', 'general_price':250, 'currency':'₹'},
        {'name':'Los Angeles', 'country':'United States of America', 'general_price':10, 'currency':'CA$'},
        {'name':'Waterloo', 'country':'Canada', 'general_price':7, 'currency':'$'},
        {'name':'Paris', 'country':'France', 'general_price':5, 'currency':'€'},
        {'name':'London', 'country':'England', 'general_price':6, 'currency':'€'},
        {'name':'Melbourne', 'country':'Australia', 'general_price':9, 'currency':'AUD$'},
        {'name':'Mumbai', 'country':'India', 'general_price':250, 'currency':'₹'},
        {'name':'Kolkata','country':'India', 'general_price':240, 'currency':'₹'},
        {'name':'Jodhpur', 'country':'India', 'general_price':200, 'currency':'₹'},
        {'name':'Kanyakumari', 'country':'India', 'general_price':220, 'currency':'₹'},
        {'name':'Chicago', 'country':'United States of America', 'general_price':10, 'currency':'$'},
        {'name':'Agra','country':'India', 'general_price':230, 'currency':'₹'},
        {'name':'Beijing','country':'China', 'general_price':30, 'currency':'¥'},
        {'name':'Shanghai','country':'China', 'general_price':35, 'currency':'¥'},
        {'name':'Gangtok', 'country':'India', 'general_price':200, 'currency':'₹'}
    ]

    interests = [
        'Cricket',
        'Tech',
        'Military',
        'Politics',
        'Internation Affairs',
        'Medical',
        'Business',
        'Legal',
        'Football',
        'Basketball',
        'Tennis',
        'Badminton',
        'Volleyball',
        'Ice Hockey',
        'Stand Up Comedy',
        'Hollywood Movies',
        'The Beatles',
        "Guns N'Roses",
        "AC/DC",
        "Queen",
        "Bollywood Movies"
    ]

    def add_place(name, country, general_price, currency):
        p = Places.objects.create(
            name=name,
            country=country,
            general_price=general_price,
            currency=currency
        )
        print(f"Successfuly created {p} with {p.country} and {p.general_price}")

    def add_interests(name):
        i = InterestsActivities.objects.create(
            name=name
        )
        print(f"Successfully created Interest {i}")

    if not Places.objects.filter(name='New Delhi').exists():
        for i in places:
            print(str(i))
            add_place(i['name'], i['country'], i['general_price'], i['currency'])
    else:
        print("Places have already been created")

    if not InterestsActivities.objects.filter(name='Cricket').exists():
        for i in interests:
            add_interests(i)
    else:
        print("Already created interests")

if __name__ == "__main__":
    print("Initialising population script")
    main()