import sublime
import sublime_plugin
import time
import re


class InsertContentCommand(sublime_plugin.TextCommand):
    def run(self, edit, point, content):
        self.view.insert(edit, point, content)


class DraftAppendCommand(sublime_plugin.TextCommand):

    def run(self, edit, file=None, content=None):
        # Loads the specified file
        window = sublime.active_window()
        view = window.open_file(file)
        sublime.set_timeout(lambda: self.append_text(view, content), 10)

    def append_text(self, view, content):
        if not view.is_loading():
            view_size = view.size()
            # Paste the text in the end of the file
            view.run_command(
                "insert_content", {"point": view_size, "content": content})
        else:
            sublime.set_timeout(
                lambda: self.append_text(view, content), 10)


class DraftPrependCommand(sublime_plugin.TextCommand):

    def run(self, edit, file=None, content=None):
        # Loads the specified file
        window = sublime.active_window()
        view = window.open_file(file)
        sublime.set_timeout(lambda: self.prepend_text(view, content), 10)

    def prepend_text(self, view, content):
        if not view.is_loading():
            # Paste the text in the beginning of the file
            view.run_command(
                "insert_content", {"point": 0, "content": content})
        else:
            sublime.set_timeout(lambda: self.prepend_text(view, content), 10)


class DraftsPromptCommand(sublime_plugin.TextCommand):

    # Read prompt_config from settings
    prompt_config = sublime.load_settings(
        "Drafts.sublime-settings").get("prompt_config")

    def run(self, edit):
        panel_items = []
        for setting in self.prompt_config:
            panel_items.append([setting['name'], setting['file']])
        window = sublime.active_window()
        window.show_quick_panel(panel_items, self.draft_action)

    def draft_action(self, index):
        # If there is no selection, do nothing
        if index == -1: return

        # get the chosen action
        name = self.prompt_config[index]['name']
        action = self.prompt_config[index]['action']
        file = self.prompt_config[index]['file']
        content = self.prompt_config[index]['content']
        content = self.content_handler(content)

        if action == "prepend":
            sublime.status_message('Chosen item: ' + name)
            self.view.run_command(
                "draft_prepend", {"file": file, "content": content})
        elif action == "append":
            self.view.run_command(
                "draft_append", {"file": file, "content": content})
        else:
            self.status("Cannot find the right action")

    def content_handler(self, content):
        match = re.search(r'[[draft]]', content)
        if match:
            draft_content = self.get_draft_content()
            content = content.replace("[[draft]]", draft_content)

        match = re.search(r'[[date]]', content)
        if match:
            date_content = time.strftime("%Y-%m-%d %H:%M")
            content = content.replace("[[date]]", date_content)

        match = re.search('\[\[date\|.+\]\]', content)
        if match:
            content = re.sub('\[\[date\|.+\]\]', get_formated_date, content)

        return content

    def get_draft_content(self):
        # Save the document size
        view_size = self.view.size()
        # Get selections
        regions = self.view.sel()
        # Select the whole document, clear selection before
        regions.clear()
        regions.add(sublime.Region(0, view_size))

        # For each text selection region
        # for region in regions:
        draft_content = self.view.substr(regions[0])
        regions.clear()
        return draft_content


def get_formated_date(format):
    format = re.search('(?<=date\|)[^(\]\])]*(?=(\]\]))', format.group(0))
    return time.strftime(format.group(0))
