from pipeline.render import render
from pipeline.spec import DesignSpec

base = dict(
    title="Title",
    subtitle="subtitle",
    body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    date="11.11.1111 | 11:11",
    place="Place, Street 1111",
)

jobs = [
    ("poster", "portrait"),
    ("flyer", "portrait"),
    ("invitation", "landscape"),
]

for fmt, orientation in jobs:
    print(render(DesignSpec(format=fmt, orientation=orientation, **base)))