class ToolRegistry:
    def __init__(self):
        self._tools = {}
    def register(self, tool):
        self._tools[tool.spec.name] = tool
    def get(self, name):
        return self._tools.get(name)
    def list(self):
        return list(self._tools.values())
