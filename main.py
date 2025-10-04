from fastmcp import FastMCP
import json

mcp=FastMCP("demo server")

@mcp.tool
def add(a:int,b:int)-> int:
    return a+b

@mcp.tool
def sub(a:int,b:int)-> int:
    return a-b

@mcp.resource("info://server")
def server_info()->str:
    info={
        "name":"Simple calculator",
        "version":"1.2.1",
        "description":"Basic calculation",
        "tools":['abb','sub'],
        "author":"sumanth habib"
    }
    return json.dumps(info,indent=2)
    

if __name__ == "__main__":
    mcp.run(transport='http',host="0.0.0.0",port=8000)
