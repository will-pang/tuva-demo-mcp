# Osler: The Tuva Project Demo + MCP

### 📦 Installation

Assuming you have [UV](https://docs.astral.sh/uv/getting-started/installation/) installed.

**Step 1: Clone and Navigate**

```bash
# Clone the repository
git clone https://github.com/will-pang/tuva-demo-mcp
cd m3
```

**Step 2: Create `UV` Virtual Environment**

```bash
# Create virtual environment
uv venv
```

**Step 3: Activate virtual environment**

```
source .venv/bin/activate
```

**Step 4: Install Osler**

```bash
uv sync
# Do not forget to use `uv run` to any subsequent commands to ensure you're using the `uv` virtual environment
```

`uv pip install -e .`

### 🗄️ Database Configuration

1. **Download demo database**:
   ```bash
   osler init
   ```
