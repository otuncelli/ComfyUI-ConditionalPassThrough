# Conditional Pass-Through 🔀

A [ComfyUI](https://github.com/comfy-org/comfyui) custom node that gates any value through based on the presence of a second input — letting you build chainable conditional pipelines without boolean outputs.

---

## How it works

```
value     ──┐
             ├──► [Conditional Pass-Through] ──► value  (or None)
condition ──┘
```

| condition wired? | output |
|---|---|
| ✅ Yes (any value) | `value` passed through unchanged |
| ❌ No / disconnected | `None` |

The output type mirrors `value` exactly, so the result plugs straight into any downstream node — or into another gate.

---

## Install

### Option A — Manual
1. Copy the `ComfyUI-ConditionalPassThrough/` folder into your `ComfyUI/custom_nodes/` directory:
   ```
   ComfyUI/
   └── custom_nodes/
       └── ComfyUI-ConditionalPassThrough/
           ├── __init__.py
           ├── conditional_passthrough_node.py
           └── README.md
   ```
2. Restart ComfyUI.

### Option B — Git clone
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/otuncelli/comfyui_conditional_passthrough
```
Then restart ComfyUI.

The node appears under **`utils/logic`** as **"Conditional Pass-Through 🔀"**.

---

## Inputs & Outputs

| Pin | Type | Required | Description |
|---|---|---|---|
| `value` | `*` (any) | ✅ | The payload to forward — image, latent, string, number, anything |
| `condition` | `*` (any) | ❌ | Gate trigger — connect anything; its presence opens the gate |
| ➡ `value` | `*` (any) | — | The forwarded `value`, or `None` if gate is closed |

---

## Use cases

### 1. Simple guard — only decode if a latent exists
```
[KSampler] ──value──► [Gate] ──► [VAE Decode]
                          ▲
                     [some condition]
```

### 2. Chained gates — all conditions must be met
Run downstream processing only when multiple upstream steps have all produced output:

```
[KSampler A] ──value──► [Gate 1] ──► [Gate 2] ──► [VAE Decode]
                             ▲             ▲
                        [Result B]    [Result C]
```
Both Gate 1 and Gate 2 must be open for the latent to reach the decoder.

### 3. Optional style injection
```
[Base latent] ──value──► [Style Gate] ──► [KSampler]
                               ▲
                        [Style prompt]   ← leave disconnected to skip
```
Swap a style in or out simply by wiring/unwiring the condition — no need to rebuild the graph.

---

## Compatibility

- ComfyUI (any recent version supporting wildcard `"*"` inputs)
- No extra dependencies — pure Python, no pip installs needed
- Works alongside ImpactPack, rgthree, and other logic node packs

---

## License

MIT — do whatever you like with it.
