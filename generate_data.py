import logging
import uuid
from faker import Faker
from random import choice
from database_setup import Session
from database_setup import no_rec
from models import User, Product, Transaction

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_data():
    session = Session()
    fake = Faker()

    # List of products
    products = [
    # Electronics
        {
            'category': 'Electronics',
            'items': [
                {'name': 'XYZ Pro Max 12GB RAM', 'type': 'Smartphone', 'price': 999.99},
                {'name': 'ABC Lite 5G', 'type': 'Smartphone', 'price': 499.99},
                {'name': 'UltraBook 14” Intel i7', 'type': 'Laptop', 'price': 1299.99},
                {'name': 'PowerLaptop 15” AMD Ryzen 7', 'type': 'Laptop', 'price': 1099.99},
                {'name': 'Noise Cancelling Over-Ear Headphones', 'type': 'Headphones', 'price': 199.99},
                {'name': 'Wireless Bluetooth Earbuds', 'type': 'Headphones', 'price': 89.99},
                {'name': 'SmartWatch Series 6', 'type': 'Smartwatch', 'price': 399.99},
                {'name': 'Fitness Tracker Pro', 'type': 'Smartwatch', 'price': 149.99},
                {'name': 'Premium 10” Tablet', 'type': 'Tablet', 'price': 349.99},
                {'name': 'Compact 8” Kids Tablet', 'type': 'Tablet', 'price': 199.99},
                {'name': 'DSLR Camera with Kit Lens', 'type': 'Camera', 'price': 799.99},
                {'name': 'Compact Digital Camera', 'type': 'Camera', 'price': 299.99},
                {'name': 'Smart Speaker with Voice Assistant', 'type': 'Smart Home Device', 'price': 129.99},
                {'name': 'Smart Thermostat', 'type': 'Smart Home Device', 'price': 249.99},
                {'name': 'Fast Charging USB-C Cable', 'type': 'Charger', 'price': 19.99},
                {'name': 'Wireless Charger Pad', 'type': 'Charger', 'price': 29.99},
                {'name': 'Latest Gaming Console', 'type': 'Gaming Console', 'price': 499.99},
                {'name': 'Handheld Gaming Device', 'type': 'Gaming Console', 'price': 299.99},
                {'name': '4K Ultra HD Smart TV', 'type': 'TV', 'price': 699.99},
                {'name': 'LED TV 32”', 'type': 'TV', 'price': 229.99},
                {'name': 'Smart Doorbell with Camera', 'type': 'Home Security', 'price': 179.99},
                {'name': 'Indoor Security Camera', 'type': 'Home Security', 'price': 99.99},
                {'name': 'High-Capacity Power Bank 20,000mAh', 'type': 'Power Bank', 'price': 49.99},
                {'name': 'Compact Power Bank 10,000mAh', 'type': 'Power Bank', 'price': 29.99}
            ]
        },
        # Home & Kitchen
        {
            'category': 'Home & Kitchen',
            'items': [
                {'name': 'Electric Coffee Maker', 'type': 'Kitchen Appliance', 'price': 89.99},
                {'name': 'Air Fryer 3.5L', 'type': 'Kitchen Appliance', 'price': 119.99},
                {'name': 'Modern Area Rug (5x7 ft)', 'type': 'Home Decor', 'price': 149.99},
                {'name': 'Decorative Throw Pillow', 'type': 'Home Decor', 'price': 24.99},
                {'name': 'Adjustable Office Chair', 'type': 'Furniture', 'price': 159.99},
                {'name': 'Compact Dining Table Set', 'type': 'Furniture', 'price': 299.99},
                {'name': 'Robot Vacuum Cleaner', 'type': 'Cleaning Supply', 'price': 249.99},
                {'name': 'Microfiber Cleaning Cloth Set', 'type': 'Cleaning Supply', 'price': 15.99},
                {'name': 'Non-Stick Cookware Set', 'type': 'Cookware', 'price': 99.99},
                {'name': 'Cast Iron Skillet', 'type': 'Cookware', 'price': 39.99},
                {'name': 'Multi-Tier Storage Rack', 'type': 'Storage Solution', 'price': 89.99},
                {'name': 'Stackable Storage Bins', 'type': 'Storage Solution', 'price': 29.99},
                {'name': 'Queen Size Comforter Set', 'type': 'Bedding', 'price': 119.99},
                {'name': 'Memory Foam Pillow', 'type': 'Bedding', 'price': 49.99},
                {'name': 'LED Floor Lamp', 'type': 'Lighting', 'price': 79.99},
                {'name': 'Smart Bulb Set (4-pack)', 'type': 'Lighting', 'price': 39.99},
                {'name': 'Folding Lawn Chair', 'type': 'Outdoor Furniture', 'price': 39.99},
                {'name': 'Patio Table with Umbrella', 'type': 'Outdoor Furniture', 'price': 229.99},
                {'name': 'Ceramic Dinnerware Set (Service for 4)', 'type': 'Dining', 'price': 79.99},
                {'name': 'Stainless Steel Cutlery Set', 'type': 'Dining', 'price': 49.99},
                {'name': 'Pitcher Water Filter', 'type': 'Water Filtration', 'price': 29.99},
                {'name': 'Under-Sink Water Filter System', 'type': 'Water Filtration', 'price': 99.99},
                {'name': 'Toaster Oven', 'type': 'Small Appliance', 'price': 59.99},
                {'name': 'Electric Kettle', 'type': 'Small Appliance', 'price': 29.99}
            ]
        },
        # Clothing & Accessories
        {
            'category': 'Clothing & Accessories',
            'items': [
                {'name': 'Casual Polo Shirt (Various Colors)', 'type': 'Men’s Clothing', 'price': 29.99},
                {'name': 'Slim Fit Jeans (Blue, Black)', 'type': 'Men’s Clothing', 'price': 49.99},
                {'name': 'Floral Summer Dress', 'type': 'Women’s Clothing', 'price': 39.99},
                {'name': 'High-Waist Trousers', 'type': 'Women’s Clothing', 'price': 34.99},
                {'name': 'Leather Wallet', 'type': 'Accessory', 'price': 59.99},
                {'name': 'Sunglasses (Various Styles)', 'type': 'Accessory', 'price': 19.99},
                {'name': 'Classic Sneakers', 'type': 'Footwear', 'price': 69.99},
                {'name': 'Leather Ankle Boots', 'type': 'Footwear', 'price': 89.99},
                {'name': 'Woolen Scarf', 'type': 'Winter Wear', 'price': 29.99},
                {'name': 'Insulated Winter Gloves', 'type': 'Winter Wear', 'price': 24.99},
                {'name': 'Moisture-Wicking Workout T-Shirt', 'type': 'Activewear', 'price': 24.99},
                {'name': 'Yoga Pants', 'type': 'Activewear', 'price': 29.99},
                {'name': 'Minimalist Pendant Necklace', 'type': 'Jewelry', 'price': 49.99},
                {'name': 'Classic Hoop Earrings', 'type': 'Jewelry', 'price': 29.99},
                {'name': 'Crossbody Bag', 'type': 'Bag', 'price': 79.99},
                {'name': 'Travel Duffel Bag', 'type': 'Bag', 'price': 89.99},
                {'name': 'Baseball Cap', 'type': 'Hat & Cap', 'price': 19.99},
                {'name': 'Beanie Hat', 'type': 'Hat & Cap', 'price': 14.99},
                {'name': 'Polarized Sunglasses', 'type': 'Sunglasses', 'price': 39.99},
                {'name': 'Retro Cat-Eye Sunglasses', 'type': 'Sunglasses', 'price': 34.99},
                {'name': 'Leather Dress Belt', 'type': 'Belt', 'price': 29.99},
                {'name': 'Casual Canvas Belt', 'type': 'Belt', 'price': 19.99},
                {'name': 'Leather Watch Strap', 'type': 'Watch Accessory', 'price': 49.99},
                {'name': 'Watch Box for Storage', 'type': 'Watch Accessory', 'price': 59.99}
            ]
        },
        # Health & Beauty
        {
            'category': 'Health & Beauty',
            'items': [
                {'name': 'Moisturizing Face Cream', 'type': 'Skincare', 'price': 34.99},
                {'name': 'Anti-Aging Serum', 'type': 'Skincare', 'price': 49.99},
                {'name': 'Shampoos & Conditioners Set', 'type': 'Hair Care', 'price': 19.99},
                {'name': 'Hair Styling Tools (Straightener, Curler)', 'type': 'Hair Care', 'price': 89.99},
                {'name': 'Yoga Mat', 'type': 'Fitness', 'price': 29.99},
                {'name': 'Resistance Bands Set', 'type': 'Fitness', 'price': 24.99},
                {'name': 'Electric Toothbrush', 'type': 'Personal Care', 'price': 79.99},
                {'name': 'Beard Trimmer', 'type': 'Personal Care', 'price': 59.99},
                {'name': 'Foundation and Concealer Set', 'type': 'Makeup', 'price': 39.99},
                {'name': 'Eye Shadow Palette', 'type': 'Makeup', 'price': 24.99},
                {'name': 'Nail Polish Set', 'type': 'Nail Care', 'price': 14.99},
                {'name': 'Nail Care Tools Kit', 'type': 'Nail Care', 'price': 19.99},
                {'name': 'Body Scrub Exfoliator', 'type': 'Body Care', 'price': 22.99},
                {'name': 'Bath Bombs Gift Set', 'type': 'Body Care', 'price': 29.99},
                {'name': 'Essential Oil Diffuser', 'type': 'Wellness', 'price': 39.99},
                {'name': 'Relaxation Candle Set', 'type': 'Wellness', 'price': 22.99},
                {'name': 'SPF 50 Sunscreen Lotion', 'type': 'Sun Protection', 'price': 19.99},
                {'name': 'After-Sun Hydrating Gel', 'type': 'Sun Protection', 'price': 24.99},
                {'name': 'Digital Thermometer', 'type': 'Health Monitoring', 'price': 15.99},
                {'name': 'Blood Pressure Monitor', 'type': 'Health Monitoring', 'price': 59.99},
                {'name': 'Daily Multivitamin Tablets', 'type': 'Vitamins & Supplements', 'price': 14.99},
                {'name': 'Omega-3 Fish Oil Capsules', 'type': 'Vitamins & Supplements', 'price': 19.99},
                {'name': 'First Aid Kit', 'type': 'First Aid', 'price': 29.99},
                {'name': 'Antiseptic Wipes and Ointments', 'type': 'First Aid', 'price': 12.99}
            ]
        }
    ]

    # Create a dictionary to map product names to their IDs
    product_dict = {}
    existing_product_names = set()

    # Query existing products and build the product_dict
    existing_products = session.query(Product).all()
    for prod in existing_products:
        product_dict[prod.product_name] = prod.product_id
        existing_product_names.add(prod.product_name)

    for category in products:
        for item in category['items']:
            if item['name'] not in existing_product_names:
                product_id = str(uuid.uuid4())
                product_dict[item['name']] = product_id
                existing_product_names.add(item['name'])
                product = Product(
                    product_id=product_id,
                    product_name=item['name'],
                    product_category=category['category'],
                    product_type=item['type'],
                    product_price=item['price']
                )
                session.add(product)

    session.commit()

    # Creating fake data and inserting into the session
    for _ in range(no_rec):
        user = User(
            user_id=str(uuid.uuid4()),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.address(),
            age=fake.random_int(min=18, max=100),
            email=fake.email()
        )

        # Randomly select a product from the products list
        selected_product_name = choice(list(product_dict.keys()))
        selected_product_id = product_dict[selected_product_name]

        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            user_id=user.user_id,
            product_id=selected_product_id,
            transaction_date=fake.date_time_this_decade().date()
        )
        
        session.add(user)
        session.add(transaction)

    session.commit()
    logging.info("Data committed to the database.")