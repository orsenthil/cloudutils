Cloud Utils
===========

Small set of scripts that is handy when working on Cloud Infrastructure.



**AWS**

::

    export AWS_PROFILE=AWS-PROFILE-TO-USE

The `AWS-PROFILE-TO-USE` is consists of a profile-name with secrets stored in name `~/.aws/credentials`


::

    [AWS-PROFILE-TO-USE]
    aws_access_key_id     =
    aws_secret_access_key =
    aws_session_token     =

And a non-secret in `~/.aws/config`

::

    [profile AWS-PROFILE-TO-USE]
    region = us-west-2
    output = json


How to Use
----------

This is work in progress. Update main.py to various operations you like to do, using the higher level operations like

::

    cf.list_stacks
    cf.delete_stacks_in_state(state-name)
    s3.delete_all_buckets_older_than_2_days


Documentation
-------------

These are higher level helper functions and scripts written on top of http://boto3.readthedocs.io/en/latest/index.html



