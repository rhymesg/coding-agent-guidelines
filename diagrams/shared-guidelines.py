"""Write shared-guidelines.svg beside this file: a team's shared rules and knowledge reaching every project, a lesson or a
solved problem in one coming back, kept current and used by agents, and the engineers reading each other's results alike."""
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent

PAPER, INK, MUTED = "#FBF8F3", "#1E2235", "#6B7280"
INDIGO, INDIGO_SOFT, CORAL, SAGE = "#2B3A67", "#C9D3EE", "#E07A5F", "#5E9C7F"
FONTS = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"

W, H = 900, 800
HUB = (450, 450)
HUB_R = 84
PROJECTS = {               # name: (centre, width, height, dashed)
    "project": ((165, 450), 170, 64, False),
    "another project": ((735, 450), 190, 64, False),
    "next project": ((450, 690), 200, 64, True),
}
KNOWLEDGE = ((450, 150), 210, 60)   # centre, width, height; it sits on the engineers' ring
NEXT_SUB = "quick setup"   # a new project starts from the guidelines
RING = (420, 300)          # ellipse radii the engineers sit on
ENGINEERS = [(150, False), (210, False), (-30, False), (30, False), (90, True)]   # (angle in degrees, faded)
LABEL = 50                 # where on the ring its label sits, in degrees


def head(tip, ux, uy, length=13, half=6.5):
    bx, by = tip[0] - ux * length, tip[1] - uy * length
    return f"{tip[0]:.1f},{tip[1]:.1f} {bx - uy * half:.1f},{by + ux * half:.1f} {bx + uy * half:.1f},{by - ux * half:.1f}"


def arrow(i, start, end, dashed):
    ux, uy = end[0] - start[0], end[1] - start[1]
    n = math.hypot(ux, uy)
    ux, uy = ux / n, uy / n
    line_end = end[0] - ux * 12, end[1] - uy * 12
    dash = ' stroke-dasharray="6 6"' if dashed else ""
    return (f'<path id="spoke{i}" class="spoke" d="M{start[0]:.1f},{start[1]:.1f} L{line_end[0]:.1f},{line_end[1]:.1f}"{dash}/>'
            f'<polygon class="spoke-head" points="{head(end, ux, uy)}"/>'
            f'<circle class="pulse" r="4"><animateMotion dur="2.2s" begin="{i * 0.5:.1f}s" repeatCount="indefinite">'
            f'<mpath href="#spoke{i}"/></animateMotion></circle>')


def spokes():
    x, y = HUB
    r = HUB_R + 22
    (ax, ay), aw, _, _ = PROJECTS["project"]
    (bx, by), bw, _, _ = PROJECTS["another project"]
    (nx, ny), _, nh, _ = PROJECTS["next project"]
    return [arrow(0, (x - r, y), (ax + aw / 2, ay), False),
            arrow(1, (x + r, y), (bx - bw / 2, by), False),
            arrow(2, (x, y + r), (nx, ny - nh / 2), True)]


def project(name):
    (x, y), w, h, dashed = PROJECTS[name]
    text = (f'<text class="name" x="{x}" y="{y - 9}">{name}</text><text class="sub" x="{x}" y="{y + 13}">{NEXT_SUB}</text>'
            if dashed else f'<text class="name" x="{x}" y="{y}">{name}</text>')
    return (f'<g class="project{" next" if dashed else ""}"><rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" '
            f'height="{h}" rx="10"/>{text}</g>')


def bezier(p0, p1, p2, t):
    return tuple((1 - t) ** 2 * a + 2 * (1 - t) * t * b + t ** 2 * c for a, b, c in zip(p0, p1, p2))


def curve(name, p0, p1, p2, steps, note, note_at):
    """A dotted way back from a project, with an arrowhead, a moving dot and its steps as labels."""
    before = bezier(p0, p1, p2, 0.97)
    ux, uy = p2[0] - before[0], p2[1] - before[1]
    n = math.hypot(ux, uy)
    ux, uy = ux / n, uy / n
    end = p2[0] - ux * 12, p2[1] - uy * 12
    out = [f'<path id="{name}" class="loop" d="M{p0[0]:.1f},{p0[1]:.1f} Q{p1[0]},{p1[1]} {end[0]:.1f},{end[1]:.1f}"/>',
           f'<polygon class="loop-head" points="{head(p2, ux, uy)}"/>',
           f'<circle class="lesson" r="5"><animateMotion dur="3.2s" repeatCount="indefinite">'
           f'<mpath href="#{name}"/></animateMotion></circle>']
    for t, text in steps:
        px, py = bezier(p0, p1, p2, t)
        pw = len(text) * 7 + 24
        out.append(f'<g class="step"><rect x="{px - pw / 2:.1f}" y="{py - 14:.1f}" width="{pw:.1f}" height="28" rx="6"/>'
                   f'<text x="{px:.1f}" y="{py:.1f}">{text}</text></g>')
    out.append(f'<text class="note" x="{note_at[0]:.1f}" y="{note_at[1]:.1f}">{note}</text>')
    return out


