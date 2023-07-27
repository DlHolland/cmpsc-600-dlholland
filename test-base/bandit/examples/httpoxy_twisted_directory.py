from twisted.internet import reactor
from twisted.web import server, static, twcgi

root = static.File("/root")
root.putChild("cgi-bin", twcgi.CGIDirectory("/var/www/cgi-bin"))
reactor.listenTCP(80, server.Site(root))
reactor.run()
