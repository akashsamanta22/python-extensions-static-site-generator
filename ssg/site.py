import sys
from pathlib import Path

from ssg import extensions, hooks


class Site:
    def __init__(self, source, dest, parsers=None):
@@ -27,12 +29,16 @@ def run_parser(self, path):
            )

    def build(self):
        extensions.load_bundled()
        hooks.event("collect_files", self.source, self.parsers)
        hooks.event("start_build")
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
        hooks.event("stats")

    @staticmethod
    def error(message):