def loops():
    """A lesson goes back into the rules; a solved problem goes into the knowledge."""
    (x, y), w, h, _ = PROJECTS["project"]
    p0 = x - w * 0.1, y - h / 2
    a = math.radians(236)
    p2 = HUB[0] + (HUB_R + 22) * math.cos(a), HUB[1] + (HUB_R + 22) * math.sin(a)
    out = curve("rules-loop", p0, (270, 150), p2, ((0.18, "improvement MR"), (0.9, "consistency check")),
                "lesson learned", (p0[0] - 52, p0[1] - 14))
    (x, y), w, h, _ = PROJECTS["another project"]
    q0 = x + w * 0.1, y - h / 2
    (kx, ky), _, kh = KNOWLEDGE
    out += curve("knowledge-loop", q0, (640, 260), (kx + 60, ky + kh / 2), ((0.5, "added by agents"),),
                 "problem solved", (q0[0] + 50, q0[1] - 14))
    return out


def knowledge():
    """The team's shared knowledge on the engineers' ring: every engineer's agents search it and add to it."""
    (x, y), w, h = KNOWLEDGE
    return [f'<g class="knowledge"><rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" height="{h}" rx="10"/>'
            f'<text class="name" x="{x}" y="{y - 10}">shared knowledge</text>'
            f'<text class="sub" x="{x}" y="{y + 13}">wiki · solved problems</text></g>']


def report(x, y):
    """A small report card: a title bar, a line and a rising chart, the same for every engineer."""
    return (f'<g class="report"><rect class="sheet" x="{x - 13:.1f}" y="{y - 17:.1f}" width="26" height="34" rx="3"/>'
            f'<rect class="ink" x="{x - 8:.1f}" y="{y - 12:.1f}" width="16" height="3" rx="1"/>'
            f'<rect class="ink" x="{x - 8:.1f}" y="{y - 6:.1f}" width="11" height="2" rx="1"/>'
            f'<polyline class="chart" points="{x - 8:.1f},{y + 11:.1f} {x - 3:.1f},{y + 5:.1f} {x + 2:.1f},{y + 8:.1f} '
            f'{x + 8:.1f},{y:.1f}"/></g>')


def on_ring(angle):
    a = math.radians(angle)
    return HUB[0] + RING[0] * math.cos(a), HUB[1] + RING[1] * math.sin(a)


def engineer(angle, faded):
    """An engineer badge and, unless faded, the report beside it."""
    px, py = on_ring(angle)
    card = "" if faded else report(px + (42 if math.cos(math.radians(angle)) > 0 else -42), py)
    return (f'<g class="person{" faded" if faded else ""}"><circle class="badge" cx="{px:.1f}" cy="{py:.1f}" r="21"/>'
            f'<circle class="figure" cx="{px:.1f}" cy="{py - 6:.1f}" r="6"/>'
            f'<path class="figure" d="M{px - 11:.1f},{py + 12:.1f} a11,9 0 0 1 22,0 Z"/>{card}</g>')


def ring():
    """The engineers around their projects, joined by one ring: they read each other's results alike."""
    x, y = HUB
    out = [f'<ellipse class="ring-line" cx="{x}" cy="{y}" rx="{RING[0]}" ry="{RING[1]}">'
           '<animate attributeName="stroke-dashoffset" values="0;-24" dur="1.2s" repeatCount="indefinite"/></ellipse>']
    out += [engineer(angle, faded) for angle, faded in ENGINEERS]
    lx, ly = on_ring(LABEL)
    text = "consistent results and reports"
    w = len(text) * 7.4 + 30
    out.append(f'<g class="ring-label"><rect x="{lx - w / 2:.1f}" y="{ly - 15:.1f}" width="{w:.1f}" height="30" rx="6"/>'
               f'<text x="{lx:.1f}" y="{ly:.1f}">{text}</text></g>')
    return out


