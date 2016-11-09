import sublime
import sublime_plugin


class RefreshFileAndFoldersCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('revert')
        self.window.run_command('refresh_folder_list')
