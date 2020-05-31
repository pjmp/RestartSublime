import sublime_plugin, subprocess, os, platform, sublime

class RestartSublimeInstanceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if platform.system() != 'Linux' and platform.system() != 'Darwin':
            sublime.error_message('Unsupported OS')
        else:
            # this will return pid of `plugin_host`
            my_pid=str(os.getpid())

            # get pid of parent process aka `sublime_text`
            parent_pid='ps -o ppid= ' + my_pid

            final_cmd='kill -9 $({0}) && subl'.format(parent_pid)

            subprocess.call(final_cmd, shell=True)
