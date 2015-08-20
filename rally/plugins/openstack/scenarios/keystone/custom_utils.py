from rally.benchmark.scenarios import base
import uuid

class CustomKeystoneScenario(base.Scenario):
    """ Base Class for CustomKeystone scenarios with basic atomic action """
    RESOURCE_NAME_PREFIX = "rally_keystone_"
    
    @base.atomic_action_timer("keystone.create_tenant")
    def _tenant_create(self, name_length=10, **kwargs):
        name = self._generate_random_name(length=name_length)
        return self.admin_clients("keystone").tenants.create(name, **kwargs)

    @base.atomic_action_timer("keystone.list_tenants")
    def _list_tenants(self):
        return self.admin_clients("keystone").tenants.list()

 
