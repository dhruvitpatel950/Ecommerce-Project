# 🛒 E-Shop | Multi-Vendor E-Commerce Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

**E-Shop** is a scalable, multi-vendor e-commerce web application built with **Django**. It features a robust **Role-Based Access Control (RBAC)** system that distinguishes between Customers and Sellers, ensuring secure and distinct workflows.

Unlike standard e-commerce demos, this project implements **location-based product availability**, allowing users to check delivery feasibility before purchase—a complex Many-to-Many relationship implementation.

---

## 🚀 Key Features

### 🔐 Security & Authentication
* **Role-Based Access Control (RBAC):** Distinct dashboards and permissions for **Customers** and **Sellers**.
    * *Sellers:* Can add, edit, and delete their own products.
    * *Customers:* Can browse, search, and purchase products.
* **Custom Authentication Backend:** Implemented a manual authentication backend (`accounts/backend.py`) for precise control over user login logic.
* **Route Protection:** Custom decorators (`@blocked_user_required`, `@seller_product_owner_required`) prevent unauthorized access to specific views.

### 📦 Product Management (Seller Side)
* **CRUD Operations:** Sellers have full control to Create, Read, Update, and Delete their products.
* **Inventory Management:** Real-time stock updates upon purchase.
* **Image Handling:** Secure image uploads using Django's media handling.

### 🛒 Shopping Experience (Customer Side)
* **Smart Search:** Advanced search functionality using `Q` objects to filter products by name or description.
* **Location-Based Availability:** Users can check if a product is deliverable to their city (utilizing complex `Many-to-Many` database relationships between Products and Cities).
* **Order History:** Customers can view their past purchases and order status in a dedicated profile section.
* **Buy Now Flow:** Streamlined purchase process with stock validation and order generation.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend Framework** | Python (Django 5.x) |
| **Architecture** | Django MVT (Model-View-Template) |
| **Database** | SQLite (Development) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Authentication** | Custom Auth Backend & Decorators |

---

## 📂 Project Structure

```bash
E-Commerce-Project/
├── accounts/          # User management, RBAC, Custom Auth
├── core/              # Core settings and utilities
├── products/          # Product CRUD, Categories, Search Logic
├── orders/            # Order processing, Availability checks
├── templates/         # Global HTML templates (Base, Navbar)
├── static/            # CSS, Images, JS
├── media/             # User-uploaded content (Product images)
├── manage.py          # Django entry point
└── requirements.txt   # Dependencies
