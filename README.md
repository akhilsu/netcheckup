# netcheckup

**netcheckup** is a lightweight internet health diagnostic tool. It can check DNS resolution time, ping latency, and common port connectivity.

## Usage

```bash
netcheckup
```

[![PyPI version](https://badge.fury.io/py/netcheckup.svg)](https://pypi.org/project/netcheckup/)


# 🧠 netcheckup

[![PyPI version](https://badge.fury.io/py/netcheckup.svg)](https://pypi.org/project/netcheckup/)
[![Python version](https://img.shields.io/pypi/pyversions/netcheckup.svg)](https://pypi.org/project/netcheckup/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A simple CLI tool to check your internet health — DNS resolution, ping, and port reachability in one shot!

---

## 🚀 Features

- ✅ DNS resolution check for popular domains
- ✅ ICMP Ping check for global IPs like `8.8.8.8`
- ✅ Port connectivity check for standard services
- ✅ Fast, Pythonic, and fully terminal-based
- ✅ CLI with one command: `netcheckup`

---

## 📦 Installation

Install directly from PyPI:

```bash
pip install netcheckup
```

After installation, just run:
```bash
netcheckup
```

just run:
```bash
netcheckup speed
```

```bash
from netcheckup import main

main()
```

```bash
from netcheckup import ping_check

print(ping_check(["8.8.8.8"]))
```

```bash
netcheckup ping --host 8.8.8.8 1.1.1.1 --count 4
```

```bash
from netcheckup import dns_check

print(dns_check(["google.com"]))
```

```bash
netcheckup dns --domain example.com google.com
```

```bash
from netcheckup import port_check

print(port_check(host="8.8.8.8", ports=[53, 443]))
```

```bash
netcheckup port --host 8.8.8.8 --ports 53 443
```

```bash
netcheckup all
```