from rally.benchmark.scenarios import base
from rally.benchmark import utils as bench_utils
from rally.plugins.openstack.scenarios.custom import utils as customutils


class CustomKeystone(customutils.CustomKeystoneScenario):
    """Test plugin for creating and listing tenants"""

    @base.scenario(context={})
    def create_tenant(self, name_length=10, **kwargs):
        tenant = self._tenant_create(name_length=name_length, **kwargs)

    @base.scenario(context={})
    def list_tenants(self):
        self._list_tenants()
