from rally.benchmark.scenarios import base
from rally.benchmark import utils as bench_utils
from rally.benchmark import validation
from rally import osclients


class CustomScenarioPlugin(base.Scenario):
    """Sample plugin which lists flavors."""

    @base.atomic_action_timer("list_flavors")
    def _list_flavors(self):
        """Sample of usage clients - list flavors

        You can use self.context, self.admin_clients and self.clients which are
        initialized on scenario instance creation.
        """
        self.clients("nova").flavors.list()

    @base.atomic_action_timer("list_flavors_as_admin")
    def _list_flavors_as_admin(self):
        """The same with admin clients."""
        self.admin_clients("nova").flavors.list()

    @base.scenario()
    def list_flavors(self):
        """List flavors."""
        self._list_flavors()
        self._list_flavors_as_admin()
