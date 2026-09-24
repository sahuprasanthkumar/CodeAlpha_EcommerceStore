import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

def run_seed():
    print("Seeding database...")

    # Create Superuser / Demo accounts
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Created superuser: admin / admin123")

    if not User.objects.filter(username='demo_user').exists():
        demo_user = User.objects.create_user('demo_user', 'demo@example.com', 'demo123')
        demo_user.first_name = "Alex"
        demo_user.last_name = "Morgan"
        demo_user.save()
        print("Created demo user: demo_user / demo123")

    # Categories
    categories_data = [
        {'name': 'Audio & Headphones', 'slug': 'audio-headphones', 'icon': 'bi-headphones', 'description': 'Immersive sound, noise cancelling, and true wireless freedom.'},
        {'name': 'Smart Wearables', 'slug': 'smart-wearables', 'icon': 'bi-smartwatch', 'description': 'Track health, receive notifications, and optimize your fitness daily.'},
        {'name': 'Laptops & Computing', 'slug': 'laptops-computing', 'icon': 'bi-laptop', 'description': 'High-performance machines for developers, creators, and power users.'},
        {'name': 'Photography & Video', 'slug': 'photography-video', 'icon': 'bi-camera', 'description': 'Pro grade lenses, cameras, and studio-grade cinematic gear.'},
        {'name': 'Smart Home & IoT', 'slug': 'smart-home-iot', 'icon': 'bi-house-gear', 'description': 'Automate your lighting, security, and climate effortlessly.'},
    ]

    cat_map = {}
    for cat in categories_data:
        c, created = Category.objects.get_or_create(
            slug=cat['slug'],
            defaults={'name': cat['name'], 'icon': cat['icon'], 'description': cat['description']}
        )
        cat_map[cat['slug']] = c

    # Products
    products_data = [
        {
            'category': cat_map['audio-headphones'],
            'name': 'AeroSound Pro Wireless ANC Headphones',
            'description': 'Studio-quality acoustic architecture with Active Noise Cancellation, 40-hour battery life, and crystal-clear microphone beamforming for work and entertainment.',
            'price': 199.99,
            'original_price': 249.99,
            'stock': 25,
            'rating': 4.9,
            'reviews_count': 64,
            'is_featured': True,
            'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop&q=80',
        },
        {
            'category': cat_map['audio-headphones'],
            'name': 'PulseTrue Wireless Earbuds with Wireless Case',
            'description': 'Ultra-compact earbuds featuring IPX7 water resistance, transparent audio pass-through mode, and instant Bluetooth 5.3 auto-pairing.',
            'price': 79.99,
            'original_price': 99.99,
            'stock': 40,
            'rating': 4.7,
            'reviews_count': 38,
            'is_featured': False,
            'image_url': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800&auto=format&fit=crop&q=80',
        },
        {
            'category': cat_map['smart-wearables'],
            'name': 'Apex Ultra Titanium Fitness Smartwatch',
            'description': 'Aerospace-grade titanium casing, dual-frequency precision GPS, ECG cardiac sensor, and up to 7 days of non-stop battery on a single charge.',
            'price': 299.99,
            'original_price': 349.99,
            'stock': 15,
            'rating': 4.8,
            'reviews_count': 52,
            'is_featured': True,
            'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&auto=format&fit=crop&q=80',
        },
        {
            'category': cat_map['smart-wearables'],
            'name': 'FitBand Orbit Health Tracker',
            'description': 'Minimalist, lightweight sleep and oxygen saturation tracker designed for 24/7 continuous health tracking with silent haptic alarms.',
            'price': 49.99,
            'original_price': 69.99,
            'stock': 30,
            'rating': 4.5,
            'reviews_count': 29,
            'is_featured': False,
            'image_url': 'https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=800&auto=format&fit=crop&q=80',
        },
        {
            'category': cat_map['laptops-computing'],
            'name': 'ZenithBook 16 Pro Creator Laptop',
            'description': 'Powered by cutting edge 14-core processor, 32GB LPDDR5X RAM, 1TB NVMe Gen4 SSD, and a breathtaking 3.2K 120Hz OLED edge-to-edge display.',
            'price': 1499.99,
            'original_price': 1699.99,
            'stock': 10,
            'rating': 4.9,
            'reviews_count': 81,
            'is_featured': True,
            'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&auto=format&fit=crop&q=80',
        },
        {
            'category': cat_map['laptops-computing'],
            'name': 'KeyCraft Mechanical Wireless Keyboard RGB',
            'description': 'Hot-swappable lubricated mechanical switches, PBT dye-sub keycaps, aluminum top plate, and customizable per-key RGB backlighting.',
            'price': 119.99,
            'original_price': 139.99,
            'stock': 22,
            'rating': 4.8,
            'reviews_count': 45,
            'is_featured': False,
            'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&auto=format&fit=crop&q=80',
        },
        {
            'category': cat_map['photography-video'],
            'name': 'Lumix Pro 4K Mirrorless Cinema Camera',
            'description': 'Full-frame sensor delivering 4K 120fps video recording, dual native ISO, in-body 5-axis stabilization, and cinematic dynamic color profiles.',
            'price': 1299.99,
            'original_price': 1449.99,
            'stock': 8,
            'rating': 4.9,
            'reviews_count': 34,
            'is_featured': True,
            'image_url': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&auto=format&fit=crop&q=80',
        },
        {
            'category': cat_map['smart-home-iot'],
            'name': 'Aura Ambient Smart LED Light Bar Kit',
            'description': 'Dynamic monitor screen sync backlighting with 16 million colors, voice assistant control (Alexa / Google Assistant), and ambient music rhythm modes.',
            'price': 59.99,
            'original_price': 79.99,
            'stock': 50,
            'rating': 4.6,
            'reviews_count': 22,
            'is_featured': False,
            'image_url': 'https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=800&auto=format&fit=crop&q=80',
        },
    ]

    for p in products_data:
        Product.objects.get_or_create(
            name=p['name'],
            defaults=p
        )

    print("Database successfully seeded with categories and products!")

if __name__ == '__main__':
    run_seed()
