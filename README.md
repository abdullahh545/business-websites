# Lahore Super Steel Door - Business Website

A business website built with **Django** for Lahore Super Steel Door, a steel fabrication and welding company based in Bahrain.  
The site provides a professional showcase of services, allows customers to make bookings online, and enables admins to manage services and bookings via the Django admin panel.

---

## 🚀 Features

- **Home Page**
  - Hero section introducing the company.
  - About Us with portfolio of past projects.
  - Responsive design with modern layout.

- **Services**
  - List of all services with details and pricing.
  - Service detail page with image, description, and status.
  - Admin users can **create, update, and delete services**.
  - Customers can only view and book services.

- **Bookings**
  - Customers can create bookings for services.
  - Each booking includes customer name, email, phone, service, and status.
  - Admin can **view, update, and delete bookings**.
  - Bookings displayed in a styled card layout.

- **Authentication**
  - Custom `User` model with **roles** (Admin, Customer).
  - Sign-up, login, and logout functionality.
  - Only authenticated users can create bookings.

- **Styling**
  - Custom CSS for different sections:
    - `base.css` → navigation, footer, homepage.
    - `service.css` → service pages.
    - `booking.css` → booking pages.
    - `login.css` and `signup.css` → authentication pages.
  - Mobile-friendly responsive design.
  - Cards for services, bookings, and portfolio items.

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x (Python 3.13)
- **Frontend:** HTML5, CSS3, Django Templates
- **Database:** SQLite (default, easy setup)
- **Authentication:** Django Auth with custom `User` model
- **Deployment-ready:** Static files setup

---

## 📂 Project Structure

Lahoresuper_steeldoor/
│── main_app/
│ ├── migrations/
│ ├── static/
│ │ ├── base.css
│ │ ├── service.css
│ │ ├── booking.css
│ │ ├── login.css
│ │ └── signup.css
│ ├── templates/
│ │ ├── base.html
│ │ ├── homepage.html
│ │ ├── service/
│ │ │ ├── service_list.html
│ │ │ ├── service_detail.html
│ │ │ ├── service_form.html
│ │ │ ├── service_confirm_delete.html
│ │ └── serviceBooking/
│ │ ├── serviceBooking_list.html
│ │ ├── serviceBooking_detail.html
│ │ ├── serviceBooking_form.html
│ │ └── serviceBooking_confirm_delete.html
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│── Lahoresuper_steeldoor/ (project settings)
│── manage.py


---

## ⚙️ Installation & Setup

- step: 🛠️ Clone the repository  
   git clone https://github.com/abdullahh545/business-websites.git
   cd business-websites

- step: 🐍 Create a virtual environment
      command: |
        python -m venv venv
        source venv/bin/activate   # 💻 Mac/Linux
        venv\Scripts\activate      # 🪟 Windows

    - step: 📦 Install dependencies
      command: pip install -r requirements.txt

    - step: 🗄️ Apply migrations
      command: |
        python manage.py makemigrations
        python manage.py migrate

    - step: 👤 Create superuser
      command: python manage.py createsuperuser

    - step: 🚀 Run development server
      command: python manage.py runserver

  url: 🌍 "http://127.0.0.1:8000/"

     👥 User Roles

Admin

Add, update, and delete services.

Manage bookings from customers.

Full access to Django admin panel.

Customer

Sign up, log in, and book services.

View services and booking status.


📸 Screenshots (Optional)

[![Homepage Screenshot](static/images/homepage.jpg)](static/images/homepage.jpg)


📞 Contact

Lahore Super Welding & Fabrication
📧 Email: info@lahoresupersteel.com

📞 Phone: +973 33248620
💬 WhatsApp: Chat with us
