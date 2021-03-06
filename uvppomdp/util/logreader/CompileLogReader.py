# --------------------------------------------
# @File     : CompileLogReader.py
# @Time     : 2018/6/7 21:14
# @Author   : Yanqing Wang (DarkNightRequiem)
# @Note     :
# --------------------------------------------
import os
import chardet
import zipfile
from antlr4 import *
from util.ConfigReader import config_reader
from util.meta.ComplieFile import CompileFile
from util.ColorfulLogger import logger
from util.antlr4.recognizers.CSharpLexer import CSharpLexer
from util.meta.ZipFileStream import ZipFileStream


class ComplieLogReader:
    def __init__(self):
        # 编译日志存放目录
        self.dir = config_reader.compile_logs_uploads_dir

        # 编译日志文件名列表
        self.files_names = os.listdir(self.dir)

    def read(self, name):
        """
        用于读取单个zip文件的内容，文件需要位于dir中
        :param name: 文件名
        :return: 单个压缩文件中的所有内容字典
        """
        contents={}
        try:
            zip = zipfile.ZipFile(self.dir + "/" + name, "r")

            # 内容为空
            if 0 == zip.filelist.__len__():
                return None

            # 项目名称
            folder = zip.filelist[0].filename.split("/")[0]

            for entry in zip.filelist:
                if entry.filename.find(folder + "/Properties") >= 0:
                    # 忽略Properties文件夹
                    continue
                else:
                    # 读取文件内容
                    file_bytes = zip.read(entry.filename)

                    # 查看文件编码
                    encode = (chardet.detect(file_bytes))["encoding"] \
                        if (chardet.detect(file_bytes))["encoding"] is not None \
                        else "utf-8"

                    # 加入字典
                    contents[entry.filename]=zip.read(entry.filename).decode(encode)
        except zipfile.BadZipFile:
            # 文件损坏
            # print("\033[32;0mBroken File:",name)
            logger.error(str(self.__class__),"Broken File: "+ name)
            return None
        except TypeError:
            # 无法解析文件编码
            # print("\033[32;0mUnKnown File Encoding: ",name)
            logger.error(str(self.__class__), "UnKnown File Encoding: " + name)
            return None

        return contents

    def readall(self):
        """
        读取配置文件中指定目录下的所有zip文件内容
        注意：文件存放目录中排序方式需要按名称排序
        :return: 字典形式的所有文件内容列表
        """
        cmpllogs=[]

        for filename in self.files_names:
            # 读取文件内容
            contents=self.read(filename)

            # 读取成功加入列表
            if contents is not None:
                cmpllogs.append(
                    CompileFile(
                        filename,
                        contents
                    )
                )

        return cmpllogs

    def read_as_zipfilestreams(self, path):
        """
        将zip中的所有文件进行流式读取
        :param path: 文件路径，如 D:/11111.zip
        :return: zip文件中的所有文件的流的列表
        """
        streams=[]
        try:
            zip = zipfile.ZipFile(path, "r")

            # 内容为空
            if 0 == zip.filelist.__len__():
                return None

            # 项目名称
            folder = zip.filelist[0].filename.split("/")[0]

            for entry in zip.filelist:
                if entry.filename.find("/Properties") >= 0:
                    # 忽略Properties文件夹
                    continue
                else:
                    # 读取文件内容
                    file_bytes = zip.read(entry.filename)

                    # 查看文件编码
                    encode = (chardet.detect(file_bytes))["encoding"] \
                        if (chardet.detect(file_bytes))["encoding"] is not None \
                        else "utf-8"

                    # 加入列表
                    stream=ZipFileStream(file_bytes=file_bytes,encoding=encode)
                    streams.append(stream)
        except zipfile.BadZipFile:
            # 文件损坏
            logger.error(str(self.__class__),"Broken File: "+ path)
            return None
        except TypeError:
            # 无法解析文件编码
            logger.error(str(self.__class__), "UnKnown File Encoding: " + path)
            return None

        return streams


# 利用模块的导入机制实现单例模式
cmpl_reader=ComplieLogReader()

