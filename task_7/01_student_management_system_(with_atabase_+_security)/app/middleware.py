from __future__ import annotations
import os
import time
from starlette.middleware.base import BaseHTTPMiddleware


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logfile: str = "./logs/requests.log"):
        super().__init__(app)
        self.logfile = logfile
        os.makedirs(os.path.dirname(self.logfile), exist_ok=True)

    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = (time.time() - start) * 1000
        line = f"{request.client.host} - {request.method} {request.url.path} {response.status_code} {duration:.1f}ms\n"
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(line)
        return response
