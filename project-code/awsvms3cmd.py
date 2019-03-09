from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.anthony.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint

import boto3
from cloudmesh.management.configuration.config import Config
from prettytable import PrettyTable


class AWSS3Command(PluginCommand):
    @command
    def do_s3(self, args, arguments):
        """
        ::

          Usage:
                  object [--object=SERVICE] put OBJECT BUCKET | KEY
                  object [--object=SERVICE] get OBJECT BUCKET | KEY
                  object [--object=SERVICE] getObjectOrKey BUCKET | KEY
                  object [--object=SERVICE] listObjectOrKey BUCKET | KEY
                  object [--object=SERVICE] delete BUCKET | KEY              
                  object [--object=SERVICE] createObjectOrKey BUCKET | KEY
                  object [--object=SERVICE] uploadObjectOrKey BUCKET | KEY 
                  object [--object=SERVICE] createfile BUCKET | KEY 

                  KEY [--KEY=API_KEY] SET API_KEY  #API key or username to be used (required)
                  SECRET [--SECRET=SECRET] SET SECRET #Secret password to be used (required)
                  SECURE [--SECURE=SECURE] SET SECURE #Whether to use HTTPS or HTTP. Note: Some providers only support HTTPS, and it is on by default.
                  HOST [--HOST=HOST] SET HOST #Override hostname used for connections
                  PORT [--PORT=PORT] SET PORT #Override port used for connections.
                  OBJECT_VERSION [--OBJECT_VERSION=OBJECT_VERSION] SET OBJECT_VERSION #Optional API version. Only used by drivers which support multiple API versions.
                  REGION [--REGION=REGION] SET REGION # Optional driver region. Only used by drivers which support multiple regions.      

            Parameters:
                BUCKET  NAME OF THE FOLDER or DIRECTORY in CLOUD STORAGE
                KEY FOLDER NAME WITH IN CLOUD STORAGE or BUCKET
                                
          
            Example:
              SET OBJECT=s3
              OBEJECT PUT BUCKET | KEY

        """
        print(arguments)