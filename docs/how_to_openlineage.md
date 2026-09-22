# Getting Started with OpenLineage

We had to do some additional setup steps to get https://openlineage.io/getting-started/ to work.

- Could not install WSL2 on work laptop, so used https://github.com/features/codespaces instead that has docker pre-installed
- Additional steps for github Codespace:
  - sudo sysctl -w vm.max_map_count=262144
  - Switch to legacy: sudo update-alternatives --config iptables & sudo update-alternatives --config ip6tables
