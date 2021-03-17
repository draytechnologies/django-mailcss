import pynliner
import css_inline


class EngineBase(object):
    def __init__(self, html, css):
        self.html = html
        self.css = css

    def render(self):
        raise NotImplementedError()


class PynlinerEngine(EngineBase):
    def render(self):
        inliner = pynliner.Pynliner().from_string(self.html)
        inliner = inliner.with_cssString(self.css)
        return inliner.run()


class CSSInlineEngine(EngineBase):
    def render(self):
        inliner = css_inline.CSSInliner(extra_css=self.css)
        inlined = inliner.inline(self.html)
        return inlined


class NullEngine(EngineBase):
    def render(self):
        return self.html
