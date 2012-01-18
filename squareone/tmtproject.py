import tmt
import subprocess
from os.path import join, exists

class Project(tmt.EclipseProject):
	def configure(self):
		tmt.EclipseProject.configure(self)
		self.squareone_tables = join(self.binResource, 'squareone_tables')

	def compile(self):
		tmt.EclipseProject.compile(self)
		# build the tables for the two phase algorithm
		# if they don't already exist
		if not exists(self.squareone_tables):
			assert 0 == tmt.java(
							main="org.squareone.twophase.Tables",
							classpath=self.getClasspath(),
							args=[ self.squareone_tables ])

Project('squareone', description="A square one solver written in Java")