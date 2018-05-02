from aws.session import get_cloudformation_session


def list_stacks():
    cf = get_cloudformation_session()
    return cf.list_stacks(
            StackStatusFilter=[
                'CREATE_IN_PROGRESS',
                'CREATE_FAILED',
                'CREATE_COMPLETE',
                'ROLLBACK_IN_PROGRESS',
                'ROLLBACK_FAILED',
                'ROLLBACK_COMPLETE',
                'DELETE_IN_PROGRESS',
                'DELETE_FAILED',
                'UPDATE_IN_PROGRESS',
                'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS',
                'UPDATE_COMPLETE',
                'UPDATE_ROLLBACK_IN_PROGRESS',
                'UPDATE_ROLLBACK_FAILED',
                'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS',
                'UPDATE_ROLLBACK_COMPLETE',
                'REVIEW_IN_PROGRESS',
                ]
    )


def delete_stacks_in_state(state_name):
    active_stacks = list_stacks()

    stacks_to_delete = []
    for stack_summary in active_stacks.get('StackSummaries', []):
        if stack_summary.get('StackStatus', None) == state_name:
            stacks_to_delete.append(stack_summary)

    cf = get_cloudformation_session()

    stacks_deleted = []

    for stack_summary in stacks_to_delete:
        stack_name_to_delete = stack_summary["StackName"]
        cf.update_termination_protection(EnableTerminationProtection=False, StackName=stack_name_to_delete)
        cf.delete_stack(StackName=stack_name_to_delete)
        stacks_deleted.append(stack_name_to_delete)

    return stacks_deleted
