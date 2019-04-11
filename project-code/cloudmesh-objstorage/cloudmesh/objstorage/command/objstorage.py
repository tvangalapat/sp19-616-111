from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.objstorage.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from cloudmesh.objstorage.provider.awss3.Provider import Provider
from pprint import pprint


class ObjstorageCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_objstorage(self, args, arguments):

        """
        ::
          Usage:
                objstorage [--objstorage=SERVICE] create dir DIRECTORY
                objstorage [--objstorage=SERVICE] copy SOURCE DESTINATION [--recursive]
                objstorage [--objstorage=SERVICE] get SOURCE DESTINATION [--recursive]
                objstorage [--objstorage=SERVICE] put SOURCE DESTINATION [--recursive]
                objstorage [--objstorage=SERVICE] list SOURCE [--recursive] [--output=OUTPUT]
                objstorage [--objstorage=SERVICE] delete SOURCE
                objstorage [--objstorage=SERVICE] search  DIRECTORY FILENAME [--recursive] [--output=OUTPUT]

          This command does some useful things.

          Arguments:
              SOURCE        BUCKET | OBJECT  can be a source bucket or object name or file
              DESTINATION   BUCKET | OBJECT can be a destination bucket or object name  or file
              DIRECTORY     DIRECTORY refers to a folder or bucket on the cloud service for ex: awss3

          Options:
              -h, --help
              --objstorage=SERVICE  specify the cloud service name like aws-s3

          Description:
                commands used to upload, download, list files on different cloud objstorage services.

                objstorage put [options..]
                    Uploads the file specified in the filename to specified cloud from the SOURCEDIR.

                objstorage get [options..]
                    Downloads the file specified in the filename from the specified cloud to the DESTDIR.

                objstorage delete [options..]
                    Deletes the file specified in the filename from the specified cloud.

                objstorage list [options..]
                    lists all the files from the container name specified on the specified cloud.

                objstorage create dir [options..]
                    creates a folder with the directory name specified on the specified cloud.

                objstorage search [options..]
                    searches for the source in all the folders on the specified cloud.

          Example:
            set objstorage=s3object
            objstorage put SOURCE DESTINATION --recursive
            is the same as
            objstorage --objstorage=s3object put SOURCE DESTINATION --recursive
        """
        # arguments.CONTAINER = arguments["--container"]

        map_parameters(arguments,
                       "recursive",
                       "objstorage")
        VERBOSE.print(arguments, verbose=9)

        if arguments.objstorage is None:
            try:
                v = Variables()
                arguments.objstorage = v['objstorage']
            except Exception as e:
                arguments.objstorage = None
                raise ValueError("objstorage provider is not defined")

        arguments.objstorage = Parameter.expand(arguments.objstorage)

        print(arguments)

        provider = Provider(arguments.objstorage)

        if arguments.copy:
            result = provider.copy(arguments.objstorage,
                                  arguments.SOURCE,
                                  arguments.DESTINATION,
                                  arguments.recursive)

        if arguments.get:
            result = provider.get(arguments.objstorage,
                                  arguments.SOURCE,
                                  arguments.DESTINATION,
                                  arguments.recursive)

        elif arguments.put:
            result = provider.put(arguments.objstorage,
                                  arguments.SOURCE,
                                  arguments.DESTINATION,
                                  arguments.recursive)

        elif arguments.create and arguments.dir:
            result = provider.createdir(arguments.objstorage,
                                        arguments.DIRECTORY)

        elif arguments.list:
            for objstorage in arguments.objstorage:
                provider = Provider(objstorage)

                result = provider.list(arguments.objstorage,
                                       arguments.SOURCE,
                                       arguments.recursive)

        elif arguments.delete:

            for objstorage in arguments.objstorage:
                provider = Provider(objstorage)

                provider.delete(arguments.objstorage,
                                arguments.SOURCE)

        elif arguments.search:

            for objstorage in arguments.objstorage:
                provider = Provider(objstorage)

                provider.search(arguments.objstorage,
                                arguments.DIRECTORY,
                                arguments.FILENAME,
                                arguments.recursive)


        # arguments.FILE = arguments['--file'] or None
        #
        # print(arguments)
        #
        # m = Manager()
        #
        # if arguments.FILE:
        #     print("option a")
        #     m.list(path_expand(arguments.FILE))
        #
        # elif arguments.list:
        #     print("option b")
        #     m.list("just calling list without parameter")
        #
        # Console.error("This is just a sample")
        # return ""
