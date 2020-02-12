from fman import DirectoryPaneCommand, show_alert
from fman.url import as_human_readable
import subprocess

class GoTerminal(DirectoryPaneCommand):
	def __call__(self):
		current_path = self.pane.get_path()
		subprocess.call(f'cmd /c "cd /d {as_human_readable(current_path)} && start wt.exe"')