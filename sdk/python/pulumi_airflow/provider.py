# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 base_endpoint: pulumi.Input[str],
                 disable_ssl_verification: Optional[pulumi.Input[bool]] = None,
                 oauth2_token: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[bool] disable_ssl_verification: Disable SSL verification
        :param pulumi.Input[str] oauth2_token: The oauth to use for API authentication
        :param pulumi.Input[str] password: The password to use for API basic authentication
        :param pulumi.Input[str] username: The username to use for API basic authentication
        """
        pulumi.set(__self__, "base_endpoint", base_endpoint)
        if disable_ssl_verification is not None:
            pulumi.set(__self__, "disable_ssl_verification", disable_ssl_verification)
        if oauth2_token is not None:
            pulumi.set(__self__, "oauth2_token", oauth2_token)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="baseEndpoint")
    def base_endpoint(self) -> pulumi.Input[str]:
        return pulumi.get(self, "base_endpoint")

    @base_endpoint.setter
    def base_endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_endpoint", value)

    @property
    @pulumi.getter(name="disableSslVerification")
    def disable_ssl_verification(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable SSL verification
        """
        return pulumi.get(self, "disable_ssl_verification")

    @disable_ssl_verification.setter
    def disable_ssl_verification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_ssl_verification", value)

    @property
    @pulumi.getter(name="oauth2Token")
    def oauth2_token(self) -> Optional[pulumi.Input[str]]:
        """
        The oauth to use for API authentication
        """
        return pulumi.get(self, "oauth2_token")

    @oauth2_token.setter
    def oauth2_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth2_token", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password to use for API basic authentication
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The username to use for API basic authentication
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_endpoint: Optional[pulumi.Input[str]] = None,
                 disable_ssl_verification: Optional[pulumi.Input[bool]] = None,
                 oauth2_token: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the airflow package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_ssl_verification: Disable SSL verification
        :param pulumi.Input[str] oauth2_token: The oauth to use for API authentication
        :param pulumi.Input[str] password: The password to use for API basic authentication
        :param pulumi.Input[str] username: The username to use for API basic authentication
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the airflow package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_endpoint: Optional[pulumi.Input[str]] = None,
                 disable_ssl_verification: Optional[pulumi.Input[bool]] = None,
                 oauth2_token: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if base_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'base_endpoint'")
            __props__.__dict__["base_endpoint"] = base_endpoint
            __props__.__dict__["disable_ssl_verification"] = pulumi.Output.from_input(disable_ssl_verification).apply(pulumi.runtime.to_json) if disable_ssl_verification is not None else None
            __props__.__dict__["oauth2_token"] = oauth2_token
            __props__.__dict__["password"] = password
            __props__.__dict__["username"] = username
        super(Provider, __self__).__init__(
            'airflow',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="baseEndpoint")
    def base_endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "base_endpoint")

    @property
    @pulumi.getter(name="oauth2Token")
    def oauth2_token(self) -> pulumi.Output[Optional[str]]:
        """
        The oauth to use for API authentication
        """
        return pulumi.get(self, "oauth2_token")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password to use for API basic authentication
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        """
        The username to use for API basic authentication
        """
        return pulumi.get(self, "username")

