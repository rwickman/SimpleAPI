
apiDomain = "muac-api.cfialab.net"
devPort = ":4000"
protocol = "http"

API_BASE = f"{protocol}://{apiDomain}{devPort}/api"


USERS_API = f"{API_BASE}/user"
NOTIFICATION_API = f"{API_BASE}/notifications"
ACCESS_API = f"{API_BASE}/documents"

REGISTER_ENDPOINT = f"{USERS_API}/register"
LOGIN_ENDPOINT = f"{USERS_API}/login"

REQUESTS_ENDPOINT = f"{API_BASE}/documents/approval-requests"

ACCESS_ENDPOINT = f"{API_BASE}/documents/update-access"