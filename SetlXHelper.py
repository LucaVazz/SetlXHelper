import sublime, sublime_plugin
import webbrowser


class OpenQuickrefCommand(sublime_plugin.TextCommand):
	def run(self, edit=None):
		webbrowser.open_new_tab("https://github.com/LucaVazz/SetlXQuickreference/blob/master/SetlX-Quickreference.pdf")
