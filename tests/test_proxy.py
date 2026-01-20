# Basic test for proxy server
import os

def test_log_file():
    log_path = '../logs/traffic.log'
    assert os.path.exists(log_path), "Log file does not exist. Run the proxy and simulate traffic first."
    with open(log_path) as f:
        lines = f.readlines()
        assert len(lines) > 0, "Log file is empty."
    print("Test passed: Log file has entries.")

if __name__ == "__main__":
    test_log_file()
