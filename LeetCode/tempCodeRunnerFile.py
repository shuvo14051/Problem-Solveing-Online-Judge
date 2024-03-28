class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = []
        self.pages.append(homepage)
        self.current = 0

    def visit(self, url: str) -> None:
        self.current += 1
        self.pages.append(url)

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.pages[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.pages) - 1, self.current + steps)
        return self.pages[self.current]