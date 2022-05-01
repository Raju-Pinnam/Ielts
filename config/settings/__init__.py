import os
ENV = os.environ.get("ENV", "prod")

if ENV in ("local", "qa", "prod"):
    exec(f"from .{ENV} import *")
