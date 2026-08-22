from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:float, b:float)-> float:
    """_summary_
    Add two numbers"""
    return a+b

@mcp.tool()
def multiply(a:float, b:float)-> float:
    """_summary_
    Multiply two numbers"""
    return a*b

@mcp.tool()
def subtract(a:float, b:float)-> float:
    """_summary_
    subtract two numbers"""
    return a-b

@mcp.tool()
def divide(a:float, b:float)-> float:
    """_summary_
    divide two numbers"""
    return a/b


if __name__ == "__main__":
    mcp.run(transport="stdio") 