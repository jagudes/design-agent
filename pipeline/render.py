from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import playwright.sync_api
from .formats import *
from .spec import DesignSpec


env = Environment(
    loader=FileSystemLoader(Path(__file__).parent / "templates"),
    autoescape=True,
)


def render(spec: DesignSpec, out_dir: Path = Path("out")) -> dict[str, Path]:
    w, h = get_size(spec.format, spec.orientation)
    html = env.get_template("layout.html.j2").render(spec=spec, w=w, h=h)
    out_dir.mkdir(exist_ok=True)

    name = f"{spec.format}_{spec.orientation}"
    pdf_path = out_dir / f"{spec.format}.pdf"
    png_path = out_dir / f"{spec.format}.png"

    #zmiana mm na piksele
    px_w = round(w * 96 / 25.4)
    px_h = round(h * 96 / 25.4)

    with playwright.sync_api.sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": px_w, "height": px_h},
            device_scale_factor=300 / 96,  # PNG w ok. 300 DPI
        )
        page.set_content(html)
        page.pdf(
            path=str(pdf_path),
            width=f"{w}mm",
            height=f"{h}mm",
            print_background=True,
        )
        page.screenshot(path=str(png_path))
        browser.close()

    return {"pdf": pdf_path, "png": png_path}