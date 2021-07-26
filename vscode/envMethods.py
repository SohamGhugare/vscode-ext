class Env:
    def open_external(self, target):
        print(f"OE: {target}", flush=True, end="")

    @property
    def app_name(self):
        print(f"EP: appName", flush=True, end="")
        return input()

    @property
    def app_root(self):
        print(f"EP: appRoot", flush=True, end="")
        return input()

    @property
    def clipboard(self):
        print(f"EP: clipboard", flush=True, end="")
        return input()

    @property
    def is_new_app_install(self) -> bool:
        print(f"EP: isNewAppInstall", flush=True, end="")
        return eval(input().title())

    @property
    def is_telemetry_enabled(self) -> bool:
        print(f"EP: isTelemetryEnabled", flush=True, end="")
        return eval(input().title())

    @property
    def language(self):
        print(f"EP: language", flush=True, end="")
        return input()

    @property
    def machine_id(self):
        print(f"EP: machineId", flush=True, end="")
        return input()

    @property
    def remote_name(self):
        print(f"EP: remoteName", flush=True, end="")
        return input()

    @property
    def session_id(self):
        print(f"EP: sessionId", flush=True, end="")
        return input()

    @property
    def shell(self):
        print(f"EP: shell", flush=True, end="")
        return input()

    @property
    def ui_kind(self):
        print(f"EP: uiKind", flush=True, end="")
        return input()

    @property
    def uri_scheme(self):
        print(f"EP: uriScheme", flush=True, end="")
        return input()


env = Env()
