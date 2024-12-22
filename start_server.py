#!/usr/bin/env python

import argparse
import ipaddress

import uvicorn

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start API gateway server")
    parser.add_argument("--host", type=ipaddress.ip_address, default="0.0.0.0", help="Interface to bind for API server")
    parser.add_argument("--port", type=int, default=8000, help="Port for API server")
    args = parser.parse_args()
    uvicorn.run("app.main:app", host=args.host.exploded, port=args.port, reload=True)
