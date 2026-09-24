# CodeAlpha_EcommerceStore 🛒

**Full Stack Development Internship Project — CodeAlpha (Task 1)**

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, responsive, full-stack E-Commerce web application developed for the **CodeAlpha Full Stack Web Development Internship**. Features full user authentication, dynamic product catalog, category filters, interactive shopping cart, checkout system, order processing, and administrative controls.

---

## ✨ Features Implemented

1. **User Authentication & Profiles**
   - User registration with validation and encrypted passwords
   - User login and logout sessions
   - Authenticated user order history dashboard

2. **Product Catalog & Browsing**
   - Responsive multi-device product grid with card hover effects
   - Category filtering (Audio, Smart Wearables, Laptops, Photography, Smart Home)
   - Real-time search by keyword, title, or category description
   - Sorting by Price (Low to High, High to Low), Customer Rating, and Newest

3. **Product Details Page**
   - Detailed product view with high-resolution imagery and specs
   - Stock availability indicators (In Stock vs. Out of Stock)
   - Dynamic quantity selector (+ / - controls)
   - Customer star ratings and reviews counter
   - Related products recommendation carousel

4. **Interactive Shopping Cart**
   - Session-based persistent cart
   - AJAX "Add to Cart" with non-intrusive toast notifications
   - In-cart quantity modifications and real-time subtotal calculation
   - Item removal and empty cart states
   - Free shipping qualification indicator (Free over $100)

5. **Order Processing & Checkout**
   - Clean checkout form with delivery address validation
   - Order summary with itemized breakdown and shipping fee calculations
   - Order placement workflow that creates persistent database records and updates product stock
   - Printable order invoice / receipt page with unique Order ID and tracking status

6. **Django Administration Panel**
   - Full management of Categories, Products, and Customer Orders via `/admin/`

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3, Bootstrap Icons
- **Backend:** Python, Django 6.1 (MTV Architecture)
- **Database:** SQLite (ORM-managed)
- **Session & Storage:** Django Session Framework

---

## 🚀 Getting Started & Setup Instructions

### 1. Prerequisites
- Python 3.10+ installed on your system.

### 2. Installation
Open your terminal in the `CodeAlpha_EcommerceStore` directory:

```bash
# Optional: create a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install Django
pip install django
```

### 3. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed Initial Sample Data
Run the automated seed script to populate products, categories, and demo accounts:
```bash
python seed_data.py
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

Now open your browser and navigate to:
👉 **`http://127.0.0.1:8000/`**

---

## 🔑 Demo Credentials

- **Admin Account (Full Management):**
  - Username: `admin`
  - Password: `admin123`
  - Access Admin Panel at: `http://127.0.0.1:8000/admin/`

- **Demo Customer Account:**
  - Username: `demo_user`
  - Password: `demo123`

*(You can also register a brand new account at `/register/`)*

---

## 📁 Project Structure

```
CodeAlpha_EcommerceStore/
│
├── ecommerce_site/         # Core Django Project Settings & Routing
│   ├── settings.py         # App configurations, templates & static dirs
│   ├── urls.py             # Main routing
│   └── wsgi.py
│
├── store/                  # E-Commerce Application Module
│   ├── models.py           # Category, Product, Order, OrderItem
│   ├── views.py            # Business logic (cart, products, checkout, auth)
│   ├── urls.py             # Store endpoints
│   ├── forms.py            # Auth & Checkout forms
│   ├── cart.py             # Session cart helper
│   ├── context_processors.py # Cart count & nav categories
│   └── admin.py            # Django Admin registration
│
├── templates/              # HTML5 Templates
│   ├── base.html           # Master layout with responsive navbar & footer
│   └── store/
│       ├── product_list.html
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       ├── order_detail.html
│       ├── order_history.html
│       ├── login.html
│       └── register.html
│
├── static/
│   ├── css/style.css       # Custom design system
│   └── js/main.js          # AJAX cart, toast alerts, quantity counters
│
├── seed_data.py            # Database populator
├── manage.py
└── README.md
```

---

## 📹 Video Walkthrough & LinkedIn Presentation Guide

When recording your project video for LinkedIn (as required by CodeAlpha):
1. **Introduction:** Mention your name and that this is Task 1 (E-Commerce Store) for the CodeAlpha Full Stack Internship.
2. **Product Browsing:** Demonstrate categories, keyword search, and sorting.
3. **Cart & Details:** Open a product, select quantity, add to cart with instant feedback.
4. **Order Placement:** Navigate to checkout, fill shipping details, and place the order.
5. **Receipt & Dashboard:** Show the generated invoice receipt and user order history.
6. **Admin Panel:** Briefly show the Django admin interface where products and orders are organized.