def hub():
    x, y = HUB
    return [f'<circle class="halo" cx="{x}" cy="{y}" r="{HUB_R + 40}">'
            f'<animate attributeName="r" values="{HUB_R + 26};{HUB_R + 46};{HUB_R + 26}" dur="3s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0.6;0.15;0.6" dur="3s" repeatCount="indefinite"/></circle>',
            f'<circle class="hub-ring" cx="{x}" cy="{y}" r="{HUB_R + 12}"/>',
            f'<circle class="hub" cx="{x}" cy="{y}" r="{HUB_R}"/>',
            f'<text class="hub-name" x="{x}" y="{y - 10}">team plugin</text>',
            f'<text class="hub-sub" x="{x}" y="{y + 20}">agents · CI · review</text>']


def svg():
    style = f"""
text {{ font-family: {FONTS}; dominant-baseline: central; text-anchor: middle; }}
.bg {{ fill: {PAPER}; stroke: #E8E2D8; stroke-width: 1; }}
.title {{ fill: {INK}; font-size: 30px; font-weight: 600; text-anchor: start; }}
.subtitle {{ fill: {MUTED}; font-size: 17px; font-weight: 400; text-anchor: start; }}
.halo {{ fill: {INDIGO_SOFT}; }}
.hub-ring {{ fill: none; stroke: {INDIGO}; stroke-width: 1.5; stroke-dasharray: 3 7; opacity: 0.6; }}
.hub {{ fill: {INDIGO}; }}
.hub-name {{ fill: {PAPER}; font-size: 26px; font-weight: 600; }}
.hub-sub {{ fill: {PAPER}; font-size: 14px; font-weight: 400; opacity: 0.85; }}
.spoke {{ fill: none; stroke: {INDIGO}; stroke-width: 2; opacity: 0.55; }}
.spoke-head {{ fill: {INDIGO}; opacity: 0.7; }}
.pulse {{ fill: {CORAL}; }}
.knowledge rect {{ fill: {SAGE}; }}
.knowledge .name {{ fill: #FFFFFF; font-size: 18px; font-weight: 600; }}
.knowledge .sub {{ fill: #FFFFFF; font-size: 13px; opacity: 0.9; }}
.project > rect {{ fill: #FFFFFF; stroke: {INDIGO}; stroke-width: 1.5; }}
.project.next > rect {{ fill: none; stroke: {MUTED}; stroke-dasharray: 6 5; }}
.project .name {{ fill: {INK}; font-size: 19px; font-weight: 600; }}
.project .sub {{ fill: {MUTED}; font-size: 13px; font-weight: 400; }}
.note {{ fill: {MUTED}; font-size: 13px; font-style: italic; }}
.loop {{ fill: none; stroke: {CORAL}; stroke-width: 2; stroke-dasharray: 2 6; stroke-linecap: round; }}
.loop-head {{ fill: {CORAL}; }}
.lesson {{ fill: {CORAL}; }}
.step rect {{ fill: {PAPER}; stroke: {CORAL}; stroke-width: 1.2; }}
.step text {{ fill: {INK}; font-size: 13px; }}
.ring-line {{ fill: none; stroke: {INK}; stroke-width: 1.5; stroke-dasharray: 4 8; opacity: 0.3; }}
.person .badge {{ fill: {CORAL}; }}
.person .figure {{ fill: #FFFFFF; }}
.person.faded {{ opacity: 0.45; }}
.report .sheet {{ fill: #FFFFFF; stroke: #D9D3C7; stroke-width: 1; }}
.report .ink {{ fill: {INK}; opacity: 0.7; }}
.report .chart {{ fill: none; stroke: {SAGE}; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }}
.ring-label rect {{ fill: {PAPER}; stroke: {MUTED}; stroke-width: 1; }}
.ring-label text {{ fill: {INK}; font-size: 14px; }}
"""
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
             f"<style>{style}</style>", f'<rect class="bg" x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18"/>',
             '<text class="title" x="48" y="56">Shared rules and knowledge</text>',
             '<text class="subtitle" x="48" y="90">Kept current by agents: a lesson learned once helps every project</text>']
    parts += ring()
    parts += knowledge()
    parts += hub()
    parts += spokes()
    parts += loops()
    parts += [project(name) for name in PROJECTS]
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    (HERE / "shared-guidelines.svg").write_text(svg())
