from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamablehttp_client
import asyncio
import traceback

server_params = "http://localhost:8000/mcp"

async def main():
    try:
        async with streamablehttp_client(server_params) as (read, write, _):
            print("Client connected to server.....")
            async with ClientSession(read, write) as session:
                print("Initializing client session.....")
                await session.initialize()

                # tool call
                print("Initializing tool.....")
                tools = await session.list_tools()
                print("Available tools:", tools)

    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())