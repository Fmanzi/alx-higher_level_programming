import dis
import marshal

with open("hidden_4.pyc", "rb") as pyc_file:
    code = marshal.load(pyc_file)

names = set()
for instruction in code.co_code:
    if instruction.opname == "STORE_NAME":
        name = code.co_names[instruction.arg]
        if not name.startswith("__"):
            names.add(name)

for name in sorted(names):
    print(name)
