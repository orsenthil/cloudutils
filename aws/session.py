import os
import boto3


def get_boto_session():
    profile = os.environ.get('AWS_PROFILE', '')
    session = boto3.Session(profile_name=profile)
    return session


def get_s3_session():
    session = get_boto_session()
    return session.resource('s3')


def get_cloudformation_session():
    session = get_boto_session()
    return session.client('cloudformation')
