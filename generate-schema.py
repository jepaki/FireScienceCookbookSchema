"""
Script to generate JSON schemas and markdown documentation from pydantic models.
Usage: python scripts/generate-schema.py <schema_file.py> <RootModel>

"""
# sudo apt install libgraphviz-dev
from json import dumps
from jsonschema2md import Parser
import erdantic as erd
from pydantic import BaseModel
from pathlib import Path
from importlib import import_module
import sys

# Define PYTHONPATH

schema_file = "/home/oryx/PycharmProjects/FireScienceCookbook/FireScienceCookbookSchema/schema.py"
root_models = ["ProspectivityModel"]

# Get the output directory
fn = Path(schema_file)
output_dir = fn.parent
name = fn.stem

print(name, output_dir, fn)
sys.path.append(str(output_dir))


# print(Path.cwd())
# Convert filename to module name
# Import the schema file
# mod_name = schema_file.replace("/", ".").replace(".py", "")
# print(mod_name)
mod = import_module(name=fn.stem)

models = []
for root_model in root_models:
    # Find the root model
    RootModel = getattr(mod, root_model)
    assert issubclass(RootModel, BaseModel)
    models.append(RootModel)

graph = erd.create(*models)

# Draw the entity-relation diagram
erd_file = output_dir / (name + ".png")
print(erd_file)
graph.draw(out=erd_file)


schemas = [RootModel.model_json_schema() for RootModel in models]

json_file = output_dir / (name + ".json")
with json_file.open("w") as f:
    f.write(dumps(schemas, indent=2))

parser = Parser(
    examples_as_yaml=False,
)

md_lines = []

print(graph.models)
print(list(graph.models.keys()))
print(models)
#sub_models = [d.model for d in graph.models if d.model not in models]
doc_models = models #+ sub_models

for d in doc_models:
    schema = d.model_json_schema()
    lines = parser.parse_schema(schema)
    md_lines.extend(lines)
    md_lines.append("\n")

text = "".join(md_lines).replace("#/$defs/", "").replace("#$defs/", "#")
# Move headers down a level
text = text.replace("\n#", "\n##")

doc_file = output_dir / (name + ".md")
with doc_file.open("w") as f:
    f.write(text)