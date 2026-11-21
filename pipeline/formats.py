# orientację ustala get_size
FORMATS = {
    "poster": (297, 420),
    "flyer": (148, 210),
    "invitation": (216, 102),
}


def get_size(fmt: str, orientation: str) -> tuple[int, int]:
    short, long = sorted(FORMATS[fmt])
    return (long, short) if orientation == "landscape" else (short, long)