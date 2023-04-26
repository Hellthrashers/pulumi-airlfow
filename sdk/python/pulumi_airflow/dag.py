# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DagArgs', 'Dag']

@pulumi.input_type
class DagArgs:
    def __init__(__self__, *,
                 dag_id: pulumi.Input[str],
                 is_paused: pulumi.Input[bool],
                 delete_dag: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Dag resource.
        :param pulumi.Input[str] dag_id: The ID of the DAG.
        :param pulumi.Input[bool] is_paused: Whether the DAG is paused.
        """
        pulumi.set(__self__, "dag_id", dag_id)
        pulumi.set(__self__, "is_paused", is_paused)
        if delete_dag is not None:
            pulumi.set(__self__, "delete_dag", delete_dag)

    @property
    @pulumi.getter(name="dagId")
    def dag_id(self) -> pulumi.Input[str]:
        """
        The ID of the DAG.
        """
        return pulumi.get(self, "dag_id")

    @dag_id.setter
    def dag_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dag_id", value)

    @property
    @pulumi.getter(name="isPaused")
    def is_paused(self) -> pulumi.Input[bool]:
        """
        Whether the DAG is paused.
        """
        return pulumi.get(self, "is_paused")

    @is_paused.setter
    def is_paused(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_paused", value)

    @property
    @pulumi.getter(name="deleteDag")
    def delete_dag(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_dag")

    @delete_dag.setter
    def delete_dag(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_dag", value)


@pulumi.input_type
class _DagState:
    def __init__(__self__, *,
                 dag_id: Optional[pulumi.Input[str]] = None,
                 delete_dag: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_token: Optional[pulumi.Input[str]] = None,
                 fileloc: Optional[pulumi.Input[str]] = None,
                 is_active: Optional[pulumi.Input[bool]] = None,
                 is_paused: Optional[pulumi.Input[bool]] = None,
                 is_subdag: Optional[pulumi.Input[bool]] = None,
                 root_dag_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Dag resources.
        :param pulumi.Input[str] dag_id: The ID of the DAG.
        :param pulumi.Input[str] description: User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.
        :param pulumi.Input[str] file_token: The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file.
        :param pulumi.Input[str] fileloc: The absolute path to the file.
        :param pulumi.Input[bool] is_active: Whether the DAG is currently seen by the scheduler(s).
        :param pulumi.Input[bool] is_paused: Whether the DAG is paused.
        :param pulumi.Input[bool] is_subdag: Whether the DAG is SubDAG.
        :param pulumi.Input[str] root_dag_id: If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.
        """
        if dag_id is not None:
            pulumi.set(__self__, "dag_id", dag_id)
        if delete_dag is not None:
            pulumi.set(__self__, "delete_dag", delete_dag)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if file_token is not None:
            pulumi.set(__self__, "file_token", file_token)
        if fileloc is not None:
            pulumi.set(__self__, "fileloc", fileloc)
        if is_active is not None:
            pulumi.set(__self__, "is_active", is_active)
        if is_paused is not None:
            pulumi.set(__self__, "is_paused", is_paused)
        if is_subdag is not None:
            pulumi.set(__self__, "is_subdag", is_subdag)
        if root_dag_id is not None:
            pulumi.set(__self__, "root_dag_id", root_dag_id)

    @property
    @pulumi.getter(name="dagId")
    def dag_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the DAG.
        """
        return pulumi.get(self, "dag_id")

    @dag_id.setter
    def dag_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dag_id", value)

    @property
    @pulumi.getter(name="deleteDag")
    def delete_dag(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_dag")

    @delete_dag.setter
    def delete_dag(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_dag", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="fileToken")
    def file_token(self) -> Optional[pulumi.Input[str]]:
        """
        The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file.
        """
        return pulumi.get(self, "file_token")

    @file_token.setter
    def file_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_token", value)

    @property
    @pulumi.getter
    def fileloc(self) -> Optional[pulumi.Input[str]]:
        """
        The absolute path to the file.
        """
        return pulumi.get(self, "fileloc")

    @fileloc.setter
    def fileloc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fileloc", value)

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the DAG is currently seen by the scheduler(s).
        """
        return pulumi.get(self, "is_active")

    @is_active.setter
    def is_active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_active", value)

    @property
    @pulumi.getter(name="isPaused")
    def is_paused(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the DAG is paused.
        """
        return pulumi.get(self, "is_paused")

    @is_paused.setter
    def is_paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_paused", value)

    @property
    @pulumi.getter(name="isSubdag")
    def is_subdag(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the DAG is SubDAG.
        """
        return pulumi.get(self, "is_subdag")

    @is_subdag.setter
    def is_subdag(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_subdag", value)

    @property
    @pulumi.getter(name="rootDagId")
    def root_dag_id(self) -> Optional[pulumi.Input[str]]:
        """
        If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.
        """
        return pulumi.get(self, "root_dag_id")

    @root_dag_id.setter
    def root_dag_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "root_dag_id", value)


class Dag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dag_id: Optional[pulumi.Input[str]] = None,
                 delete_dag: Optional[pulumi.Input[bool]] = None,
                 is_paused: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Provides an Airflow DAG.

        > Note this resource adpots an existing DAG and does not create a one, Also on delete the resource by default. A DAG is only deleted from state and not acutally deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_airflow as airflow

        example = airflow.Dag("example",
            dag_id="example",
            is_paused=False)
        ```

        ## Import

        DAGs can be imported using the DAG Id. terraform

        ```sh
         $ pulumi import airflow:index/dag:Dag default example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dag_id: The ID of the DAG.
        :param pulumi.Input[bool] is_paused: Whether the DAG is paused.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Airflow DAG.

        > Note this resource adpots an existing DAG and does not create a one, Also on delete the resource by default. A DAG is only deleted from state and not acutally deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_airflow as airflow

        example = airflow.Dag("example",
            dag_id="example",
            is_paused=False)
        ```

        ## Import

        DAGs can be imported using the DAG Id. terraform

        ```sh
         $ pulumi import airflow:index/dag:Dag default example
        ```

        :param str resource_name: The name of the resource.
        :param DagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dag_id: Optional[pulumi.Input[str]] = None,
                 delete_dag: Optional[pulumi.Input[bool]] = None,
                 is_paused: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DagArgs.__new__(DagArgs)

            if dag_id is None and not opts.urn:
                raise TypeError("Missing required property 'dag_id'")
            __props__.__dict__["dag_id"] = dag_id
            __props__.__dict__["delete_dag"] = delete_dag
            if is_paused is None and not opts.urn:
                raise TypeError("Missing required property 'is_paused'")
            __props__.__dict__["is_paused"] = is_paused
            __props__.__dict__["description"] = None
            __props__.__dict__["file_token"] = None
            __props__.__dict__["fileloc"] = None
            __props__.__dict__["is_active"] = None
            __props__.__dict__["is_subdag"] = None
            __props__.__dict__["root_dag_id"] = None
        super(Dag, __self__).__init__(
            'airflow:index/dag:Dag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dag_id: Optional[pulumi.Input[str]] = None,
            delete_dag: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            file_token: Optional[pulumi.Input[str]] = None,
            fileloc: Optional[pulumi.Input[str]] = None,
            is_active: Optional[pulumi.Input[bool]] = None,
            is_paused: Optional[pulumi.Input[bool]] = None,
            is_subdag: Optional[pulumi.Input[bool]] = None,
            root_dag_id: Optional[pulumi.Input[str]] = None) -> 'Dag':
        """
        Get an existing Dag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dag_id: The ID of the DAG.
        :param pulumi.Input[str] description: User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.
        :param pulumi.Input[str] file_token: The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file.
        :param pulumi.Input[str] fileloc: The absolute path to the file.
        :param pulumi.Input[bool] is_active: Whether the DAG is currently seen by the scheduler(s).
        :param pulumi.Input[bool] is_paused: Whether the DAG is paused.
        :param pulumi.Input[bool] is_subdag: Whether the DAG is SubDAG.
        :param pulumi.Input[str] root_dag_id: If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DagState.__new__(_DagState)

        __props__.__dict__["dag_id"] = dag_id
        __props__.__dict__["delete_dag"] = delete_dag
        __props__.__dict__["description"] = description
        __props__.__dict__["file_token"] = file_token
        __props__.__dict__["fileloc"] = fileloc
        __props__.__dict__["is_active"] = is_active
        __props__.__dict__["is_paused"] = is_paused
        __props__.__dict__["is_subdag"] = is_subdag
        __props__.__dict__["root_dag_id"] = root_dag_id
        return Dag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dagId")
    def dag_id(self) -> pulumi.Output[str]:
        """
        The ID of the DAG.
        """
        return pulumi.get(self, "dag_id")

    @property
    @pulumi.getter(name="deleteDag")
    def delete_dag(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "delete_dag")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fileToken")
    def file_token(self) -> pulumi.Output[str]:
        """
        The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file.
        """
        return pulumi.get(self, "file_token")

    @property
    @pulumi.getter
    def fileloc(self) -> pulumi.Output[str]:
        """
        The absolute path to the file.
        """
        return pulumi.get(self, "fileloc")

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> pulumi.Output[bool]:
        """
        Whether the DAG is currently seen by the scheduler(s).
        """
        return pulumi.get(self, "is_active")

    @property
    @pulumi.getter(name="isPaused")
    def is_paused(self) -> pulumi.Output[bool]:
        """
        Whether the DAG is paused.
        """
        return pulumi.get(self, "is_paused")

    @property
    @pulumi.getter(name="isSubdag")
    def is_subdag(self) -> pulumi.Output[bool]:
        """
        Whether the DAG is SubDAG.
        """
        return pulumi.get(self, "is_subdag")

    @property
    @pulumi.getter(name="rootDagId")
    def root_dag_id(self) -> pulumi.Output[str]:
        """
        If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.
        """
        return pulumi.get(self, "root_dag_id")

