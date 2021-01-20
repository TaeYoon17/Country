from req import oneFile
list=[
[6,"https://www.iso.org/committee/45674.html?view=participation"]
,[39,"https://www.iso.org/committee/48390.html?view=participation"]
,[87,"https://www.iso.org/committee/50400.html?view=participation"]
,[89,"https://www.iso.org/committee/50428.html?view=participation"]
,[165,"https://www.iso.org/committee/53584.html?view=participation"]
,[218,"https://www.iso.org/committee/54976.html?view=participation"]
,[238,"https://www.iso.org/committee/554401.html?view=participation"]
,[287,"https://www.iso.org/committee/4952370.html?view=participation"]
,[296,"https://www.iso.org/committee/5819148.html?view=participation"]
,[23,"https://www.iso.org/committee/47002.html?view=participation"]
,[29,"https://www.iso.org/committee/47464.html?view=participation"]
,[51,"https://www.iso.org/committee/48928.html?view=participation"]
,[61,"https://www.iso.org/committee/49256.html?view=participation"]
,[77,"https://www.iso.org/committee/50056.html?view=participation"]
,[146,"https://www.iso.org/committee/52702.html?view=participation"]
,[188,"https://www.iso.org/committee/54258.html?view=participation"]
,[219,"https://www.iso.org/committee/54988.html?view=participation"]
]
for li in list:
    oneFile(li[1],li[0])