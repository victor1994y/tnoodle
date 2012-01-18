import tmt
from os.path import join

class Project(tmt.EclipseProject):
	def configure(self):
		tmt.EclipseProject.configure(self)
		tmt.Server.addPlugin(self)
		self.nonJavaSrcDeps += tmt.glob(self.srcResource, '.*html$', relativeTo=self.srcResource)
		self.nonJavaSrcDeps += tmt.glob(self.srcResource, '.*js$', relativeTo=self.srcResource)

Project(tmt.projectName(), description="A server plugin wrapper for scrambles that also draws pdfs.")