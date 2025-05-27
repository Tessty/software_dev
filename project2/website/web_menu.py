from website.extension import db
from website.models import MenuItem
from website import create_app  # or from app import create_app

app = create_app()

def web_menu():
    with app.app_context():
        db.drop_all()
        db.create_all()

        menu_items = [
            MenuItem(name='Salmon Sashimi', price=12.99, image='salmon.jpg'),
            MenuItem(name='Tuna Tataki', price=13.99, image='tuna_tataki.jpg'),
            MenuItem(name='Spicy Tuna Roll', price=9.99, image='spicy_tuna_roll.jpg'),
            MenuItem(name='California Roll', price=8.99, image='california_roll.jpg'),
            MenuItem(name='Dragon Roll', price=14.99, image='dragon_roll.jpg'),
            MenuItem(name='Vegetable Tempura', price=7.99, image='vegetable_tempura.jpg'),
            MenuItem(name='Shrimp Tempura', price=9.99, image='shrimp_tempura.jpg'),
            MenuItem(name='Pork Gyoza', price=6.99, image='pork_gyoza.jpg'),
            MenuItem(name='Chicken Karaage', price=10.99, image='chicken_karaage.jpg'),
            MenuItem(name='Chicken Teriyaki', price=11.99, image='chicken_teriyaki.jpg'),
            MenuItem(name='Beef Teriyaki', price=13.99, image='beef_teriyaki.jpg'),
            MenuItem(name='Unagi Donburi', price=16.99, image='unagi_donburi.jpg'),
            MenuItem(name='Miso Soup', price=3.50, image='miso_soup.jpg'),
            MenuItem(name='Seaweed Salad', price=4.99, image='seaweed_salad.jpg'),
            MenuItem(name='Edamame', price=4.00, image='edamame.jpg'),
            MenuItem(name='Beef Yakitori', price=8.99, image='beef_yakitori.jpg'),
            MenuItem(name='Chicken Yakitori', price=7.99, image='chicken_yakitori.jpg'),
            MenuItem(name='Tako Yaki', price=6.99, image='tako_yaki.jpg'),
            MenuItem(name='Okonomiyaki', price=11.99, image='okonomiyaki.jpg'),
            MenuItem(name='Matcha Ice Cream', price=4.99, image='matcha_ice_cream.jpg'),
            MenuItem(name='Mochi Ice Cream', price=5.50, image='mochi_ice_cream.jpg'),
        ]

        db.session.bulk_save_objects(menu_items)
        db.session.commit()
        print("Database seeded with a variety of Japanese Izakaya menu items.")

if __name__ == '__main__':
    web_menu()
