from prometheus_client import Counter, start_http_server
from dictionary import Dictionary
import time

# Prometheus counter
lookup_counter = Counter(
    "dictionary_requests_total", "Number of dictionary lookups", ["result"]
)

# Start a Prometheus HTTP server on port 8000
start_http_server(8000)

# Dictionary instance
d = Dictionary()

def lookup(word):
    definition = d.look(word)
    if "Can't find entry" in definition:
        lookup_counter.labels(result="miss").inc()
    else:
        lookup_counter.labels(result="hit").inc()
    return definition

# 👇 This loop is crucial, otherwise the script exits immediately
if __name__ == "__main__":
    print("🚀 Metrics server running on http://localhost:8000/metrics")
    while True:
        time.sleep(1)
