from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.keystone import custom_utils as csutils



class CustomKeystone(csutils.CustomKeystoneScenario):
    """Test plugin for creating and listing tenants"""

    @scenario.configure(context={})
    def create_tenant(self, name_length=10, **kwargs):
        tenant = self._tenant_create(name_length=name_length, **kwargs)

    @scenario.configure(context={})
    def list_tenants(self):
        self._list_tenants()
