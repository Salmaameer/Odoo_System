# Mini Odoo – Sale Order System

## 📌 Project Overview
This project is a mini simulation of the Sales module in Odoo.  
It covers the main flow starting from creating a customer, adding products, creating a sale order, and calculating totals automatically.

The goal of the project is to understand how Odoo models work, how relations link the system together, and how workflows operate inside a real-life business module.

---

## 📂 Project Structure

### **1. Models Included**

#### 🧍 Customer Model
- Stores customer data: **name, email, phone**
- Linked to sale orders through a Many2one field

#### 📦 Product Model
- Contains product details: **name, price, category**
- Used when creating sale order lines

#### 🧾 Sale Order Model
- Main core of the system
- Linked to customers and contains multiple order lines
- Automatically calculates totals
- Has states: **draft → confirmed → delivered**

#### 🧮 Sale Order Line Model
- Stores each line of the sale order
- Linked to both product and sale order
- Auto-calculates subtotal (**price × quantity**)

---

## ⚙️ System Workflow

### **1. Create Customer**
Add a new customer to the system.

### **2. Add Products**
Add products with name, price, and category.

### **3. Create Sale Order (Draft)**
- Select customer  
- Add order lines  
- Subtotal is calculated automatically

### **4. Confirm Order**
- Order state changes to **Confirmed**
- Editing the order is disabled

### **5. Delivery**
- Final workflow step  
- Status changes to **Delivered**

### **6. Automatic Calculations**
- Subtotal on each order line  
- Total amount on the sale order  
- All computed fields update instantly  

---

## 🧪 Testing the Module

1. Open **Sales**
2. Create a new **Customer**
3. Create **Products**
4. Create a **Sale Order**
5. Add **Order Lines**
6. Confirm the order
7. Validate Delivery

### Expected Results:
- Automatic subtotal calculation  
- Automatic total calculation  
- Workflow state changes functioning correctly  

---

## 🧾 Author
Developed by: **Rahma Ayman & Salma Ameer**  
