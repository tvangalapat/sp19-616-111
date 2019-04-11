import io
import json

from cloudmesh.storage.provider.gdrive.Authentication import Authentication
import httplib2


from apiclient.http import MediaFileUpload
from apiclient.http import MediaIoBaseDownload
from cloudmesh.management.configuration.config import Config
from cloudmesh.common.util import path_expand
from cloudmesh.objstorage.ObjectStorageABC import ObjectStorageABC
import magic

#
# BUG: des not follow named arguments in abc class
#
class Provider(ObjectStorageABC):



    def get(self, bucket_name, object_name):

        """Retrieve an object from an Amazon S3 bucket

        :param bucket_name: string
        :param object_name: string
        :return: botocore.response.StreamingBody object. If error, return None.
        """

        # Retrieve the object
        s3 = boto3.client('s3')
        try:
            response = s3.get_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            # AllAccessDisabled error == bucket or object not found
            logging.error(e)
            return None
        # Return an open StreamingBody object
        return response['Body']

    def put(dest_bucket_name, dest_object_name, src_data):
        """Add an object to an Amazon S3 bucket

        The src_data argument must be of type bytes or a string that references
        a file specification.

        :param dest_bucket_name: string
        :param dest_object_name: string
        :param src_data: bytes of data or string reference to file spec
        :return: True if src_data was added to dest_bucket/dest_object, otherwise
        False
        """

        # Construct Body= parameter
        if isinstance(src_data, bytes):
            object_data = src_data
        elif isinstance(src_data, str):
            try:
                object_data = open(src_data, 'rb')
                # possible FileNotFoundError/IOError exception
            except Exception as e:
                logging.error(e)
                return False
        else:
            logging.error('Type of ' + str(type(src_data)) +
                          ' for the argument \'src_data\' is not supported.')
            return False

        # Put the object
        s3 = boto3.client('s3')
        try:
            s3.put_object(Bucket=dest_bucket_name, Key=dest_object_name, Body=object_data)
        except ClientError as e:
            # AllAccessDisabled error == bucket not found
            # NoSuchKey or InvalidRequest error == (dest bucket/obj == src bucket/obj)
            logging.error(e)
            return False
        finally:
            if isinstance(src_data, str):
                object_data.close()
        return True

    def copy(src_bucket_name, src_object_name,
                    dest_bucket_name, dest_object_name=None):
        """Copy an Amazon S3 bucket object

        :param src_bucket_name: string
        :param src_object_name: string
        :param dest_bucket_name: string. Must already exist.
        :param dest_object_name: string. If dest bucket/object exists, it is
        overwritten. Default: src_object_name
        :return: True if object was copied, otherwise False
        """

        # Construct source bucket/object parameter
        copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
        if dest_object_name is None:
            dest_object_name = src_object_name

        # Copy the object
        s3 = boto3.client('s3')
        try:
            s3.copy_object(CopySource=copy_source, Bucket=dest_bucket_name,
                           Key=dest_object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def list(bucket_name):
        """List the objects in an Amazon S3 bucket

        :param bucket_name: string
        :return: List of bucket objects. If error, return None.
        """

        # Retrieve the list of bucket objects
        s3 = boto3.client('s3')
        try:
            response = s3.list_objects_v2(Bucket=bucket_name)
        except ClientError as e:
            # AllAccessDisabled error == bucket not found
            logging.error(e)
            return None
        return response['Contents']

    def delete(bucket_name, object_names):
        """Delete multiple objects from an Amazon S3 bucket

        :param bucket_name: string
        :param object_names: list of strings
        :return: True if the referenced objects were deleted, otherwise False
        """

        # Convert list of object names to appropriate data format
        objlist = [{'Key': obj} for obj in object_names]

        # Delete the objects
        s3 = boto3.client('s3')
        try:
            s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objlist})
        except ClientError as e:
            logging.error(e)
            return False
        return True
