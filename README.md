# ml-based-ddos-mitigation
## DDoS Mitigation System - Basic MVP

### Folders
- `proxy/` : Proxy server code
- `logs/` : Traffic and event logs
- `scripts/` : Utility scripts (e.g., for simulating traffic)
- `tests/` : Test scripts

### Getting Started
1. Run the proxy server from the `proxy/` folder:
	```bash
	python3 proxy/proxy.py
	```
2. In another terminal, simulate traffic:
	```bash
	python3 scripts/simulate_traffic.py
	```
3. Check logs in the `logs/` folder.
4. Run the test:
	```bash
	python3 tests/test_proxy.py
	```

### Next Steps
- Implement more advanced detection and logging.
