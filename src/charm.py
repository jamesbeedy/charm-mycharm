#!/usr/bin/env python3
from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

import logging
import subprocess

logger = logging.getLogger()


class MycharmCharm(CharmBase):
    """Mycharm lifecycle events."""

    def __init__(self, *args):
        """Init _stored attributes and interfaces, observe events."""
        super().__init__(*args)

        event_handler_bindings = {
            self.on.install: self._on_install,
            self.on.remove: self._on_remove,
        }
        for event, handler in event_handler_bindings.items():
            self.framework.observe(event, handler)

    def _on_install(self, event):
        """Perform installation operations for mycharm."""
        subprocess.run("apt install neovim -y".split())
        self.unit.status = ActiveStatus("NeoVim Installed")

    def _on_remove(self, event):
        """Perform removal of neovim."""
        subprocess.run("apt remove --purge neovim -y".split())


if __name__ == "__main__":
    main(MycharmCharm)
