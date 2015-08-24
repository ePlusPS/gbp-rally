from rally.plugins.openstack import scenario
from rally.task import atomic
import uuid

class CustomKeystoneScenario(scenario.OpenstackScenario):
    """ Base Class for CustomKeystone scenarios with basic atomic action """
    RESOURCE_NAME_PREFIX = "rally_keystone_"
    
    @atomic.action_timer("keystone.create_tenant")
    def _tenant_create(self, name_length=10, **kwargs):
        name = self._generate_random_name(length=name_length)
        return self.admin_clients("keystone").tenants.create(name, **kwargs)

    @atomic.action_timer("keystone.list_tenants")
    def _list_tenants(self):
        return self.admin_clients("keystone").tenants.list()
