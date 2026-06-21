"""
ComfyUI Custom Node: Conditional Pass-Through Gate
===================================================
Passes `value` through only when `condition` is also connected/non-None.
Output type mirrors the input, so nodes can be chained freely.

  value      → the payload you want to forward (any type)
  condition  → any input — its mere PRESENCE (non-None) acts as the gate

  output     → `value` if condition is present, else None (blocked)
"""


class ConditionalPassThrough:
    """
    Gate that forwards `value` unchanged when `condition` is wired up.
    Because the output is the same wildcard type as `value`, you can
    chain multiple gates or feed the result directly into downstream nodes.
    """

    CATEGORY = "utils/logic"
    FUNCTION = "evaluate"
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("value",)

    OUTPUT_NODE = False

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("*",),       # the payload to pass through
            },
            "optional": {
                "condition": ("*",),   # presence = True, absence = False
            },
        }

    def evaluate(self, value, condition=None):
        if condition is not None:
            return (value,)        # gate open  → forward value as-is
        return (None,)             # gate closed → send None downstream
