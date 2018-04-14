import os
from pomdp.sessionsearch.SsModel import SessionSearchModel
from util.TrecDomParser import TrecDomParser as tdp

if __name__ == '__main__':
    # 在session track2012中有一个subject是"merck & co"在6140行左右，&是特殊字符解析或报错，我先简单替换成空格，分析无影响

    # 获取搜索日志所所在的目录
    projDir = os.path.dirname(os.path.realpath(__file__))
    projDir = os.path.split(projDir)[0]
    sessionLogPath2 = os.path.join(projDir, 'sessionlog', 'sessiontrack2012.xml')
    sessionLogPath3 = os.path.join(projDir, 'sessionlog', 'sessiontrack2013.xml')

    # 预处理获取 Long Sessions
    sessionTrack12 = tdp(sessionLogPath2, 12)
    sessionTrack13 = tdp(sessionLogPath3, 13)
    longSessions12 = sessionTrack12.getLongSessionsSorted(4)
    print("Long Sessions in Track2012 Count: ", longSessions12.__len__())
    longSessions13 = sessionTrack13.getLongSessionsSorted(4)
    print("Long Sessions in Track2013 Count: ", longSessions13.__len__())
    longSessions = tdp.concatSessions(longSessions12, longSessions13)
    print("Combined Long Sessions Count: ", longSessions.__len__())

    # 生成interaction列表
    sampleList=tdp.getTrainSamples(longSessions)

    # 模型参数
    argDict = dict()
    argDict['stateNum'] = 4
    argDict['actionNum'] = 2  # TODO: 通过数据预处理获得user agent的数量
    argDict['actionNum'] = 2  # TODO: 通过数据预处理获得user agent的数量
    argDict['discount'] = 0.95

    env = SessionSearchModel(argDict)

    print("sssss")