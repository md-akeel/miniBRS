#   vf_leap
#   Copyright (c)Cloud Innovation Partners 2020.
#   Author : Shahbaz Ali

from plugins.vf_leap.operators.common.servicenow_to_generic_transfer_operator import ServiceNowToGenericTransferOperator


class ServiceNowToS3TransferOperator(ServiceNowToGenericTransferOperator):

    def _upload(self):

        # TODO implement S3 logic
        pass