class MyNetworkAccessManager(QtNetwork.QNetworkAccessManager):
    def __init__(self):
        config_proxy = configuracao_global.retorna_configuracao_proxy()
        print(config_proxy)
        QtNetwork.QNetworkAccessManager.__init__(self)
        proxy = QtNetwork.QNetworkProxy()
        proxy.setType(QtNetwork.QNetworkProxy.ProxyType.HttpProxy)
        proxy.setHostName('Host')
        proxy.setPort(1234)
        proxy.setUser('USUARIO123')
        proxy.setPassword('123456')
        QtNetwork.QNetworkProxy.setApplicationProxy(proxy)
        #QtNetwork.QNetworkAccessManager.setProxy(proxy=proxy)
