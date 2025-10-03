# MCP-Server

A minimal Python-based **Model Context Protocol (MCP) server** with a simple client example.  
This project demonstrates how to expose tools via MCP and interact with them from a client.

## Features
- Example MCP server (`mcp_server.py`)
- Example MCP client (`mcp_client.py`)
- Tool API Config (`add_tool.py`)

## Quickstart
```bash
git clone https://github.com/pulkitdabur/MCP-Server.git
cd MCP-Server
python add_tool.py    # start Tool API
python mcp_server.py    # start server
python mcp_client.py    # run client
