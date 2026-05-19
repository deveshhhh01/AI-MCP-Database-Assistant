import json
from fastmcp import FastMCP
from utils.db import execute_query
from utils.security import is_safe_query

# Create MCP server
mcp = FastMCP("SQLite MCP Server")

@mcp.tool()
def run_sql_query(query: str):

    try:

        # Validate query
        if not is_safe_query(query):

            return json.dumps({
                "success": False,
                "error": "Unsafe SQL query blocked."
            })

        # Execute query
        result = execute_query(query)

        return json.dumps({
            "success": True,
            "data": result
        })

    except Exception as e:

        return json.dumps({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    mcp.run()