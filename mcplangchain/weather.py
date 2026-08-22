from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """get the weather based on the location"""
    if location.lower() == "chennai":
        return f"it's always sunny in {location}"
    elif location.lower() == "london":
            return f"it's always snowing in {location}"
    else:
            return f"it's always raining in {location}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")