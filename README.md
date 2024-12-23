# Store Management System

This is a simple Python-based store management system that allows managing products in a store and handling customer orders through a user-friendly interface.

## Features

1. **Product Class**:
    - Represents a product in the store with attributes such as name, price, quantity, and active status.
    - Methods to activate, deactivate, modify quantity, and display product details.

2. **Store Class**:
    - Manages a collection of products.
    - Supports adding/removing products, displaying available products, calculating total quantity, and processing orders.

3. **User Interface**:
    - Interactive menu to:
        1. List all products in the store.
        2. Show the total quantity of items in the store.
        3. Make an order by selecting products and quantities.
        4. Quit the application.

## How to Use

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure you have Python 3.x installed.

3. Install any dependencies (if applicable).

### Run the Application
1. Navigate to the project folder.
2. Execute the main script:
   ```bash
   python main.py
   ```

### Example Usage
- **List Products**: View all active products in the store.
- **Show Total Quantity**: Check how many items are available in total.
- **Make an Order**: Enter the product name and quantity to create an order. The system will calculate the total cost and update the inventory.

## Code Structure
- `products.py`: Contains the `Product` class and related functionality.
- `store.py`: Contains the `Store` class for managing the collection of products.
- `main.py`: User interface and entry point of the application.

## Sample Inventory
The application starts with a default inventory:
- MacBook Air M2: $1450, 100 units
- Bose QuietComfort Earbuds: $250, 500 units
- Google Pixel 7: $500, 250 units
