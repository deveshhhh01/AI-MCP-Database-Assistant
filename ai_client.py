import os
import re
import json
import asyncio
from dotenv import load_dotenv

from google import genai
from fastmcp import Client

# Load environment variables
load_dotenv()

# Check API key loaded
print("API Key Loaded:", os.getenv("GEMINI_API_KEY") is not None)

SYSTEM_PROMPT = """
You are an SQLite SQL expert.

Generate ONLY valid SQLite SELECT queries.

STRICT RULES:
1. Return ONLY SQL query
2. Never return explanations
3. Never use markdown
4. Never use ```sql
5. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE
6. Always close quotes properly
7. Table name is employees

employees columns:
- id
- name
- department
- salary
- experience

Examples:

User Question:
Show all employees

SQL:
SELECT * FROM employees;

User Question:
Show records of Aditya Roy

SQL:
SELECT * FROM employees WHERE name = 'Aditya Roy';

User Question:
Show Finance department employees

SQL:
SELECT * FROM employees WHERE department = 'Finance';
"""

def extract_sql(text: str):
    """
    Extract SQL query from Gemini response.
    """

    # Remove markdown formatting
    text = re.sub(r"```sql", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Remove extra spaces/newlines
    text = text.strip()

    # Remove unwanted ending quotes
    text = re.sub(r"[\"']+$", "", text)

    return text


async def main():

    # Create Gemini client
    gemini_client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    # Connect MCP client
    async with Client("server.py") as mcp_client:

        while True:

            question = input("\nAsk Question: ").strip()

            # Exit condition
            if question.lower() == "exit":
                print("\nExiting...")
                break

            # Greeting handling
            greetings = ["hi", "hello", "hey"]

            if question.lower() in greetings:
                print("\nHi! Ask me questions related to the employee database.")
                continue

            # Database-related keywords
            database_keywords = [
                "employee",
                "employees",
                "salary",
                "department",
                "experience",
                "name",
                "record",
                "records",
                "details",
                "show",
                "list",
                "all",
                "finance",
                "hr",
                "marketing",
                "sales",
                "operations",
                "design",
                "business analyst",
                "it"
            ]

            # Check if question is database related
            if not any(word in question.lower() for word in database_keywords):
                print("\nThis information is not available in the employee database.")
                continue

            try:

                # Generate SQL prompt
                prompt = f"""
{SYSTEM_PROMPT}

User Question:
{question}
"""

                # Generate SQL using Gemini
                response = gemini_client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                # Extract SQL query
                sql_query = extract_sql(response.text)

                # Fix unclosed quotes automatically
                if sql_query.count("'") % 2 != 0:
                    sql_query += "'"

                # Ensure query ends with semicolon
                if not sql_query.endswith(";"):
                    sql_query += ";"

                # Debug SQL (optional)
                print("\nGenerated SQL:")
                print(sql_query)

                # Call MCP tool
                result = await mcp_client.call_tool(
                    "run_sql_query",
                    {"query": sql_query}
                )

                # Extract MCP response
                response_text = result[0].text

                # Convert JSON string to dictionary
                data = json.loads(response_text)

                # Check query success
                if data["success"]:

                    rows = data["data"]

                    if rows:

                        print("\nAnswer:\n")

                        for index, row in enumerate(rows, start=1):

                            print(f"Record {index}")

                            for key, value in row.items():
                                print(f"{key}: {value}")

                            print("-" * 30)

                    else:
                        print("\nNo matching employee found in the database.")

                else:
                    print("\nDatabase query failed.")
                    print(data.get("error", "Unknown database error"))

            except Exception as e:

                error_message = str(e)

                if "429" in error_message:
                    print("\nAPI quota exceeded. Please wait and try again later.")

                else:
                    print("\nError:")
                    print(error_message)


if __name__ == "__main__":
    asyncio.run(main())