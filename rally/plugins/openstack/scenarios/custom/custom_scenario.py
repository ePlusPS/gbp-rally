from rally.plugins.openstack import scenario
from rally.common import utils as rutils
from rally.plugins.openstack.scenarios.custom import custom_utils as csutils



class CustomSG(csutils.CustomSGScenario):
    """Test plugin for creating and listing tenants"""

    @scenario.configure(context={})
    def create_tenant(self, name_length=10, **kwargs):
        tenant = self._tenant_create(name_length=name_length, **kwargs)

    @scenario.configure(context={})
    def list_tenants(self):
        self._list_tenants()

    @scenario.configure(context={})
    def create_policy_action(self, action_type="allow"):
        action_name = rutils.generate_random_name(prefix="rally_sg_action_allow")
        self._create_policy_action(name=action_name, type=action_type)
