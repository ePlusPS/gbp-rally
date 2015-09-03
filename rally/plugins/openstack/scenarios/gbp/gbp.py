from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.gbp import utils
from rally.plugins.openstack.scenarios.nova import utils as nova_utils
import time
from rally.common import utils as rutils
from rally.task import types
from rally.task import validation

class GBPTests(nova_utils.NovaScenario, utils.GBPScenario):
    """Benchmark scenarios for Group Based Policy"""
    
    @scenario.configure(context={"cleanup":["grouppolicy"]})
    def create_policy_action(self, action_type="allow"):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name, type=action_type)
        
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_update_policy_action(self, action_type="allow"):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name, type=action_type)
        # Create a new action name and update
        action_name1 = rutils.generate_random_name(prefix="rally_action_allow_")
        self._update_policy_action(name=action_name, new_name=action_name1)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_show_policy_action(self, action_type="allow"):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name, type=action_type)
        self._show_policy_action(action_name, action_type)
    
        
    @scenario.configure()
    def create_and_delete_policy_action(self, action_type="allow"):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name, type=action_type)
        self._delete_policy_action(name=action_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_policy_classifier(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'], classifier_args['port_range'],
                                      classifier_args['direction'])
    
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_show_policy_classifier(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'], classifier_args['port_range'],
                                      classifier_args['direction'])
        self._show_policy_classifier(classifier_name, classifier_args['protocol'],
                                     classifier_args['port_range'], classifier_args['direction'])
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_update_policy_classifier(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'], classifier_args['port_range'],
                                      classifier_args['direction'])
        classifier_name1 = rutils.generate_random_name(prefix="rally_classifier_")
        self._update_policy_classifier(classifier_name, classifier_name1,
                                       "tcp", "5001", "in")
    

    @scenario.configure()
    def create_and_delete_policy_classifier(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'], classifier_args['port_range'],
                                      classifier_args['direction'])
        self._delete_policy_classifier(classifier_name)
        self._delete_policy_action(name=action_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_policy_rule(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'], classifier_args['port_range'],
                                       classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_show_policy_rule(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'], classifier_args['port_range'],
                                       classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        self._show_policy_rule(rule_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_update_policy_rule(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'], classifier_args['port_range'],
                                       classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a new action and classifier and update
        action_name1 = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name1)
        # Create a policy classifier
        classifier_name1 = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name1,classifier_args['protocol'], classifier_args['port_range'],
                                       classifier_args['direction'])
        self._update_policy_rule(rule_name, action_name1, classifier_name1)

    
    
    @scenario.configure()
    def create_and_delete_policy_rule(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'], classifier_args['port_range'],
                                       classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        self._delete_policy_rule(rule_name)
        self._delete_policy_classifier(classifier_name)
        self._delete_policy_action(name=action_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_policy_rule_set(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])

    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_show_policy_rule_set(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        self._show_policy_rule_set(ruleset_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_update_policy_rule_set(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a new rule and add it in
        rule_name1 = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name1, classifier_name, action_name)
        self._update_policy_rule_set(ruleset_name, [rule_name, rule_name1])
    

    @scenario.configure()
    def create_and_delete_policy_rule_set(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        self._delete_policy_rule_set(ruleset_name)
        self._delete_policy_rule(rule_name)
        self._delete_policy_classifier(classifier_name)
        self._delete_policy_action(name=action_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_policy_target_group(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol']
                                       , classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_show_policy_target_group(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol']
                                       , classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        self._show_policy_target_group(pt_group_name)
    
    
    @scenario.configure()
    def create_and_delete_policy_target_group(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name,classifier_args['protocol']
                                       , classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        self._delete_policy_target_group(pt_group_name)
        self._delete_policy_rule_set(ruleset_name)
        self._delete_policy_rule(rule_name)
        self._delete_policy_classifier(classifier_name)
        self._delete_policy_action(name=action_name)
    
    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_update_policy_target_group(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        self._update_policy_target_group(pt_group_name, provided_policy_rulesets=[ruleset_name])


    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_policy_target(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        # Now update the policy target group
        self._update_policy_target_group(pt_group_name, provided_policy_rulesets=[ruleset_name])
        # Now create a policy target inside the group
        pt_name = rutils.generate_random_name(prefix="rally_target_web1")
        self._create_policy_target(pt_name,pt_group_name)

    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_show_policy_target(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        # Now update the policy target group
        self._update_policy_target_group(pt_group_name, provided_policy_rulesets=[ruleset_name])
        # Now create a policy target inside the group
        pt_name = rutils.generate_random_name(prefix="rally_target_web1")
        self._create_policy_target(pt_name,pt_group_name)
        self._show_policy_target(pt_name)


    @scenario.configure(context={"cleanup": ["grouppolicy"]})
    def create_and_update_policy_target(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        # Now update the policy target group
        self._update_policy_target_group(pt_group_name, provided_policy_rulesets=[ruleset_name])
        # Now create a policy target inside the group
        pt_name = rutils.generate_random_name(prefix="rally_target_web1")
        self._create_policy_target(pt_name,pt_group_name)
        pt_name2 = rutils.generate_random_name(prefix="rally_target_web2")
        self._update_policy_target(pt_name, pt_name2)
    
    @scenario.configure()
    def create_and_delete_policy_target(self, classifier_args={}):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        # Now update the policy target group
        self._update_policy_target_group(pt_group_name, provided_policy_rulesets=[ruleset_name])
        # Now create a policy target inside the group
        pt_name = rutils.generate_random_name(prefix="rally_target_web1")
        self._create_policy_target(pt_name,pt_group_name)
        # Delete all created resources
        self._delete_policy_target(pt_name)
        self._delete_policy_target_group(pt_group_name)
        self._delete_policy_rule_set(ruleset_name)
        self._delete_policy_rule(rule_name)
        self._delete_policy_classifier(classifier_name)
        self._delete_policy_action(name=action_name)
    
    
    @types.set(image=types.ImageResourceType, flavor=types.FlavorResourceType)
    @validation.image_valid_on_flavor("flavor", "image")
    @scenario.configure(context={"cleanup":["nova","grouppolicy"]})
    def boot_vm(self, image, flavor, classifier_args= {}, **kwargs):
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        # Create a policy classifier
        classifier_name = rutils.generate_random_name(prefix="rally_classifier_web_traffic_")
        self._create_policy_classifier(classifier_name, classifier_args['protocol'],
                                       classifier_args['port_range'], classifier_args['direction'])
        # Now create a policy rule
        rule_name = rutils.generate_random_name(prefix="rally_rule_web_policy_")
        self._create_policy_rule(rule_name, classifier_name, action_name)
        # Now create a policy rule set
        ruleset_name = rutils.generate_random_name(prefix="rally_ruleset_web_")
        self._create_policy_rule_set(ruleset_name, [rule_name])
        # Now create a policy target group
        pt_group_name = rutils.generate_random_name(prefix="rally_group_")
        self._create_policy_target_group(pt_group_name)
        # Now update the policy target group
        self._update_policy_target_group(pt_group_name, provided_policy_rulesets=[ruleset_name])
        # Now create a policy target inside the group
        pt_name = rutils.generate_random_name(prefix="rally_target_web1")
        self._create_policy_target(pt_name,pt_group_name)
        # Get the port id based on the policy target
        port_id = self._show_policy_target(pt_name)
        kwargs["nics"] = [{"port-id": port_id}]
        instance = self._boot_server(image, flavor, **kwargs)
    
    @types.set(image=types.ImageResourceType, flavor=types.FlavorResourceType)
    @validation.image_valid_on_flavor("flavor", "image")
    @scenario.configure(context={"cleanup": ["nova", "grouppolicy"]})
    def ping_and_ssh_group(self, image, flavor, **kwargs):
        """
        Scenario that has
        1. A provider group that provides icmp and ssh bidirectional
        2. 2 consumer groups that consumes icmp and ssh bidirectional
        """
        action_name = rutils.generate_random_name(prefix="rally_action_allow_")
        self._create_policy_action(name=action_name)
        
        # Create a policy classifier name for icmp and ssh
        classifier_name_icmp = rutils.generate_random_name(prefix="rally_classifier_icmp_")
        classifier_name_ssh = rutils.generate_random_name(prefix="rally_classifier_ssh_")
        # Create the policy classifier for ICMP
        self._create_policy_classifier(classifier_name_icmp, "icmp", None, "bi")
        # Create the policy classifier for SSH
        self._create_policy_classifier(classifier_name_ssh, "tcp", "22", "bi")
                                                          

        # Now create a policy rule for ICMP
        rule_name_icmp = rutils.generate_random_name(prefix="rally_rule_icmp_")
        self._create_policy_rule(rule_name_icmp, classifier_name_icmp, action_name)
        # Now create a policy rule for SSH
        rule_name_ssh = rutils.generate_random_name(prefix="rally_rule_ssh_")
        self._create_policy_rule(rule_name_ssh, classifier_name_ssh, action_name)
        
        # Now create a policy rule set for ICMP
        ruleset_name_icmp = rutils.generate_random_name(prefix="rally_ruleset_icmp_")
        self._create_policy_rule_set(ruleset_name_icmp, [rule_name_icmp])
        # Create another rule set for SSH
        ruleset_name_ssh = rutils.generate_random_name(prefix="rally_ruleset_ssh_")
        self._create_policy_rule_set(ruleset_name_ssh, [rule_name_ssh])
        
        # Create a policy target group that provides ICMP and SSH
        pt_group_name_provider = rutils.generate_random_name(prefix="rally_group_provider_")
        self._create_policy_target_group(pt_group_name_provider)
        # Now update the policy target group to provide ICMP and SSH
        self._update_policy_target_group(pt_group_name_provider, provided_policy_rulesets=[ruleset_name_icmp, ruleset_name_ssh])
        # Create another 2 policy target groups that consumes the ICMP and SSH
        pt_group_name_consumer_1 = rutils.generate_random_name(prefix="rally_group_consumer_1_")
        self._create_policy_target_group(pt_group_name_consumer_1)
        self._update_policy_target_group(pt_group_name_consumer_1, consumed_policy_rulesets=[ruleset_name_icmp, ruleset_name_ssh])
        pt_group_name_consumer_2 = rutils.generate_random_name(prefix="rally_group_consumer_2_")
        self._create_policy_target_group(pt_group_name_consumer_2)
        self._update_policy_target_group(pt_group_name_consumer_2, consumed_policy_rulesets=[ruleset_name_icmp, ruleset_name_ssh])

        
        # Create a policy target in the provider group
        pt_name_provider = rutils.generate_random_name(prefix="rally_target_provider_")
        self._create_policy_target(pt_name_provider, pt_group_name_provider)
        port_id_provider = self._show_policy_target(pt_name_provider)
        
        # Create a policy target in the consumer 1 group
        pt_name_consumer_1 = rutils.generate_random_name(prefix="rally_target_consumer_1_")
        self._create_policy_target(pt_name_consumer_1, pt_group_name_consumer_1)
        port_id_consumer_1 = self._show_policy_target(pt_name_consumer_1)
        
        # Create a policy target in the consumer 2 group
        pt_name_consumer_2 = rutils.generate_random_name(prefix="rally_target_consumer_2_")
        self._create_policy_target(pt_name_consumer_2, pt_group_name_consumer_2)
        port_id_consumer_2 = self._show_policy_target(pt_name_consumer_2)
        
        # Create a VM in provider group
        kwargs["nics"] = [{"port-id": port_id_provider}]
        instance_provider = self._boot_server(image, flavor, **kwargs)
        
        # Create a VM in the consumer1 group
        kwargs["nics"] = [{"port-id": port_id_consumer_1}]
        instance_consumer_1 = self._boot_server(image, flavor, **kwargs)
        
        # Create a VM in the consumer 2 group
        kwargs["nics"] = [{"port-id": port_id_consumer_2}]
        instance_consumer_2 = self._boot_server(image, flavor, **kwargs)
