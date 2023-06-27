# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RoleArgs', 'Role']

@pulumi.input_type
class RoleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Role resource.
        :param pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]] actions: The name of the permission.
        :param pulumi.Input[str] name: The name of the role
        """
        pulumi.set(__self__, "actions", actions)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]]:
        """
        The name of the permission.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the role
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _RoleState:
    def __init__(__self__, *,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Role resources.
        :param pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]] actions: The name of the permission.
        :param pulumi.Input[str] name: The name of the role
        """
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]]]:
        """
        The name of the permission.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoleActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the role
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Role(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleActionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Airflow role.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_airflow as airflow

        example = airflow.Role("example", actions=[airflow.RoleActionArgs(
            action="can_read",
            resource="Audit Logs",
        )])
        ```

        ## Import

        Roles can be imported using the role key. terraform

        ```sh
         $ pulumi import airflow:index/role:Role default example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleActionArgs']]]] actions: The name of the permission.
        :param pulumi.Input[str] name: The name of the role
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Airflow role.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_airflow as airflow

        example = airflow.Role("example", actions=[airflow.RoleActionArgs(
            action="can_read",
            resource="Audit Logs",
        )])
        ```

        ## Import

        Roles can be imported using the role key. terraform

        ```sh
         $ pulumi import airflow:index/role:Role default example
        ```

        :param str resource_name: The name of the resource.
        :param RoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleActionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoleArgs.__new__(RoleArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["name"] = name
        super(Role, __self__).__init__(
            'airflow:index/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleActionArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleActionArgs']]]] actions: The name of the permission.
        :param pulumi.Input[str] name: The name of the role
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoleState.__new__(_RoleState)

        __props__.__dict__["actions"] = actions
        __props__.__dict__["name"] = name
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence['outputs.RoleAction']]:
        """
        The name of the permission.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the role
        """
        return pulumi.get(self, "name")
