import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("database.db")

# Create cursor object
cursor = conn.cursor()

# Delete old employees table if exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Create employees table
cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    experience INTEGER NOT NULL
)
""")

# Sample employee data
employees = [
    ("Rahul Sharma", "IT", 75000, 5),
    ("Priya Patel", "HR", 60000, 3),
    ("Amit Verma", "Finance", 80000, 7),
    ("Sneha Joshi", "IT", 95000, 8),
    ("Karan Mehta", "Marketing", 50000, 2),
    ("Neha Singh", "IT", 72000, 4),
    ("Devesh Mandalkar", "IT", 92000, 4),
    ("Mani Joshi", "CMA", 88000, 6),
    ("Anjali Rao", "HR", 65000, 5),
    ("Shubham Chaudhari", "IT", 20000, 1),
    ("Rohit Jain", "Finance", 85000, 6),
    ("Lallu Bari", "IPS", 200000000, 4),
    ("Vikas Deshmukh", "Sales", 58000, 3),
    ("Pooja Kulkarni", "Marketing", 67000, 4),
    ("Arjun Nair", "IT", 99000, 9),
    ("Meera Iyer", "Finance", 76000, 5),
    ("Sahil Khan", "Operations", 54000, 2),
    ("Ritika Chawla", "HR", 71000, 6),
    ("Aditya Roy", "IT", 88000, 7),
    ("Simran Kaur", "Design", 63000, 3),
    ("Yash Patil", "Sales", 61000, 4),
    ("Nikita Sharma", "Finance", 93000, 8),
    ("Harsh Gupta", "Operations", 57000, 2),
    ("Tanvi Desai", "IT", 81000, 5),
    ("Mohit Agarwal", "Marketing", 69000, 4),
    ("Ayesha Siddiqui", "HR", 74000, 6),
    ("Rohan Kulkarni", "IT", 105000, 10),
    ("Ishita Bose", "Design", 72000, 5),
    ("Manav Bansal", "Sales", 64000, 3),
    ("Kritika Naidu", "Finance", 87000, 7),
    ("Dev Malhotra", "Cyber Security", 98000, 8),
    ("Sanya Kapoor", "Business Analyst", 79000, 5)
]

# Insert sample data
cursor.executemany("""
INSERT INTO employees (name, department, salary, experience)
VALUES (?, ?, ?, ?)
""", employees)

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!") 

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

print(rows)