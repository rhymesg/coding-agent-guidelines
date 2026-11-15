#!/bin/bash
# Lists each workplan's last change, size, plan files, Git checkouts, and the processes and containers using it.
# Usage: survey.sh [workplans-dir]   (default: ./workplans)
cd "${1:-workplans}" || exit 1
now=$(date +%s)
days() { echo $(( (now - ${1%.*}) / 86400 )); }

for d in */; do
  d=${d%/}
  newest=$(find "$d" -path '*/.git' -prune -o -type f -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1)
  plan=$(for f in objective.md tasks.md report.md; do [ -f "$d/$f" ] && printf ' %s' "$f"; done)
  echo "=== $d | age=$(days "${newest%% *}")d | size=$(du -sh "$d" 2>/dev/null | cut -f1) | newest=${newest#* } |$plan"
  find "$d" -name .git -prune -print 2>/dev/null | while read -r g; do
    w=$(dirname "$g")
    tracked=$(git -C "$w" rev-parse --abbrev-ref "$(git -C "$w" remote | head -1)/HEAD" 2>/dev/null)
    merged=no; [ -n "$tracked" ] && git -C "$w" merge-base --is-ancestor HEAD "$tracked" 2>/dev/null && merged=yes
    echo "   git $w | branch=$(git -C "$w" rev-parse --abbrev-ref HEAD 2>/dev/null)" \
      "| dirty=$(git -C "$w" status --porcelain 2>/dev/null | wc -l)" \
      "| commit-age=$(days "$(git -C "$w" log -1 --format=%ct 2>/dev/null || echo 0)")d" \
      "| on-remote=$(git -C "$w" branch -r --contains HEAD 2>/dev/null | wc -l)" \
      "| merged-into-${tracked:-?}=$merged"
  done
done

echo "=== processes using workplans/"
ps -eo pid,args | grep -F "workplans/" | grep -v -e grep -e survey.sh
echo "=== containers mounting workplans/"
docker ps --format '{{.Names}}' 2>/dev/null | while read -r c; do
  m=$(docker inspect "$c" --format '{{range .Mounts}}{{.Source}} {{end}}' | tr ' ' '\n' | grep workplans/)
  [ -n "$m" ] && echo "$c: $m"
done
