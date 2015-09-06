from rally.plugins.openstack import scenario
from rally.task import atomic
import uuid

class CustomSGScenario(scenario.OpenStackScenario):
    """ Base Class for CustomKeystone scenarios with basic atomic action """
    RESOURCE_NAME_PREFIX = "rally_sg_"
    
    @atomic.action_timer("keystone.create_tenant")
    def _tenant_create(self, name_length=10, **kwargs):
        name = self._generate_random_name(length=name_length)
        return self.admin_clients("keystone").tenants.create(name, **kwargs)

    @atomic.action_timer("keystone.list_tenants")
    def _list_tenants(self):
        return self.admin_clients("keystone").tenants.list()

    @atomic.action_timer("gbp.create_policy_action")
    def _create_polic_action(self, name="allow", type="allow"):
        body = {
                "policy_action": {
                "name": name,
                "action_type": type
               }
        }
        self.clients("grouppolicy").create_policy_action(body)
   
    @atomic.action_timer("gbp.create_policy_target_group")
    def _create_policy_target_group(self, name):
        body = {
                "policy_target_group": {
                "name": name
                }
        }
        self.clients("grouppolicy").create_policy_target_group(body)

