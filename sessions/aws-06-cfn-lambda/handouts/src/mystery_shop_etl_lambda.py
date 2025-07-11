from utils import s3_utils

import etl
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    LOGGER.info("lambda_handler: starting")

    try:
        file_path = "NOT_SET"  # just here to make the exception handler compile

        LOGGER.info("lambda_handler: s3.get_file_info: starting")
        bucket_name, file_path = s3_utils.get_file_info(event)

        LOGGER.info(
            f"lambda_handler: event: file={file_path}, bucket_name={bucket_name}"
        )

        LOGGER.info(
            f"lambda_handler: s3.load_file: loading file_name={file_path} from bucket_name={bucket_name}"
        )

        csv = s3_utils.load_file(bucket_name, file_path)
        LOGGER.info(f"lambda_handler: s3.load_file result={csv}")

        data = etl.extract(csv)
        LOGGER.info(f"lambda_handler: extract_csv_data result={data}")

        transformed_data = etl.transform(data)
        LOGGER.info(f"lambda_handler: transformed_data={transformed_data}")

    except Exception as err:
        LOGGER.error(f"lambda_handler: failure: error={err}, file={file_path}")
        raise err
