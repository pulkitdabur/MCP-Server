from mcp.server.fastmcp import FastMCP
import requests
from add_tool import AddRequest, AddResponse

mcp=FastMCP("ADD TOOL", port=8000, host="0.0.0.0")


@mcp.tool()
def add_tool_api(request: AddRequest):


	try:

		url = "http://localhost:8100/add"
		response = requests.post(url, json=request.model_dump(), timeout=10)
		response.raise_for_status()
		data = response.json()

		return AddResponse(**data)

	except requests.RequestException as e:

		print(f"Error fetching data from API: {e}")

		return ( "Failed to fetch data from API")

if __name__ == "__main__":
	mcp.run(transport="streamable-http")
