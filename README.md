# 🛍️ E-Commerce Website

## 🚀 Project Overview
This is a fully functional e-commerce website built using Django. The platform allows users to browse products, add them to their cart, place orders, and manage their purchases. It also includes an admin panel for managing products and tracking orders.

## ✨ Features
- 📦 **Product Listing & Pagination**: Products are displayed with a limit of four per page, with navigation options.
- 🔎 **Search Functionality**: Users can search for products dynamically.
- 🛒 **Add to Cart & Dynamic Cart Updates**: Users can add products to their cart and see real-time updates.
- 💳 **Checkout Process**: Customers can enter their details and place an order.
- 📊 **Order Management**: Admins can view orders, track customer details, and monitor order totals.
- 🛠️ **Admin Panel**: Allows management of products, prices, and order details.

## 🛠️ Technologies Used
- **Backend**: Django, Python 🐍
- **Frontend**: HTML, CSS, JavaScript 🎨
- **Database**: SQLite / PostgreSQL 🗄️

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DS-Vijayapala/Django-E-Commerce-Site.git
   cd ecommerce-project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 🎯 Usage
- Open `http://127.0.0.1:8000/` in your browser.
- Browse products, search for items, and add them to your cart.
- Proceed to checkout and place an order.
- Log in as an admin to manage products and orders.

## 🔑 Admin Access
To create a superuser, run:
```bash
python manage.py createsuperuser
```
Then, log in at `http://127.0.0.1:8000/admin/`.

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## 📜 License
This project is licensed under the MIT License.

---


