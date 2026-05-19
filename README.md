AI Powered MCP Database Assistant

This project is an AI-powered database assistant developed using Python, FastMCP, Gemini AI, and SQLite. The main goal of this project is to allow users to interact with a database using natural language instead of writing SQL queries manually.

Users can ask questions like:

- Show employees from IT department
- Who has highest salary?
- Show employees with salary greater than 70000
- Display employees with more than 5 years experience

The AI model understands the question, converts it into an SQL query, and retrieves the required data from the database using MCP tools.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project Objective

The purpose of this project is to understand how AI models, MCP architecture, databases, and asynchronous communication work together in a real-world application.

This project demonstrates:

• Natural Language Processing  
• AI-generated SQL queries  
• MCP Client-Server communication  
• Database integration  
• Async programming in Python  
• Tool-based architecture  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Technologies Used

• Python  
• FastMCP  
• Gemini AI  
• SQLite  
• Asyncio  
• dotenv  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project Structure

mcp_database_server/

├── ai_client.py  
├── server.py  
├── db.py  
├── sample_data.py  
├── requirements.txt  
├── README.md  
├── .env  
├── .gitignore  

├── database/  
│   └── employee.db  

└── screenshots/  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

How the Project Works

Step 1 — User Input

The user asks a question in normal English language.

Example:

Show employees from IT department

Step 2 — Gemini AI Processing

The question is sent to Gemini AI.

Gemini analyzes the prompt and generates an SQL query.

Example:

SELECT * FROM employees WHERE department='IT';

Step 3 — MCP Client Communication

The generated SQL query is passed from ai_client.py to the MCP server using FastMCP client communication.

Step 4 — MCP Server Execution

The MCP server receives the query and calls database functions from db.py.

Step 5 — Database Interaction

SQLite database executes the query and returns the matching records.

Step 6 — Final Response

The result is displayed back to the user in a readable format.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Important Files Explanation

ai_client.py

This is the main client-side file.

Responsibilities:

• Takes user input  
• Sends prompt to Gemini AI  
• Receives generated SQL query  
• Connects with MCP server  
• Displays final response  

server.py

This file creates the MCP server.

Responsibilities:

• Registers MCP tools  
• Receives requests from client  
• Executes database operations  
• Returns query results  

db.py

Handles all database-related operations.

Responsibilities:

• SQLite connection  
• SQL query execution  
• Fetching records  
• Returning database results  

sample_data.py

Used for inserting sample employee records into the SQLite database.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Why MCP is Used

MCP (Model Context Protocol) helps in structured communication between AI models and tools.

Instead of directly accessing the database from AI, MCP acts as a bridge between:

• AI Model  
• Database Tools  
• External Services  

Benefits of MCP:

• Better modularity  
• Secure tool execution  
• Scalable architecture  
• Easy integration with multiple tools  
• Clean separation of client and server  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Why Async Programming is Used

Async programming allows the system to handle operations without blocking execution.

In this project, async programming helps while:

• Waiting for AI responses  
• Communicating with MCP server  
• Executing external operations  

Benefits:

• Faster execution  
• Better performance  
• Non-blocking architecture  
• Improved scalability  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Features

• Natural language to SQL conversion  
• AI-generated database queries  
• MCP-based architecture  
• SQLite integration  
• Async communication  
• Dynamic query handling  
• Easy to extend and modify  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sample Queries

Show all employees

Show employees with salary greater than 80000

Who has highest salary?

Show employees from HR department

Display employees with more than 5 years experience

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Installation Steps

1. Clone Repository

git clone <repository-url>

2. Move into Project Folder

cd mcp_database_server

3. Install Dependencies

pip install -r requirements.txt

4. Create .env File

GEMINI_API_KEY=your_api_key_here

5. Run MCP Server

python server.py

6. Run AI Client

Open another terminal and run:

python ai_client.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Output Example

User Input:

Show employees from IT department

Generated SQL:

SELECT * FROM employees WHERE department='IT';

Final Output:

Rahul Sharma  
Sneha Joshi  
Neha Singh  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Challenges Faced During Development

• Handling AI-generated SQL formatting  
• Managing async communication  
• MCP client-server integration  
• Database connection handling  
• Error handling for invalid queries  
• API quota limitations  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Future Improvements

• Add support for MySQL/PostgreSQL  
• Web interface integration  
• Authentication system  
• Query history tracking  
• Multiple database support  
• Better prompt engineering  
• Deployment using Docker  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Learning Outcomes

Through this project, I learned:

• MCP architecture and workflow  
• AI and database integration  
• Async programming concepts  
• SQLite database handling  
• Prompt engineering  
• Client-server communication  
• Tool-based AI systems  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Author

Developed by Devesh Mandalkar as a learning project to explore AI-powered database systems using MCP architecture and Gemini AI.
