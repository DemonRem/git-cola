def create_button(text='', layout=None, tooltip=None, icon=None):
    if text:
        button.setText(tr(text))
    'color_text':           rgba(0x00, 0x00, 0x00),
        diff_head = self.mkformat(fg=self.color_header)
        diff_head_bold = self.mkformat(fg=self.color_header, bold=True)
        diff_add = self.mkformat(fg=self.color_text, bg=self.color_add)
        diff_remove = self.mkformat(fg=self.color_text, bg=self.color_remove)
            bad_ws = self.mkformat(fg=Qt.black, bg=Qt.red)