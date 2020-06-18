class compiler:

    def __init__(self, sourcef, debug=False):
        self.sourcef = sourcef
        self.debug = debug

    def log(self, msg):
        if self.debug:
            print(msg)

    def readfile(self):
        self.log(f"openning {self.sourcef} ...")
        with open(self.sourcef) as f:
            self.sourcecode = f.read()
            self.log(f"source code: \n{self.sourcecode}")
            f.close()

    def translate(self):
        syntax = {
                "kek":"int", "smol":"short", "copypasta ":"char", "mod":"class", "rule34":"enum", "tfw":"if",
                "/b":"main", "an hero":"~", "pools closed":"}", "pools open":"{", "newfag": "new", "mod":"class",
                "dox":"return", "post":"puts", "rickroll":"*", "gib me ":"#include <", " plz":">", "wft":"else"
                }
        for x,y in syntax.items():
            self.sourcecode = self.sourcecode.replace(x, y)

        self.log(self.sourcecode)

    def writefile(self, outfile):
        with open(outfile, "w") as f:
            self.log(f"Opened {outfile} succefully")
            self.log("Inserting source code ...")
            f.write(self.sourcecode)
            self.log("writefile suceeded \nexitting ...")


# comp = compiler(sourcef="test.4lang", debug=True)
# comp.readfile()
# comp.translate()
# comp.writefile("test.c")
