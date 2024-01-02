```python
class AppIntegration:
    def __init__(self):
        # Initialize application integrations
        self.app_integrations = []

    def add_app_integration(self, integration):
        # Add an application integration
        self.app_integrations.append(integration)

    def start(self):
        # Start all application integrations
        for integration in self.app_integrations:
            if not integration.is_started():
                raise Exception(f"Application integration {integration.name} is not started!")

        print("All application integrations are started.")

    class AppIntegration:
        def __init__(self, name):
            self.name = name

        def is_started(self):
            # Check if the application integration is started
            # This is a placeholder and should be replaced with actual checks
            return True
```
