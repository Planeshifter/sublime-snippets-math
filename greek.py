import sublime, sublime_plugin
import unicodedata

class GreekSubstitution(sublime_plugin.TextCommand):
    greek_map = {}
    greek_map["a"] = "\\alpha"
    greek_map["A"] = "\\Alpha"
    greek_map["b"] = "\\beta"
    greek_map["B"] = "\\Beta"

    def run(self, edit):
        view = self.view
        cursors = view.sel()
        cursor = cursors[0]

        word_region = view.word(cursor)
        word = view.substr(word_region)
        if word in self.greek_map:
            view.replace(edit, word_region, self.greek_map[word])