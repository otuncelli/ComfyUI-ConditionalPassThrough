from .conditional_passthrough_node import ConditionalPassThrough

NODE_CLASS_MAPPINGS = {
    "ConditionalPassThrough": ConditionalPassThrough,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConditionalPassThrough": "Conditional Pass-Through 🔀",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
