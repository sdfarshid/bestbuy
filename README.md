# Store Management System

This Python-based store management system offers functionality to manage products in a store, handle customer orders, and apply promotions, all through an interactive user interface.

---

## Features

### **1. Product Management:**
- **`Product` Class:**
   - Attributes: `name`, `price`, `quantity`, `active`, and `promotions`.
   - Supports actions such as:
      - Activating or deactivating a product based on availability.
      - Modifying product details (e.g., price, quantity).
      - Displaying product information.
   - Includes multiple product types:
      - **`NonStockedProduct`**: Products without physical stock, such as digital licenses.
      - **`LimitedProduct`**: Products with a maximum purchase limit per order.

### **2. Promotions:**
- Define and apply promotional discounts, including:
   - **`PercentDiscount`**: Applies a percentage-based discount.
   - **`SecondHalfPrice`**: Every second product is half-price.
   - **`ThirdOneFree`**: Buy 3, pay for 2.
- Products can have multiple promotions applied, calculated cumulatively.

### **3. Store Management:**
- **`Store` Class:**
   - Manage a collection of products with features like:
      - Adding and removing products.
      - Viewing all active products.
      - Calculating total quantity in stock.
      - Processing customer orders.

### **4. Interactive User Interface:**
- Menu options:
   1. List all products in the store.
   2. Show the total quantity of items in the store.
   3. Place an order by selecting products and quantities.
   4. Quit the application.

---

## How to Use

### **Setup:**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure Python 3.x is installed.

3. Install any DEV dependencies if required:
   ```bash
   pip install -r dev-requirements.txt
   ```

### **Run the Application:**
1. Navigate to the project directory.
2. Execute the main script:
   ```bash
   python main.py
   ```

---

## Functionalities

### **1. Listing Products:**
- Displays all active products in the store with their details, including applied promotions.

### **2. Total Quantity:**
- Summarizes the total quantity of items available in the store.

### **3. Order Placement:**
- Users can select products by their ID and specify the desired quantity.
- The system checks availability and applies relevant promotions.
- Total price is calculated, and inventory is updated after purchase.

---

## Sample Inventory
Upon startup, the application initializes with the following products:

| Product Name                | Price  | Quantity | Notes                       |
|-----------------------------|--------|----------|-----------------------------|
| MacBook Air M2              | $1450  | 100      |                             |
| Bose QuietComfort Earbuds   | $250   | 500      |                             |
| Google Pixel 7              | $500   | 250      |                             |
| Windows License             | $125   | 0        | Non-stocked product         |
| Shipping                    | $10    | 250      | Limited to 1 per order      |

---

## Code Structure

- **`products.py`**:
   - Defines product-related functionality and promotion logic.

- **`store.py`**:
   - Handles store operations, including inventory management and order processing.

- **`main.py`**:
   - Provides the user interface and serves as the entry point for the application.

---

## Testing

### **Unit Tests:**
- Run tests using `pytest`:
  ```bash
  pytest test_products.py
  ```

### **Functional Tests:**
1. Ensure product management operations (add, remove, modify) work correctly.
2. Validate correct application of multiple promotions on purchases.
3. Test quantity limits on `LimitedProduct` and out-of-stock handling.


---

## Example Usage

### **Product Promotions:**
- MacBook Air M2:
   - Second Half Price
   - 30% Off

### **Order Example:**
1. User selects MacBook Air M2 and orders 3 units.
2. The following calculations are performed:
   - Base price: \(1450 \times 3 = 4350\)
   - Second Half Price discount: \(1450 / 2 = 725\)
   - 30% Off discount: \(4350 \times 0.3 = 1305\)
   - Final price: \(4350 - 725 - 1305 = 2320\)
3. Total cost displayed: `$2320`.
4. Inventory updated to 97 units.

---
