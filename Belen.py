from jinja2 import Environment, FileSystemLoader
import random


MINUTES = 60000
env = Environment(loader=FileSystemLoader("templates/"))

name = 'Belen'
include = '{$INCLUDE CHAINER_SCRIPTS/'
username = 'belentokyo@gmail.com'
password = 'Remerexosrs123'
levels = [1, 1, 1, 1, 1]
daysAlive = 0


# Cambiar por un template que venga de f({account.name}_Chainer_Template)
template = env.get_template(f"{name}_Chainer_Template")

LowIntensityScripts = [
    # ["SandyBot", f"{include}CH_{name}_Sandycrabs.simba" + "}"],
    ["Ration_cooker", f"{include}CH_{name}_Rations.simba" + "}"],
]

MidIntensityScripts = [
    # ["SandyBot", f"{include}CH_{name}_Sandycrabs.simba" + "}"],
    ["KnightsThiever", f"{include}CH_{name}ArdyKnights.simba" + "}"],
    ["FlaxSpinner", f"{include}CH_{name}FlaxMaker.simba" + "}"],
    ["TitheFarmer", f"{include}CH_{name}TitheFarm.simba" + "}"],
]

HighIntensityScripts = [
    ["gotr", f"{include}CH_{name}_gotr.simba" + "}"],
    ["agility", f"{include}CH_{name}_agility.simba" + "}"],
    ["TitheFarmer", f"{include}CH_{name}TitheFarm.simba" + "}"],
]


class Block:
    def setupBlock(self, blockNumber):
        self.script = []

        match blockNumber:
            case 0:
                self.script = random.choice(LowIntensityScripts)
                self.timeToRun = random.randint(90 * MINUTES, 120 * MINUTES)
                self.blockNumber = blockNumber
            case 1:
                self.script = random.choice(LowIntensityScripts)
                self.timeToRun = random.randint(85 * MINUTES, 100 * MINUTES)
                self.blockNumber = blockNumber
            case 2:
                self.script = random.choice(HighIntensityScripts)
                self.timeToRun = random.randint(110 * MINUTES, 130 * MINUTES)
                self.blockNumber = blockNumber
            case 3:
                self.script = random.choice(HighIntensityScripts)
                self.timeToRun = random.randint(90 * MINUTES, 120 * MINUTES)
                self.blockNumber = blockNumber
            case 4:
                self.script = random.choice(MidIntensityScripts)
                self.timeToRun = random.randint(100 * MINUTES, 110 * MINUTES)
                self.blockNumber = blockNumber
            case 5:
                self.script = random.choice(LowIntensityScripts)
                self.timeToRun = random.randint(85 * MINUTES, 100 * MINUTES)
                self.blockNumber = blockNumber


Waits = []
Waits.append("Wait(" + str(random.randint(160 * MINUTES, 190 * MINUTES)) + ");")
Waits.append("Wait(" + str(random.randint(110 * MINUTES, 130 * MINUTES)) + ");")
Waits.append("Wait(" + str(random.randint(110 * MINUTES, 130 * MINUTES)) + ");")


# Init blocks
Block1 = Block()
Block2 = Block()
Block3 = Block()
Block4 = Block()
Block5 = Block()
Block6 = Block()

Block1.setupBlock(0)
Block2.setupBlock(1)
Block3.setupBlock(2)
Block4.setupBlock(3)
Block5.setupBlock(4)
Block6.setupBlock(5)
BlockArray = [Block1, Block2, Block3, Block4, Block5, Block6]

Includes = []
RunAndSetup = [[], [], [], [], [], []]
for SelectedBlock in BlockArray:
    Includes.append(SelectedBlock.script[1])

    RunAndSetup[SelectedBlock.blockNumber].append(f"{SelectedBlock.script[0]}.ChainerRun({SelectedBlock.timeToRun});")
    RunAndSetup[SelectedBlock.blockNumber].append(SelectedBlock.blockNumber)

    # RunAndSetup['Run'].append(f"{SelectedBlock.script[0]}.ChainerRun({SelectedBlock.timeToRun},{SelectedBlock.actions})")
    # RunAndSetup['Setup'].append(f"{SelectedBlock.script[0]}.AntibanSetup()")

Includes = list(dict.fromkeys(Includes))

filename = f"Chainer_{name}.simba"

content = template.render(includes=Includes, RunAndSetup=RunAndSetup, waits=Waits)
# print(RunAndSetup)

with open(filename, mode="w", encoding="utf-8") as script:
    script.write(content)
    print(f". . . wrote{filename}")
