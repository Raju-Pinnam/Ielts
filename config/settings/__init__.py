import os
ENV = os.environ.get("ENV", "local")

if ENV in ("local", "qa", "prod"):
    exec(f"from .{ENV} import *")
